# Network Reconnaissance Detection using Nmap, Wireshark, Tcpdump and Splunk

## 1. Project Overview

Network reconnaissance is one of the initial stages of a cyberattack. During this stage, an attacker collects information about a target network, such as active hosts, open ports, available services, and network structure.

This project focuses on detecting network reconnaissance activities by combining network scanning, packet capture, packet analysis, Python-based processing, and SIEM monitoring.

Nmap is used to generate controlled reconnaissance traffic. Tcpdump captures the network packets, while Wireshark is used for packet-level analysis. Python scripts process and identify suspicious network behavior, and Splunk is used to monitor the collected data through dashboards and detection queries.

---

## 2. Problem Statement

Attackers commonly perform network scanning before attempting exploitation. If reconnaissance activity is detected early, security teams can investigate the source and take preventive action.

The project addresses the problem of identifying suspicious network behavior such as:

* Host discovery
* Ping sweeps
* SYN scanning
* Port scanning
* Multiple connection attempts
* Unusual network activity

---

## 3. Objectives

The main objectives of the project are:

1. Simulate network reconnaissance using Nmap.
2. Capture network traffic using Tcpdump.
3. Analyze captured packets using Wireshark.
4. Process network data using Python.
5. Identify suspicious scanning patterns.
6. Send processed security data to Splunk.
7. Create a Splunk dashboard for monitoring.
8. Generate detection results for possible reconnaissance activity.

---

## 4. Technologies Used

| Technology   | Purpose                                        |
| ------------ | ---------------------------------------------- |
| Nmap         | Network scanning and reconnaissance simulation |
| Tcpdump      | Packet capture                                 |
| Wireshark    | Packet analysis                                |
| Python       | Data processing and detection                  |
| Splunk       | SIEM monitoring, visualization and detection   |
| Kali Linux   | Reconnaissance/testing environment             |
| Linux/Ubuntu | Target and monitoring environment              |

---

## 5. System Architecture

```text
                  ┌─────────────────┐
                  │   Kali Linux    │
                  │     Nmap        │
                  │  Reconnaissance │
                  └────────┬────────┘
                           │
                           │ Network Traffic
                           ▼
                  ┌─────────────────┐
                  │  Target System  │
                  │ Linux / Ubuntu  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    Tcpdump      │
                  │ Packet Capture   │
                  └────────┬────────┘
                           │
                           │ PCAP / Packet Data
                           ▼
                  ┌─────────────────┐
                  │    Wireshark    │
                  │ Packet Analysis │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │     Python      │
                  │ Parse / Detect  │
                  └────────┬────────┘
                           │
                           │ Security Events
                           ▼
                  ┌─────────────────┐
                  │     Splunk      │
                  │      SIEM       │
                  └────────┬────────┘
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
             Dashboard           Alerts
```

---

## 6. Project Workflow

The complete project follows these stages:

```text
Nmap Scan
    ↓
Network Traffic Generation
    ↓
Tcpdump Packet Capture
    ↓
Wireshark Packet Analysis
    ↓
Python Data Processing
    ↓
Reconnaissance Detection
    ↓
Splunk Data Ingestion
    ↓
SPL Queries
    ↓
Dashboard
    ↓
Detection / Alert
```

---

## 7. Reconnaissance Simulation

Nmap is used in the controlled laboratory environment to generate reconnaissance traffic.

Examples of activities include:

### Host Discovery

```bash
nmap -sn <target-network>
```

This identifies active hosts on the network.

### SYN Scan

```bash
nmap -sS <target-ip>
```

This generates TCP SYN traffic against multiple ports.

### Service Detection

```bash
nmap -sV <target-ip>
```

This attempts to identify services running on discovered ports.

The scans are performed only against systems within the authorized laboratory environment.

---

## 8. Packet Capture using Tcpdump

Tcpdump is used to capture network traffic generated during the reconnaissance activity.

Example:

```bash
sudo tcpdump -i eth0 -w nmap_scan.pcap
```

The captured traffic is stored as a PCAP file.

The PCAP file provides the raw network traffic required for further analysis.

---

## 9. Packet Analysis using Wireshark

The captured PCAP file is opened in Wireshark for detailed packet analysis.

Important traffic characteristics include:

* Source IP address
* Destination IP address
* Source port
* Destination port
* Protocol
* TCP flags
* Packet frequency
* Communication patterns

Example Wireshark filter for SYN traffic:

```text
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

This helps identify TCP connection attempts commonly associated with SYN scanning.

---

## 10. Python Processing

Python is used to process the captured or extracted network data.

The processing stage can:

1. Read packet/log data.
2. Extract relevant network fields.
3. Count network events.
4. Group traffic by source IP.
5. Count destination ports.
6. Identify suspicious activity.
7. Generate detection results.
8. Prepare structured data for Splunk.

Typical fields include:

```text
timestamp
src_ip
dest_ip
src_port
dest_port
protocol
tcp_flags
packet_size
scan_type
severity
alert
```

---

## 11. Reconnaissance Detection Logic

The project uses network behavior as an indicator of possible reconnaissance.

For example:

```text
High number of events
        +
Multiple destination ports
        +
Multiple destination hosts
        ↓
Possible Reconnaissance Activity
```

Example detection conditions used for the laboratory environment:

| Indicator                | Example Threshold |
| ------------------------ | ----------------: |
| Network Events           |               50+ |
| Unique Destination Ports |               10+ |
| Unique Destination IPs   |                5+ |

These thresholds are configurable and should be tuned according to normal network behavior.

---

## 12. Splunk Integration

Splunk is used as the centralized monitoring and analysis platform.

Processed network data is ingested into Splunk and searched using Splunk Processing Language (SPL).

The Splunk stage provides:

* Centralized event analysis
* Search and filtering
* Statistical analysis
* Visualization
* Reconnaissance detection
* Dashboard monitoring
* Alerting capability

The SPL queries used for the dashboard are available in:

```text
splunk/queries.md
```

---

## 13. Splunk Dashboard

The dashboard provides a centralized view of network reconnaissance activity.

The dashboard contains panels such as:

### Total Events

Displays the total number of network events.

### Top Source IPs

Shows the source addresses generating the highest amount of traffic.

### Top Destination IPs

Shows frequently targeted systems.

### Top Targeted Ports

Shows ports receiving the highest number of connection attempts.

### Network Activity Timeline

Displays network activity over time.

### Protocol Distribution

Shows the protocols present in the captured traffic.

### Scan Type Distribution

Shows detected reconnaissance categories.

### Detection Results

Displays source IPs showing suspicious scanning behavior.

---

## 14. Detection Example

A source generating traffic toward many different ports may indicate a port scan.

```text
Source IP: 192.168.x.x

Ports contacted:
22
23
25
53
80
110
135
139
443
445
...

Result:
Possible Port Scan
```

Similarly, a source contacting multiple hosts using ICMP may indicate a possible ping sweep.

---

## 15. Project Output

The project produces the following outputs:

* Network packet captures
* Wireshark traffic analysis
* Processed network data
* Detected reconnaissance events
* Splunk search results
* Splunk dashboard visualizations
* Potential security alerts

---

## 16. Project Directory

```text
Network-Reconnaissance-Detection/
│
├── README.md
│
├── src/
│   ├── detect_scan.py
│   ├── parser.py
│   └── alert.py
│
├── data/
│   └── sample_packets.csv
│
├── splunk/
│   └── queries.md
│
├── screenshots/
│   ├── nmap_scan.png
│   ├── tcpdump_capture.png
│   ├── wireshark_analysis.png
│   └── splunk_dashboard.png
│
├── docs/
│   └── PROJECT_DOCUMENTATION.md
│
├── requirements.txt
└── .gitignore
```

---

## 17. Testing

The project can be tested by generating controlled reconnaissance traffic and verifying whether each stage successfully processes the activity.

### Test 1 — Nmap

Perform an authorized scan against the laboratory target.

### Test 2 — Tcpdump

Verify that packets are captured.

### Test 3 — Wireshark

Open the PCAP and verify SYN, ICMP, and other relevant traffic.

### Test 4 — Python

Run the detection script and verify that suspicious activity is identified.

### Test 5 — Splunk

Verify that processed events appear in Splunk.

### Test 6 — Dashboard

Verify that the dashboard displays the expected statistics and detection results.

---

## 18. Limitations

The project is designed as a controlled laboratory implementation.

Some limitations include:

* Detection thresholds may require tuning.
* Legitimate high-volume traffic can produce false positives.
* Different scanning techniques may produce different traffic patterns.
* Detection accuracy depends on the quality of captured network data.
* The project does not automatically prevent an attack.

---

## 19. Future Enhancements

The project can be extended with:

* Real-time packet monitoring
* Suricata or Snort integration
* Automated incident response
* Email or messaging notifications
* Machine learning-based anomaly detection
* Behavioral fingerprinting
* Threat intelligence integration
* Automated blocking of confirmed malicious sources
* Advanced SOC dashboards

---

## 20. Security and Ethical Considerations

All scanning activities should be performed only against systems for which authorization has been obtained.

The project is intended for:

* Educational purposes
* Cybersecurity research
* Authorized penetration testing
* Security monitoring
* Laboratory experimentation

Unauthorized scanning of networks or systems may violate laws, organizational policies, or security regulations.

---

## 21. Conclusion

The Network Reconnaissance Detection project demonstrates a complete workflow for identifying early-stage network reconnaissance activity.

Nmap is used to generate controlled reconnaissance traffic, Tcpdump captures the traffic, Wireshark provides packet-level analysis, Python processes and detects suspicious patterns, and Splunk provides centralized monitoring and visualization.

The project provides practical experience in network security, packet analysis, detection engineering, SIEM concepts, and security monitoring.

The overall approach demonstrates how multiple open-source security tools can be combined to improve visibility and identify potential reconnaissance activity before it progresses into a more serious attack.

---

## 22. Author

**Vaishnavi Kurhade**

**Project:** Network Reconnaissance Detection using Nmap, Wireshark, Tcpdump and Splunk

