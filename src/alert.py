import csv

print("\n======= ALERTS =======\n")

with open("alerts.csv", "r") as f:

    reader = csv.DictReader(f)

    for row in reader:

        print("-" * 40)

        print("Timestamp :", row["timestamp"])
        print("Source IP :", row["source_ip"])
        print("Scan Type :", row["scan_type"])
        print("Count     :", row["count"])
        print("Severity  :", row["severity"])

        print("-" * 40)
