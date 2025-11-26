<h1>How To Test CIDR Blocks</h1>

Sometimes, you're given a list of hosts in CIDR Notation, otherwise known as a CIDR Block. Below is an example that shows the CIDR Blocks that are in scope for Hilton's Public Bug Bounty Program on HackerOne as of 11/25/2025.
Make sure to check the updated list on HackerOne if you choose to test these targets.

<img width="265" height="567" alt="hilton-cidr-blocks" src="https://github.com/user-attachments/assets/de3424ab-3fdc-48fd-8350-adcbac375f8a" />

<h1>Expanding The Ranges Into Individual IP Addresses</h1>

It's easy enough to find a tool to expand these CIDR ranges into their individual IP addresses. If you want, you can use the expand_cidr.py tool I included in this repository. See example below

<img width="965" height="836" alt="expand_cidr-example" src="https://github.com/user-attachments/assets/b74f5758-df67-4fb2-b696-feb9b38a395e" />


<h1>Scanning For HTTP Services</h1>

<h2>Scan Entire CIDR Block For HTTP Services On Common Ports</h2>

nmap -sS -p 80,443,8000,8001,8008,8080,8081,8089,8090,8443,8888,9000,9443 -Pn -n --open 82.196.42.196/28 --randomize-hosts -oN syn-scan-cidr-block-for-http-services.txt

<h2>Scan List Of Hosts For HTTP Services On Common Ports</h2>

nmap -sS -p 80,443,8000,8001,8008,8080,8081,8089,8090,8443,8888,9000,9443 -Pn -n --open -iL hosts.txt --randomize-hosts -oN syn-scan-list-of-hosts-for-http-services.txt

<h1>TO BE CONTINUED</h1>
