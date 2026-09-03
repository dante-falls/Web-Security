<h1>GraphQL IDORs</h1>

GraphQL API's can also suffer from Access Control Issues, such as Insecure Direct Object References (IDORs). Sometimes, developers forget to write proper authorization checks into the GraphQL Resolver for a query or mutation. This means that anyone 
can use the GraphQL Query or Mutation to view or modify other user's data. You can test GraphQL queries and mutations for IDORs the same way you would any other API request. Change the object identifier value and see if you can view or modify another
user's data.

<h1>GraphQL Introspection</h1>

GraphQL Introspection is one of my best-friends. A good portion of the IDORs I have reported are because GraphQL Introspection was enabled in the testing environment, which allowed me to appropriately test all the operations.

When you're testing your target, search through your proxy history for endpoints receiving GraphQL Queries or Mutations. Then test the endpoint with an introspection query and see if Introspection is enabled.

If Introspection is enabled, you now have a map of every query and mutation at your fingertips, allowing you to systematically check authorization boundaries and hunt for IDORs in GraphQL operations you might have missed by simply utilizing 
the web application.

Here is an example of an Introspection query:

<code>{"query": "query IntrospectionQuery{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}"}</code>

See the below image of a GraphQL Introspection query and the server's response

<img width="1412" height="632" alt="graphql-introspection" src="https://github.com/user-attachments/assets/51210780-7f22-46ca-ace3-21c1854898c6" />
