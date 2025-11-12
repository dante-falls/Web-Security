<h1>How To Discover HTTP Services Living On Non-Standard Ports With Nmap</h1>

Sometimes, HTTP/HTTPS services live on non-standard ports (any port other then the default ports of 80 and 443). We can use an Nmap service scan to identify these ports. See examples below.

<h2>Scan 154 Non-Standard HTTP Ports To Discover HTTP Services</h2>

I looked through IANA and a few other resources to check for official Non-Standard HTTP Ports. Some of them are not scanned by Nmap by default, so I created a list that you can use to scan. Below is the link to the list:

https://github.com/dante-falls/Web-Security/blob/main/Nmap_Stuff/Nonstandard-HTTP-Scan/list-nonstandard-http-ports-comma-delimeter.txt


<h3>Scan Syntax</h3>

1. Single Host: nmap -sV -Pn -p $(cat /path/to/port-list.txt) 10.201.106.66
2. List Of Hosts: nmap -iL hosts.txt -sV -Pn -p $(cat /path/to/port-list.txt)


<mark>See Example Image Below</mark>

<img width="1787" height="296" alt="non-standard-http-port-scan-syntax" src="https://github.com/user-attachments/assets/771a993a-5045-41bb-b63f-7c45f43afa70" />



<h2>Scan All Ports To Discover HTTP Services On Non-Standard Ports</h2>

If you want to scan all 65,535 ports to try and find HTTP services on non-standad ports, you can use -p-

<h3>Scan Syntax</h3>

1. Single Host: nmap -sV -Pn -p- 10.201.106.66
2. List Of Hosts: nmap -iL hosts.txt -sV -Pn -p-


<h1>Screenshotting Each Identified HTTP Service</h1>

I also use an Nmap NSE script that takes a screenshot of the webpage when nmap discovers an HTTP/HTTPS service. The NSE script can be found in the link below:

https://github.com/dante-falls/Web-Security/tree/main/Nmap_Stuff/Nmap_NSE_Scripts/HTTP-Service-Screenshot

<h3>Scan Syntax With Screenshots From http-service-screenshot.nse</h3>

sudo nmap -sV --script http-service-screenshot -Pn -p $(cat /path/to/port-list.txt) -vv 10.201.106.66

See Example Images Below

<img width="1902" height="590" alt="non-standard-http-port-scan-with-screenshot-nse" src="https://github.com/user-attachments/assets/23edf6a0-6940-43dd-b7ba-308ff5f82d89" />

<img width="1909" height="760" alt="http-service-screenshot-nse-image-example" src="https://github.com/user-attachments/assets/aa59a770-09ba-4186-83b1-a571a6c24a20" />

<img width="1899" height="769" alt="mr-robot-http-service-screenshot" src="https://github.com/user-attachments/assets/aac81711-a92b-44de-a433-ffa979573c48" />







