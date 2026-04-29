import re

log_file = "logs.txt"

failed_logins = 0
ip_counts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_logins += 1
            ip = re.search(r"\d+\.\d+\.\d+\.\d+", line)
            if ip:
                ip = ip.group()
                ip_counts[ip] = ip_counts.get(ip, 0) + 1

print(f"Total Failed Logins: {failed_logins}")

for ip, count in ip_counts.items():
    print(f"{ip} → {count} attempts")
