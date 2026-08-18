# Network Reconnaissance Detection using Nmap, Wireshark, Tcpdump and Splunk

## Overview

This project focuses on detecting network reconnaissance activities such as port scanning, host discovery, and SYN scanning. The project uses Nmap to simulate reconnaissance activity, Tcpdump to capture network packets, Wireshark to analyze traffic, and Splunk to monitor, visualize, and generate alerts for suspicious network behavior.

The main goal is to identify reconnaissance activities at an early stage so that security teams can investigate suspicious behavior before it leads to further attacks.

## Objectives

* Detect network reconnaissance activities.
* Analyze packets generated during scanning.
* Identify suspicious SYN and ICMP traffic.
* Parse network traffic into useful security events.
* Send security data to Splunk.
* Create dashboards for network monitoring.
* Generate alerts for potential scanning activities.
* Understand the basic workflow of a Security Operations Center (SOC).

## Technologies Used

* **Nmap** – Network reconnaissance and scanning
* **Tcpdump** – Network packet capture
* **Wireshark** – Packet analysis
* **Python** – Detection and log processing
* **Splunk** – SIEM, visualization, and alerting
* **Linux/Kali Linux** – Testing environment

## Project Workflow

```text
Kali Linux
    │
    │ Nmap Scan
    ▼
Target Network
    │
    │ Network Traffic
    ▼
Tcpdump
    │
    │ PCAP
    ▼
Wireshark
    │
    │ Traffic Analysis
    ▼
Python Detection
    │
    │ Security Events
    ▼
Splunk
    │
    ├── Dashboard
    └── Alerts
```

## Detection Approach

The project looks for patterns that may indicate reconnaissance activity, including:

* Large numbers of SYN packets
* Multiple destination ports contacted by one source
* Repeated ICMP requests
* Sequential port scanning
* High-frequency connection attempts within a short period

When suspicious activity crosses the configured detection threshold, the system generates a potential reconnaissance alert.

Splunk Dashboard
================

Dashboard Name:
Network Reconnaissance Detection Dashboard

Purpose:
The dashboard provides visualization and monitoring of network reconnaissance
activities detected by the Python-based detection system.

Panels:
1. Total Attacks
2. Scan Type
3. Top Attacker
4. Severity Distribution
5. Timeline
6. Most Targeted Ports
7. Critical Alert

Data Source:
alerts.csv

Splunk Index:
network_recon

Detection Pipeline:
Nmap → tcpdump → PCAP → Python/Scapy → alerts.csv → Splunk → Dashboard

## Expected Result

The system helps identify possible network scanning activity and presents the detected events in Splunk. The dashboard can be used by a security analyst to investigate the source IP, destination IP, ports, scan type, and frequency of suspicious traffic.

## Disclaimer

This project is developed for educational and authorized security-testing purposes only. Scanning networks or systems without permission may be illegal or violate organizational policies.

## Author

**Vaishnavi Kurhade**

