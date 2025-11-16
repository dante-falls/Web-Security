<h1>Discovering Live Hosts To Engage With</h1>

When it comes to penetration testing, knowledge is power. The more knowledge you have about a target, the more options you have available. We want to essentially find as wide of an attack surface, as possible. 
This makes it imperative that proper enumeration is carried out before any exploitation attempts are made. We can use nmap to discover live targets on a network.

<h1>List Scans - Lists Live Hosts Via Reverse DNS</h1>

Before doing any active scans on the target network, we can start by doing a so-called “list scan”. A list scan doesn’t send traffic to any hosts but rather attempts a reverse DNS lookup to determine if a hostname can be found for the target.

1. Singular Host: nmap -sL 45.33.32.156 -vv
2. List Of Hosts: nmap -iL hosts.txt -sL -vv

See Image Below

<img width="903" height="178" alt="nmap-list-scan-example" src="https://github.com/user-attachments/assets/92df3ca4-5443-491a-bcb2-007c26badde8" />

<h1>Ping Scans To Identify Live Hosts - Uses Port Scan</h1>

When scanning for hosts, at the most basic level, we can use Nmap on a single host without doing any port scanning. We use the -sn scan option (for “no port scan”) to tell Nmap to ping the given IP address/block for hosts. This ping scan is similar to the traditional ping command, but by default an Nmap ping scan will also attempt to connect to any TCP service running on ports 80 and 443 with ACK and SYN packets respectively. These ports are customizable with the -PS and -PA options if you know there’s a particular service running on another port that you would like to send traffic to.Because of this additional traffic that Nmap sends, the default ping scan behaves slightly differently to the traditional ping command: Targets on the internet will likely not respond to ICMP pings and would appear down, so Nmap’s -sn configuration uses additional techniques to determine if a host is up.

1. Singular Host: nmap -sn 45.33.32.156
2. List Of Hosts: nmap -iL hosts.txt -sn
3. Pure Ping Scan (dont run initial port connections on 80 and 443): nmap -PE -sn 45.33.32.156

See Image Below

<img width="893" height="309" alt="nmap-ping-scan-example" src="https://github.com/user-attachments/assets/4cf0e522-3169-4a0d-91c8-26ab2bfeac79" />

<h1>UDP Ping Scan</h1>

A UDP ping scan can be useful to circumvent firewalls between you and your target, as some firewalls will allow UDP traffic while blocking TCP. In this scan, Nmap sends a UDP packet to a high-numbered port that it expects to be closed. Depending on the response received, Nmap may be able to determine whether there is a host at the given address.

1. Singular Host: nmap -sn -PU -Pn --reason -vv 45.33.32.156
2. List Of Hosts: nmap -iL hosts.txt -sN -PU -Pn --reason -vv

See Images Below

<img width="893" height="309" alt="nmap-UDP-ping-scan-example" src="https://github.com/user-attachments/assets/1302d132-267d-4b16-9a48-156293cea3f3" />

<h3>Example When A UDP Ping Scan Finds An Open Host</h3>

<img width="744" height="406" alt="nmap-UDP-ping-scan-example-2" src="https://github.com/user-attachments/assets/19e4800b-cfd8-4c2b-a73d-26ab0f6edfab" />

<h1>ARP Ping Scans</h1>

If you are scanning within your local network, an ARP ping is a speedy and reliable way to discover hosts. Note that Nmap can scan IP blocks rather than specific addresses, so if you would like to quickly scan a local network subnet, you can specify the block to scan.

1. Scan List of Hosts: nmap -iL hosts.txt -sn -PR
2. Scan IP Block: nmap -sn -PR 10.0.1.1/24

<img width="743" height="304" alt="nmap-arp-scan-example" src="https://github.com/user-attachments/assets/7e886f6c-a65d-44d1-8720-d8eed2c58ed5" />


<h1>Nmap Scan Types</h1>

<h2>-sT - TCP Connect Scan</h2>

First the connecting terminal (our attacking machine, in this instance) sends a TCP request to the target server with the SYN flag set. The server then acknowledges this packet with a TCP response containing 
the SYN flag, as well as the ACK flag. Finally, our terminal completes the handshake by sending a TCP request with the ACK flag set. See Images Below.

<img width="1861" height="447" alt="nmap-tcp-connect-scan-visual" src="https://github.com/user-attachments/assets/02896cb4-3ce8-4048-866d-fb3cc59f1b32" />

<h2>-sS - SYN "Half Open/Stealth" Scan</h2>

Where TCP scans perform a full three-way handshake with the target, SYN scans sends back a RST TCP packet after receiving a SYN/ACK from the server. This prevents the server from repeatedly 
trying to make the request.

SYN scans are often not logged by applications listening on open ports, as standard practice is to log a connection once it's been fully established. Again, this plays into the idea of SYN scans 
being stealthy. Without having to bother about completing (and disconnecting from) a three-way handshake for every port, SYN scans are significantly faster than a standard TCP Connect scan.

1. <mark>Nmap SYN Scans Require Sudo Permissions on Linux because they require the ability to create Raw Packets</mark>
2. <mark>Unstable services are sometimes brought down by SYN scans, which could prove problematic if a client has provided a production environment for the test.</mark>



See Images Below

<img width="1860" height="609" alt="nmap-syn-scan-visual" src="https://github.com/user-attachments/assets/aca3c24e-5f15-42b1-98fa-6f75a547db06" />


<h2>-sU - UDP Scan</h2>

Unlike TCP, UDP connections are stateless. This means that, rather than initiating a connection with a back-and-forth "handshake", UDP connections rely on sending packets to a target port and essentially 
hoping that they make it. This makes UDP superb for connections which rely on speed over quality (e.g. video sharing), but the lack of acknowledgement makes UDP significantly more difficult (and much slower) 
to scan. The switch for an Nmap UDP scan is (-sU)

When a packet is sent to an open UDP port, there should be no response. When this happens, Nmap refers to the port as being open|filtered. In other words, it suspects that the port is open, but it could be 
firewalled. If it gets a UDP response (which is very unusual), then the port is marked as open. More commonly there is no response, in which case the request is sent a second time as a double-check. If 
there is still no response then the port is marked open|filtered and Nmap moves on.

When a packet is sent to a closed UDP port, the target should respond with an ICMP (ping) packet containing a message that the port is unreachable. This clearly identifies closed ports, which Nmap marks as 
such and moves on. Due to this difficulty in identifying whether a UDP port is actually open, UDP scans tend to be incredibly slow in comparison to the various TCP scans 
(in the region of 20 minutes to scan the first 1000 ports, with a good connection). For this reason it's usually good practice to run an Nmap scan with --top-ports <number> enabled. 
For example, scanning with  nmap -sU --top-ports 20 <target>. Will scan the top 20 most commonly used UDP ports, resulting in a much more acceptable scan time.

When scanning UDP ports, Nmap usually sends completely empty requests -- just raw UDP packets. That said, for ports which are usually occupied by well-known services, it will instead send a protocol-specific 
payload which is more likely to elicit a response from which a more accurate result can be drawn.

<h2>-sN - TCP Null Scan</h2>

NULL scans (-sN) are when the TCP request is sent with no flags set at all. As per the RFC, the target host should respond with a RST if the port is closed.

<img width="1744" height="583" alt="nmap-null-scan" src="https://github.com/user-attachments/assets/fe4dea33-9e0c-4fe7-a1f1-7f884a70b571" />


<h2>-sF - TCP FIN Scan</h2>

FIN scans (-sF) work in an almost identical fashion; however, instead of sending a completely empty packet, a request is sent with the FIN flag (usually used to gracefully close an active connection). Once again, Nmap expects a RST if the port is closed.

<img width="1744" height="579" alt="nmap-fin-scan" src="https://github.com/user-attachments/assets/683ba71e-b93c-422a-bfe9-3377a5ed9b20" />


<h2>-sX - TCP Xmas Scan</h2>

Xmas scans (-sX) send a malformed TCP packet and expects a RST response for closed ports. It's referred to as an xmas scan as the flags that it sets (PSH, URG and FIN) give it the appearance of a blinking christmas tree when viewed as a packet capture in Wireshark.

<img width="1693" height="502" alt="nmap-xmas-scan" src="https://github.com/user-attachments/assets/31005b92-194e-45d6-be79-0cf2653c64ee" />

<h1>-sn - Ping Sweep</h1>

On first connection to a target network in a black box assignment, our first objective is to obtain a "map" of the network structure -- or, in other words, we want to see which IP addresses contain active hosts, and which do not.

Nmap sends an ICMP packet to each possible IP address for the specified network. When it receives a response, it marks the IP address that responded as being alive.

The -sn switch tells Nmap not to scan any ports -- forcing it to rely primarily on ICMP echo packets (or ARP requests on a local network, if run with sudo or directly as the root user) to identify targets. In addition to the ICMP echo requests, the -sn switch will also cause nmap to send a TCP SYN packet to port 443 of the target, as well as a TCP ACK (or TCP SYN if not run as root) packet to port 80 of the target.

<h2>Examples</h2>

nmap -sn 192.168.0.1-254

OR

nmap -sn 192.168.0.0/24

<h1>-sA - TCP ACK Scan - Identify Ports That Are Filtered By Firewalls/IDS</h1>

-sA (TCP ACK Scan)

This scan is different than the others discussed so far in that it never determines open (or even open|filtered) ports. It is used to map out firewall rulesets, determining whether they are stateful or not and which ports are filtered.

The ACK scan probe packet has only the ACK flag set (unless you use --scanflags). When scanning unfiltered systems, open and closed ports will both return a RST packet. Nmap then labels them as unfiltered, meaning that they are reachable by the ACK packet, but whether they are open or closed is undetermined. Ports that don't respond, or send certain ICMP error messages back (type 3, code 0, 1, 2, 3, 9, 10, or 13), are labeled filtered.

See TCP ACK Scan Images Below

<img width="905" height="440" alt="nmap-tcp-ack-scan-command-line-results" src="https://github.com/user-attachments/assets/4c22c0d2-2f54-43e2-b4ad-c26027478cdb" />


<img width="1912" height="1091" alt="nmap-tcp-ack-scan-to-identify-filtered-ports" src="https://github.com/user-attachments/assets/1c70f7fa-ae85-46c7-b6e8-a7b2323a9fca" />


<h1>More Scans Can Be Found At</h1>
https://nmap.org/book/man-port-scanning-techniques.html

<h1>How To Set Custom Flags with nmap --scanflags</h1>

Truly advanced Nmap users need not limit themselves to the canned scanned types. The --scanflags option allows you to design your own scan by specifying arbitrary TCP flags.

Example(s):

1. nmap -sN --scanflags SYNCWRECE -Pn -p 21,53,80,135,3389 -vv TARGET_IP -- wireshark will show open ports if you run a -sN (Null) scan


The packets are sent with [SYN, CWE, ECE] flags. See image below to see one of the packets sent from this scan

<img width="950" height="417" alt="nmap-null-scanflags-syncwrece-packet-sent-from-client" src="https://github.com/user-attachments/assets/1f0a4540-883d-4a1a-bc33-0e036957f3de" />

The server responds with [SYN, ACK, ECE] for open ports in Wireshark. See image below.

<img width="1898" height="248" alt="nmap-null-scanflags-syncwrece-responses-from-server" src="https://github.com/user-attachments/assets/36fdbb1d-1c40-48e9-9135-e384dd12b59e" />


Sometimes nmap can identify open|filtered ports while using Null scans (-sN). If nmap recieves no response when running a Null scan, it considers the port to be open|filtered. See image below.

<img width="824" height="367" alt="nmap-null-scan-scanflags-syncwrece-open-ports-no-response" src="https://github.com/user-attachments/assets/9ddd5bb2-e470-4805-94f7-39f4cbb95602" />


2. nmap -sS --scanflags SYNCWRECE -Pn -p 21,53,80,135,3389 -vv TARGET_IP -- nmap will be able to identify open ports if you run a -sS (SYN) scan

When running an 'nmap -sS --scanflags SYNCWRECE ' scan, nmap will be able to identify the open ports. See image below.

<img width="857" height="681" alt="nmap-syn-scan-scanflags-syncwrece" src="https://github.com/user-attachments/assets/338528a3-9a17-46c1-a922-77cfb0460a8b" />


<h1>Add Custom Strings For Testing/Firewall Evasion Purposes</h1>

1. <mark>Append a custom payload to sent packets</mark>: --data-string 'customString6942031337'</mark> -- this may cause a lot of random protocols to pop up, but it still works

<h1>Firewall Evasion Techniques</h1>

1. -Pn - skip Host discovery. This tells Nmap to not ping the Host before scanning it. This can potentially take a very long time to complete the scan (if the host really is dead then Nmap will still be checking and double checking every specified port). It's worth noting that if you're already directly on the local network, Nmap can also use ARP requests to determine host activity.

2. -f - Used to fragment the packets (i.e. split them into smaller pieces) making it less likely that the packets will be detected by a firewall or IDS.

3. --mtu NUMBER - An alternative to -f, but providing more control over the size of the packets, --mtu accepts a maximum transmission unit size to use for the packets sent. This must be a multiple of 8.

4. --scan-delay TIME ms - used to add a delay between packets sent. This is very useful if the network is unstable, but also for evading any time-based firewall/IDS triggers which may be in place.

5. --badsum - this is used to generate in invalid checksum for packets. Any real TCP/IP stack would drop this packet, however, firewalls may potentially respond automatically, without bothering to check the checksum of the packet. As such, this switch can be used to determine the presence of a firewall/IDS.

6. -D RND:10 - This adds 10 random decoys. The target will see many IPs scanning, not just you.

7. -S IP_ADDRESS - spoof your IP address

8. Bypass Firewall To Discover Live Host With ACK Packets (Only scans Port 80 with ACK Packet, expects RST -- Does not resolve DNS): nmap -PA80 -sn -n 192.168.1.0/24

<h1>Working With NSE Scripts</h1>

The Nmap Scripting Engine (NSE) is an incredibly powerful addition to Nmap, extending its functionality quite considerably. NSE Scripts are written in the Lua programming language, and can be used to do a variety of things: from scanning for vulnerabilities, to automating exploits for them. The NSE is particularly useful for reconnaisance, however, it is well worth bearing in mind how extensive the script library is. See some of the script categories, below.

1. safe: Won't affect the target
2. intrusive: Not safe: likely to affect the target
3. vuln: Scan for vulnerabilities
4. exploit: Attempt to exploit a vulnerability
5. auth: Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
6. brute: Attempt to bruteforce credentials for running services
7. discovery: Attempt to query running services for further information about the network (e.g. query an SNMP server).

Example Useage:

<mark>nmap -Pn -p 21 --script=ftp-anon --data-string 'defaultz6942031337ardvark' --min-rate 100 -vv 10.201.92.218</mark>

The above Nmap NSE script will attempt FTP Anonymous login on the Target Host.

<h3>How To Run Multiple NSE Scripts</h3>

--script=smb-enum-users,smb-enum-shares

<h3>Learn About An NSE Script</h3>

nmap --script-help <script-name>

<h3>Find NSE Scripts</h3>

grep "ftp" /usr/share/nmap/scripts/script.db

ls -l /usr/share/nmap/scripts/*ftp*

<h2>Installing New Scripts</h2>

We mentioned previously that the Nmap website contains a list of scripts, so, what happens if one of these is missing in the scripts directory locally? A standard sudo apt update && sudo apt install nmap should fix this; however, it's also possible to install the scripts manually by downloading the script from Nmap (sudo wget -O /usr/share/nmap/scripts/<script-name>.nse https://svn.nmap.org/nmap/scripts/<script-name>.nse). This must then be followed up with nmap --script-updatedb, which updates the script.db file to contain the newly downloaded script.

It's worth noting that you would require the same "updatedb" command if you were to make your own NSE script and add it into Nmap -- a more than manageable task with some basic knowledge of Lua!

<h1>Great Resources</h1>

<h3>Firewall/IDS Evasion</h3>

1. https://nmap.org/book/man-bypass-firewalls-ids.html
2. https://medium.com/@appsecvenue/mastering-nmap-part-2-advanced-scans-firewall-evasion-for-bug-bounty-hunters-e005dcaf21a7
3. https://www.device42.com/blog/2023/03/29/nmap-host-discovery-the-ultimate-guide/

<h3>NSE Scripts</h3>

1. https://nmap.org/nsedoc/

<h3>Places To Learn And Practice Nmap</h3>

1. https://nmap.org/book/
2. https://tryhackme.com/room/furthernmap
3. http://scanme.nmap.org/
4. https://www.device42.com/blog/2023/03/29/nmap-host-discovery-the-ultimate-guide/
