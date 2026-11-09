import json
import sys


def load_introspection(filename):
    """Load a GraphQL introspection response from a TXT/JSON file."""

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Handle:
    # {"data": {"__schema": {...}}}
    if "data" in data and "__schema" in data["data"]:
        return data["data"]["__schema"]

    # Handle:
    # {"__schema": {...}}
    if "__schema" in data:
        return data["__schema"]

    # Handle:
    # {"data": {"__schema": ...}} variants
    if "data" in data and isinstance(data["data"], dict):
        if "__schema" in data["data"]:
            return data["data"]["__schema"]

    raise ValueError("Could not find GraphQL __schema in the introspection response.")


def build_type(type_info):
    """
    Convert GraphQL introspection type information into a GraphQL type string.

    Examples:
        String
        String!
        [String]
        [String!]!
    """

    if not type_info:
        return "Unknown"

    kind = type_info.get("kind")
    name = type_info.get("name")

    if kind == "NON_NULL":
        return build_type(type_info.get("ofType")) + "!"

    if kind == "LIST":
        return "[" + build_type(type_info.get("ofType")) + "]"

    return name or "Unknown"


def unwrap_type(type_info):
    """Return the underlying named type from a nested GraphQL type."""

    while type_info:
        kind = type_info.get("kind")

        if kind in ("NON_NULL", "LIST"):
            type_info = type_info.get("ofType")
        else:
            return type_info

    return {}


def is_required(type_info):
    """Determine whether a GraphQL argument is required."""

    return bool(type_info and type_info.get("kind") == "NON_NULL")


def default_variable_value(type_info):
    """
    Generate an empty value suitable for the variable.

    Strings/IDs/etc. use an empty string.
    Lists use an empty list.
    Input objects use an empty object.
    """

    if not type_info:
        return ""

    # Remove NON_NULL wrapper
    if type_info.get("kind") == "NON_NULL":
        return default_variable_value(type_info.get("ofType"))

    if type_info.get("kind") == "LIST":
        return []

    kind = type_info.get("kind")

    if kind == "INPUT_OBJECT":
        return {}

    if kind == "ENUM":
        return ""

    # Scalars such as String, ID, Int, Float, Boolean
    return ""


def format_argument_definition(arg):
    """Create a GraphQL variable definition."""

    name = arg.get("name", "unknown")
    arg_type = build_type(arg.get("type"))

    return f"${name}: {arg_type}"


def format_argument_usage(arg):
    """Create the argument portion used inside the query."""

    name = arg.get("name", "unknown")

    return f"{name}: ${name}"


def process_operation(field, operation_type, type_map):
    """
    Convert a GraphQL query/mutation field into a usable operation template.
    """

    field_name = field.get("name", "unknown")
    args = field.get("args") or []

    required_args = [
        arg for arg in args
        if is_required(arg.get("type"))
    ]

    all_args = [
        arg for arg in args
        if arg.get("name")
    ]

    # Variable definitions
    variable_definitions = ", ".join(
        format_argument_definition(arg)
        for arg in required_args
    )

    # Argument usage
    argument_usage = ", ".join(
        format_argument_usage(arg)
        for arg in required_args
    )

    # Operation declaration
    if variable_definitions:
        operation_header = (
            f"{operation_type} {field_name}"
            f"({variable_definitions})"
        )
    else:
        operation_header = f"{operation_type} {field_name}"

    # Field invocation
    if argument_usage:
        field_invocation = f"{field_name}({argument_usage})"
    else:
        field_invocation = field_name

    # We don't know the selection set from the field alone.
    # "..." allows the user to fill in the requested fields.
    operation = (
        f"{operation_header} {{\n"
        f"  {field_invocation}\n"
        f"}}"
    )

    # Variables JSON
    variables = {}

    for arg in required_args:
        variables[arg["name"]] = default_variable_value(arg.get("type"))

    return {
        "operation": operation,
        "variables": variables,
        "field": field,
        "required_args": required_args,
        "all_args": all_args,
    }


def main():

    if len(sys.argv) != 3:
        print(
            f"Usage: {sys.argv[0]} <introspection.txt> <output.txt>"
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        schema = load_introspection(input_file)
    except Exception as e:
        print(f"[!] Failed to load introspection response: {e}")
        sys.exit(1)

    # Build a map of all types.
    type_map = {
        t.get("name"): t
        for t in schema.get("types", [])
        if t.get("name")
    }

    query_type = schema.get("queryType")
    mutation_type = schema.get("mutationType")

    queries = []
    mutations = []

    # -------------------------
    # Queries
    # -------------------------

    if query_type:
        query_name = query_type.get("name")
        query_definition = type_map.get(query_name)

        if query_definition:
            for field in query_definition.get("fields") or []:
                queries.append(
                    process_operation(
                        field,
                        "query",
                        type_map
                    )
                )

    # -------------------------
    # Mutations
    # -------------------------

    if mutation_type:
        mutation_name = mutation_type.get("name")
        mutation_definition = type_map.get(mutation_name)

        if mutation_definition:
            for field in mutation_definition.get("fields") or []:
                mutations.append(
                    process_operation(
                        field,
                        "mutation",
                        type_map
                    )
                )

    # -------------------------
    # Write output
    # -------------------------

    with open(output_file, "w", encoding="utf-8") as f:

        f.write("=" * 80 + "\n")
        f.write("GRAPHQL QUERIES\n")
        f.write("=" * 80 + "\n\n")

        for i, item in enumerate(queries, 1):

            f.write(f"[QUERY {i}] {item['field']['name']}\n")
            f.write("-" * 80 + "\n")

            f.write(item["operation"])
            f.write("\n\n")

            f.write("Variables:\n")
            f.write(
                json.dumps(
                    item["variables"],
                    indent=2
                )
            )
            f.write("\n\n")

            # Show all arguments for reference
            if item["all_args"]:
                f.write("Arguments:\n")

                for arg in item["all_args"]:
                    arg_name = arg.get("name")
                    arg_type = build_type(arg.get("type"))

                    required = (
                        "REQUIRED"
                        if is_required(arg.get("type"))
                        else "optional"
                    )

                    f.write(
                        f"  - {arg_name}: "
                        f"{arg_type} ({required})\n"
                    )

                f.write("\n")

            f.write("\n")

        f.write("\n")
        f.write("=" * 80 + "\n")
        f.write("GRAPHQL MUTATIONS\n")
        f.write("=" * 80 + "\n\n")

        for i, item in enumerate(mutations, 1):

            f.write(f"[MUTATION {i}] {item['field']['name']}\n")
            f.write("-" * 80 + "\n")

            f.write(item["operation"])
            f.write("\n\n")

            f.write("Variables:\n")
            f.write(
                json.dumps(
                    item["variables"],
                    indent=2
                )
            )
            f.write("\n\n")

            if item["all_args"]:
                f.write("Arguments:\n")

                for arg in item["all_args"]:
                    arg_name = arg.get("name")
                    arg_type = build_type(arg.get("type"))

                    required = (
                        "REQUIRED"
                        if is_required(arg.get("type"))
                        else "optional"
                    )

                    f.write(
                        f"  - {arg_name}: "
                        f"{arg_type} ({required})\n"
                    )

                f.write("\n")

            f.write("\n")

    print(f"[+] Extracted {len(queries)} queries")
    print(f"[+] Extracted {len(mutations)} mutations")
    print(f"[+] Output written to: {output_file}")


if __name__ == "__main__":
    main()
