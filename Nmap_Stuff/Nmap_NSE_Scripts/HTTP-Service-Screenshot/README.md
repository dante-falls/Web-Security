<h1>http-service-screenshot Nmap NSE Script</h1>

<h3>IMPORTANT</h3>

1. Requires 'chromium' - I use chromium because it can bypass certificate errors and still open the web page.
2. <mark>To Be Safe, chromium should be ran as a non-priviledged user on the system because this script uses '--no-sandbox' incase it needs to be ran with sudo. Make sure to change the <NON_PRIVILEDGED_USER> string on line 37 of https://github.com/dante-falls/Web-Security/blob/main/Nmap_Stuff/Nmap_NSE_Scripts/HTTP-Service-Screenshot/http-service-screenshot.nse to match your own unpriviledged system user</mark>
3. <mark>ERRORS:</mark> This script causes dbus errors because chromium complains about an invalid dbus address. I will eventually fix this BUT for now this is harmless and the script still executes successfully.

When Nmap discovers an HTTP service during a service scan (-sV), the http-service-screenshot Nmap NSE Script will attempt to take a screenshot of the web page. The script uses 'chromium' to take a screenshot of the webpage.

<h2>Steps To Add Script To Kali Linux</h2>

link to http-service-screenshot.nse: https://github.com/dante-falls/Web-Security/blob/main/Nmap_Stuff/Nmap_NSE_Scripts/HTTP-Service-Screenshot/http-service-screenshot.nse

1. sudo nano /usr/share/nmap/scripts/http-service-screenshot.nse
2. nmap --script-updatedb
3. sudo updatedb

<h2>How To Use http-service-screenshot.nse</h2>

<h3>Syntax</h3>

sudo nmap -sV --script http-service-screenshot -Pn -vv TARGET_IP

<img width="1053" height="447" alt="http-service-screenshot-commandline-syntax" src="https://github.com/user-attachments/assets/0150e85d-3be6-43ed-933d-3d9a0bc274af" />

<h3>Nmap Report Output</h3>

<img width="1203" height="653" alt="http-service-screenshot-nmap-scan-report" src="https://github.com/user-attachments/assets/c6a44ab6-b431-4bb8-a865-5b9a4cdf5906" />

<h3>Verify The Images Were Created with 'ls'</h3>

<img width="678" height="67" alt="http-service-screenshot-view-script-images-commandline" src="https://github.com/user-attachments/assets/6eacb4d4-14e5-4b03-bb1e-725f67fdcc1f" />

<h3>View The Images One By One (sorry lol)</h3>

<img width="1916" height="690" alt="http-service-screenshot-images" src="https://github.com/user-attachments/assets/89249f6c-2ece-4711-b748-09febccf9ed0" />

