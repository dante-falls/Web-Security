<h1>http-service-screenshot Nmap NSE Script</h1>

<h2>IMPORTANT Fixes</h2>

1. <mark>Sanitization of whatweb output into http-services.html File:</mark> versions of http-service-screenshot.nse downloaded before 11/16/2025 at 11:05 AM PST were POTENTIALLY vulnerable to XSS because of the unsanitized output from whatweb written directly into the http-services.html file. This has been fixed and everything is working as expected.
2. <mark>HTTPS Services Identification Issue Fixed:</mark> As of 11/17/2025 5:43 PM PST, the http-service-screenshot.nse script can now correctly identify HTTPS services that are on ports other then 443. These HTTPS services are now identified with an SSL Probe (check line 61 of the http-service-screenshot.nse script).

<h2>Description</h2>

<mark>When Nmap discovers an HTTP or HTTPS service during a service scan (-sV), http-service-screenshot.nse will:</mark>

1. Attempt to take a screenshot of the webpage with cutycapt.
2. Run whatweb on the web service to get basic server information
3. Organizes all information into an HTML file called 'http-services.html' for easier viewing of data
4. Write a txt file called 'http-services-list.txt' that lists all the URLs found

<h2>Requirements</h2>

1. 'cutycapt' for screenshots
2. 'whatweb' for web service information

<h2>Configure How cutycapt Takes The Screenshot</h2>

You can add flags to the cutycapt command on line 79 of the http-service-screenshot.nse script in order to change how cutycapt takes a screenshot of the webpage. See all flags by running 'cutycapt --help' on the command line. You can add the following functionality, and more.

1. Minimum Width Of Image: --min-width=1366
2. Minimum Height Of Image: --min-height=768
3. Delay (milliseconds) Before Screenshot Is Taken: --delay=3000
4. Make The Background White: --user-style-string='html,body{background: white !important;}'
5. Ignore SSL/TLS Certificate Issues (THIS IS RAN BY DEFAULT): --insecure


<h2>Steps To Add Script To Kali Linux</h2>

link to http-service-screenshot.nse: https://github.com/dante-falls/Web-Security/blob/main/Nmap_Stuff/Nmap_NSE_Scripts/HTTP-Service-Screenshot/http-service-screenshot.nse

1. sudo nano /usr/share/nmap/scripts/http-service-screenshot.nse
2. sudo nmap --script-updatedb
3. sudo updatedb

<h1>How To Use http-service-screenshot.nse</h1>

<h3>Syntax</h3>

1. <mark>Service Scan Top 1000 Ports</mark>: sudo nmap -sV --script http-service-screenshot -Pn --open TARGET_IP
2. <mark>Service Scan Specific Ports</mark>: sudo nmap -sV --script http-service-screenshot -p 22,80,443,8081,8082 -Pn --open TARGET_IP

<img width="1223" height="703" alt="http-service-screenshot-commandline-syntax" src="https://github.com/user-attachments/assets/8dc90345-355c-4677-a5b0-766154d773d2" />

<h2>Verify Files Were Created with 'ls'</h2>

<img width="1334" height="99" alt="http-service-screenshot-view-script-images-commandline" src="https://github.com/user-attachments/assets/0bbb8426-b046-482c-81f2-a991cc5e4050" />



<h2>View The http-services.html File That Organizes All Data Into A Readable Format</h2>

<mark>These are images of the HTML file so they are truncated in some spots. The HTML file will look normal when you open on your own system.</mark>

<img width="1212" height="810" alt="http-services-html-file-1" src="https://github.com/user-attachments/assets/d79b8628-0074-42f3-8c92-17f39e7126fb" />
<img width="1316" height="802" alt="http-services-html-file-2" src="https://github.com/user-attachments/assets/28e6cd5d-7005-4303-b8de-ee5e1d12accb" />


<h2>View The http-services-list.txt File That Organizes All URLs Into One File</h2>

<img width="505" height="153" alt="http-services-list-txt-file" src="https://github.com/user-attachments/assets/b5198b65-88af-4617-b29b-8ad222a917bf" />



