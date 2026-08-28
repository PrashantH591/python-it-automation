import os
import platform
import shutil
import socket
import sys
from datetime import datetime


def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.platform(),
        "python_version": sys.version.split()[0],
        "current_user": os.getenv("USER") or os.getenv("USERNAME") or "Unknown",
    }


def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)

    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)
    usage_percent = (used / total) * 100

    return {
        "total_gb": round(total_gb, 2),
        "used_gb": round(used_gb, 2),
        "free_gb": round(free_gb, 2),
        "usage_percent": round(usage_percent, 2),
    }


def check_network(host="google.com", port=443, timeout=5):
    try:
        socket.create_connection((host, port), timeout=timeout)
        return "PASS"
    except OSError:
        return "FAIL"


def generate_report():
    system = get_system_info()
    disk = check_disk_usage()
    network = check_network()

    report = f"""
========================================
       IT SYSTEM HEALTH REPORT
========================================

Generated:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

SYSTEM INFORMATION
------------------
Hostname: {system["hostname"]}
Operating System: {system["operating_system"]}
Python Version: {system["python_version"]}
Current User: {system["current_user"]}

DISK USAGE
----------
Total: {disk["total_gb"]} GB
Used: {disk["used_gb"]} GB
Free: {disk["free_gb"]} GB
Usage: {disk["usage_percent"]}%

NETWORK CONNECTIVITY
--------------------
HTTPS connectivity to google.com: {network}

========================================
"""

    return report


if __name__ == "__main__":
    print(generate_report())
