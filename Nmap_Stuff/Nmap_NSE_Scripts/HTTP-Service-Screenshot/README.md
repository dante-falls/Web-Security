<h1>http-service-screenshot Nmap NSE Script</h1>

<mark>Requires 'cutycapt'</mark>

When Nmap discovers an HTTP service during a service scan (-sV), the http-service-screenshot Nmap NSE Script will attempt to take a screenshot of the web page. The script uses 'cutycapt' to take a screenshot of the webpage. My Kali
Linux had 'cutycapt' installed automatically.

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

