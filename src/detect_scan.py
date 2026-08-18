from scapy.all import *
from collections import defaultdict
from datetime import datetime
import csv
import subprocess

packets = rdpcap("scan.pcap")

syn = defaultdict(set)
udp = defaultdict(set)
fin = defaultdict(set)
null = defaultdict(set)
xmas = defaultdict(set)

for packet in packets:

    if IP in packet:

        src = packet[IP].src

        if TCP in packet:

            flags = packet[TCP].flags
            port = packet[TCP].dport

            # SYN
            if flags == 0x02:
                syn[src].add(port)

            # FIN
            elif flags == 0x01:
                fin[src].add(port)

            # NULL
            elif flags == 0x00:
                null[src].add(port)

            # XMAS
            elif flags == 0x29:
                xmas[src].add(port)

        elif UDP in packet:

            udp[src].add(packet[UDP].dport)


def severity(count):

    if count >= 100:
        return "CRITICAL"

    elif count >= 50:
        return "HIGH"

    elif count >= 20:
        return "MEDIUM"

    else:
        return "LOW"


alerts = []

for ip, ports in syn.items():

    alerts.append([
        datetime.now(),
        ip,
        "SYN_Scan",
        len(ports),
        severity(len(ports))
    ])

for ip, ports in udp.items():

    alerts.append([
        datetime.now(),
        ip,
        "UDP_Scan",
        len(ports),
        severity(len(ports))
    ])

for ip, ports in fin.items():

    alerts.append([
        datetime.now(),
        ip,
        "FIN_Scan",
        len(ports),
        severity(len(ports))
    ])

for ip, ports in null.items():

    alerts.append([
        datetime.now(),
        ip,
        "NULL_Scan",
        len(ports),
        severity(len(ports))
    ])

for ip, ports in xmas.items():

    alerts.append([
        datetime.now(),
        ip,
        "XMAS_Scan",
        len(ports),
        severity(len(ports))
    ])


with open("alerts.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "timestamp",
        "source_ip",
        "scan_type",
        "count",
        "severity"
    ])

    writer.writerows(alerts)

print("alerts.csv generated successfully.")

# Run alert script automatically
subprocess.run(["python3", "alert.py"])
