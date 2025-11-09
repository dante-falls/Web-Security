description = [[
Detects HTTP services running on any port, captures a screenshot using Cutycapt.

Usage:
  nmap -sV --script http-service-screenshot <target>

Requirements:
  - Cutycapt must be installed and in your system PATH
  - Run with sufficient privileges to execute system() calls
]]

author = "Cybernerddante AND ChatGPT"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"discovery", "safe"}

local http = require "http"
local stdnse = require "stdnse"
local shortport = require "shortport"

portrule = function(host, port)
  return shortport.port_or_service({80, 443}, {"http", "https"})(host, port)
      or (port.version and port.version.service and port.version.service:match("http"))
      or (port.version and port.version.name and port.version.name:match("http"))
      or (port.version and port.version.product and port.version.product:match("http"))
end

local screenshots = {}

action = function(host, port)
  local ip = host.ip
  local proto = (port.tls or port.service == "https" or port.number == 443) and "https" or "http"
  local url = ("%s://%s:%d/"):format(proto, ip, port.number)

  local filename = ("HTTP-%s-%d.jpg"):format(ip, port.number)
  local output_path = stdnse.tohex(ip .. port.number) .. ".jpg"  -- optional safety fallback
  local cmd = ("cutycapt --url='%s' --out='%s' --min-width=1024 --min-height=768"):format(url, filename)

  stdnse.print_debug(1, "Executing: %s", cmd)
  os.execute(cmd)

  screenshots[#screenshots + 1] = {
    ip = ip,
    port = port.number,
    filename = filename
  }

  return string.format("Screenshot saved: %s", filename)
end
