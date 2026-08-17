## Detect SYN Scan

Search:
tcp_flags="S" | stats count by src_ip

## Top Scanning IPs

Search:
index=network | stats count by src_ip

## Port Scanning

Search:
index=network | stats dc(dest_port) by src_ip
