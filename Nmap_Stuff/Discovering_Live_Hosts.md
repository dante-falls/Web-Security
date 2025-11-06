<h1>Discovering Live Hosts To Engage With</h1>

When it comes to penetration testing, knowledge is power. The more knowledge you have about a target, the more options you have available. We want to essentially find as wide of an attack surface, as possible. 
This makes it imperative that proper enumeration is carried out before any exploitation attempts are made. We can use nmap to discover live targets on a network.

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

<h2>-sF - TCP FIN Scan</h2>

<h2>-sX - TCP Xmas Scan</h2>
