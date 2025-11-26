#!/usr/bin/env python3
import ipaddress

input_file = "cidr-ranges.txt"
output_file = "ips.txt"

ips = []

with open(input_file, "r") as f:
    for line in f:
        cidr = line.strip()
        if not cidr:
            continue
        try:
            network = ipaddress.ip_network(cidr, strict=False)
            for ip in network.hosts():   # use .hosts() to skip network/broadcast for IPv4
                ips.append(str(ip))
        except ValueError as e:
            print(f"[!] Skipping invalid CIDR '{cidr}': {e}")

with open(output_file, "w") as f:
    for ip in ips:
        f.write(ip + "\n")

print(f"[+] Done. Wrote {len(ips)} IPs to {output_file}.")
