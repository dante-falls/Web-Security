-- Comprehensive Directory Scanning Script with Enhanced Features.
-- Checks for the presence of directories on a specified web server and gathers additional information.
-- Allows user-specified file for directory list, optional base directory prefix, skipping 404 responses, and shows a summary.
-- Params: dirscan-plus-fileLocation='/path/to/list.txt',dirscan-plus-base-directory='/base/path',dirscan-plus-skip-404=true
-- Usage:
-- nmap --script dirscan-plus --script-args dirscan-plus-fileLocation='/path/to/list.txt',dirscan-plus-base-directory='/base/path',dirscan-plus-skip-404=true
-- Original Author: emrekybs
-- Secondary Author: cybernerddante, ChatGPT

categories = {"safe", "discovery"}

portrule = function(host, port)
    return port.number == 80 or port.number == 443
end

local function extract_title(body)
    local title = body:match("<title>(.-)</title>")
    return title or "No title"
end

action = function(host, port)
    local http = require "http"
    local stdnse = require "stdnse"

    local file_path = stdnse.get_script_args("dirscan-plus-fileLocation")
    local base_dir = stdnse.get_script_args("dirscan-plus-base-directory") or ""
    local skip_404 = stdnse.get_script_args("dirscan-plus-skip-404")

    -- Normalize skip_404 flag (default: false)
    local skip_404_flag = false
    if skip_404 and (skip_404 == "true" or skip_404 == "yes" or skip_404 == "1") then
        skip_404_flag = true
    end

    local dirs = {}

    -- Load directories from user-supplied file
    if file_path then
        local file, err = io.open(file_path, "r")
        if not file then
            return "Error: Could not open file: " .. (err or "unknown error")
        end
        for line in file:lines() do
            if line ~= "" then
                -- Ensure each line starts with '/'
                if not line:match("^/") then
                    line = "/" .. line
                end
                -- Combine base directory and wordlist entry
                local full_path = base_dir .. line
                -- Avoid double slashes
                full_path = full_path:gsub("//+", "/")
                table.insert(dirs, full_path)
            end
        end
        file:close()
    else
        return "Error: Missing required argument 'dirscan-plus-fileLocation'. Example usage: --script-args dirscan-plus-fileLocation='/path/to/list.txt'"
    end

    local results = {}
    local total_scanned = 0
    local total_valid = 0

    for _, dir in ipairs(dirs) do
        total_scanned = total_scanned + 1

        local start_time = stdnse.clock_ms()
        local response = http.get(host, port, dir)
        local end_time = stdnse.clock_ms()
        local response_time = math.floor(end_time - start_time)

        if response.status then
            -- Skip 404 responses if the flag is true
            if skip_404_flag and tonumber(response.status) == 404 then
                goto continue
            end

            total_valid = total_valid + 1

            local title = extract_title(response.body)
            local content_length = response.header["content-length"] or "Unknown"
            local server_header = response.header["server"] or "Unknown"
            local location_header = response.header["location"] or "No redirection"

            local result = string.format(
                "Directory: %s - Status Code: %s - Title: %s - Content Length: %s - Server: %s - Redirection: %s - Response Time: %d ms",
                dir, response.status, title, content_length, server_header, location_header, response_time
            )
            table.insert(results, result)
        end

        ::continue::
    end

    -- Add summary
    table.insert(results, "")
    table.insert(results, string.format("Summary: Scanned %d directories, %d valid responses%s", 
        total_scanned, total_valid, skip_404_flag and " (404 responses skipped)" or ""))

    if #results == 0 then
        return "No directories found or no valid responses received."
    end

    return stdnse.format_output(true, results)
end
