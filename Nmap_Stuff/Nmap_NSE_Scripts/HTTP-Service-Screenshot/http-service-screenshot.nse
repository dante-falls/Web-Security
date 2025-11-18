local stdnse = require "stdnse"
local shortport = require "shortport"
local http = require "http"
local os = require "os"
local nmap = require "nmap"
local sslcert = require "sslcert"

description = [[
Custom script: capture HTTP/HTTPS screenshots + WhatWeb enumeration,
then generate http-services.html and http-services-list.txt.
]]

author = "CyberNerdDante AND Sage (ChatGPT)"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"default", "discovery", "safe"}

portrule = function(host, port)
    return shortport.port_or_service({80, 443}, {"http", "https"})(host, port)
        or (port.version and port.version.service and port.version.service:match("http"))
        or (port.version and port.version.name and port.version.name:match("http"))
        or (port.version and port.version.product and port.version.product:match("http"))
end

local function escape_html(str)
    if not str then return "" end
    return (str
        :gsub("&", "&amp;")
        :gsub("<", "&lt;")
        :gsub(">", "&gt;")
        :gsub('"', "&quot;")
        :gsub("'", "&#39;")
    )
end

-- Storage for postrule
nmap.registry.http_services = nmap.registry.http_services or {}

action = function(host, port)
    local ip = host.ip

    --------------------------------------------------------------------
    -- ROBUST HTTPS DETECTION
    --------------------------------------------------------------------
    local is_https = false

    -- Nmap version info
    if port.version then
        if port.version.tunnel == "ssl" then
            is_https = true
        elseif port.version.service and port.version.service:lower():match("https") then
            is_https = true
        end
    end

    -- Direct service name
    if port.service == "https" then
        is_https = true
    end

    -- LIVE SSL PROBE
    local cert_raw = sslcert.getCertificate(host, port)
    if cert_raw then
        is_https = true
    end

    --------------------------------------------------------------------
    -- Build URL + filenames
    --------------------------------------------------------------------
    local scheme = is_https and "https" or "http"
    local scheme_upper = is_https and "HTTPS" or "HTTP"

    local url = ("%s://%s:%d"):format(scheme, ip, port.number)
    local screenshot_file = ("%s-%s-%d.jpg"):format(scheme_upper, ip, port.number)

    --------------------------------------------------------------------
    -- Run CutyCapt
    --------------------------------------------------------------------
    local cutycapt_cmd =
        ("cutycapt --url='%s' --out='%s' --insecure"):format(url, screenshot_file)
    os.execute(cutycapt_cmd)

    --------------------------------------------------------------------
    -- Run WhatWeb
    --------------------------------------------------------------------
    local tmpfile = ("whatweb-%s-%d.tmp"):format(ip, port.number)
    local whatweb_cmd =
        ("whatweb '%s' --color=NEVER --user-agent 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' --no-errors > '%s'")
        :format(url, tmpfile)

    os.execute(whatweb_cmd)

    local wf = io.open(tmpfile, "r")
    local whatweb_output = wf and wf:read("*all") or ""
    if wf then wf:close() end
    os.remove(tmpfile)

    --------------------------------------------------------------------
    -- Store results
    --------------------------------------------------------------------
    table.insert(nmap.registry.http_services, {
        ip = ip,
        port = port.number,
        scheme = scheme,
        scheme_upper = scheme_upper,
        url = url,
        screenshot = screenshot_file,
        whatweb = whatweb_output
    })

    return ("Captured screenshot + WhatWeb for %s"):format(url)
end

--------------------------------------------------------------------
-- POSTRULE
--------------------------------------------------------------------
postrule = function()
    local all = nmap.registry.http_services
    if not all or #all == 0 then
        return false
    end

    -- Write text list
    local list = io.open("http-services-list.txt", "w")
    for i, entry in ipairs(all) do
        list:write(entry.url)
        if i < #all then list:write("\n") end
    end
    list:close()

    -- Write HTML
    local html = io.open("http-services.html", "w")
    html:write("<html>\n<h1>HTTP Services</h1>\n")

    local grouped = {}
    for _, e in ipairs(all) do
        grouped[e.ip] = grouped[e.ip] or {}
        table.insert(grouped[e.ip], e)
    end

    for ip, entries in pairs(grouped) do
        html:write("<div>\n")
        html:write("<h1>" .. ip .. "</h1>\n")

        for _, e in ipairs(entries) do
            html:write(("<h2>%s</h2>\n"):format(e.url))
            html:write(escape_html(e.whatweb):gsub("\n", "<br>") .. "<br>\n")
            html:write(("<img src=\"%s\">\n<br><br>\n"):format(e.screenshot))
        end

        html:write("</div>\n")
    end

    html:write("</html>")
    html:close()

    return false
end
