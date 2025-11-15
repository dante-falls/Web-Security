<h1>http-service-screenshot Nmap NSE Script</h1>

<mark>When Nmap discovers an HTTP or HTTPS service during a service scan (-sV), http-service-screenshot.nse will:</mark>

1. Attempt to take a screenshot of the webpage with cutycapt.
2. Run whatweb on the web service to get basic server information
3. Organizes all information into an HTML file called 'http-services.html' for easier viewing of data
4. Write a txt file called 'http-services-list.txt' that lists all the URLs found

<h3>Requirements</h3>

1. 'cutycapt' for screenshots
2. 'whatweb' for web service information

<h2>Steps To Add Script To Kali Linux</h2>

link to http-service-screenshot.nse: https://github.com/dante-falls/Web-Security/blob/main/Nmap_Stuff/Nmap_NSE_Scripts/HTTP-Service-Screenshot/http-service-screenshot.nse

1. sudo nano /usr/share/nmap/scripts/http-service-screenshot.nse
2. nmap --script-updatedb
3. sudo updatedb

<h1>How To Use http-service-screenshot.nse</h1>

<h3>Syntax</h3>

1. <mark>Service Scan Top 1000 Ports</mark>: sudo nmap -sV --script http-service-screenshot -Pn TARGET_IP
2. <mark>Service Scan Specific Ports</mark>: sudo nmap -sV --script http-service-screenshot -p 22,80,443,8081,8082 -Pn TARGET_IP

<img width="1390" height="747" alt="http-service-screenshot-commandline-syntax" src="https://github.com/user-attachments/assets/775f5a82-fb4e-4cec-a4df-a924046323e0" />


<h2>Verify Files Were Created with 'ls'</h2>

<img width="1479" height="110" alt="http-service-screenshot-view-script-images-commandline" src="https://github.com/user-attachments/assets/24c8563f-1abd-4220-9cb4-262bfeac3ca4" />


<h2>View The http-services.html File That Organizes All Data Into A Readable Format</h2>

<img width="1417" height="807" alt="http-services-html-file-1" src="https://github.com/user-attachments/assets/23045a8d-3caf-458f-bf41-53afe7b3253e" />
<img width="981" height="746" alt="http-services-html-file-2" src="https://github.com/user-attachments/assets/bf2b75da-b3be-4c2a-bcae-347bf2bc76c0" />



<h2>View The http-services-list.txt File That Organizes All URLs Into One File</h2>

<img width="448" height="148" alt="http-services-list-txt-file" src="https://github.com/user-attachments/assets/7559df6d-769d-47db-aed2-00a3379c112c" />


