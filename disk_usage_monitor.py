#!/usr/bin/env python3
# =============================================
# Script: disk_usage_monitor.py
# Description: Monitors disk usage and alerts if low
# Author: Akshat Dubey
# Usage: python3 disk_usage_monitor.py
# =============================================

import shutil
from datetime import datetime

# Alert threshold (percentage)
ALERT_THRESHOLD = 80

def get_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)
    percent = (used / total) * 100
    return total_gb, used_gb, free_gb, percent

def main():
    print("=" * 45)
    print("        DISK USAGE MONITOR")
    print("=" * 45)
    print(f"Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    paths = ["/"] if __import__("os").name != "nt" else ["C:/", "D:/"]

    for path in paths:
        try:
            total, used, free, percent = get_disk_usage(path)
            print(f"Drive   : {path}")
            print(f"Total   : {total:.1f} GB")
            print(f"Used    : {used:.1f} GB ({percent:.1f}%)")
            print(f"Free    : {free:.1f} GB")

            if percent >= ALERT_THRESHOLD:
                print(f"⚠️  ALERT: Disk usage is above {ALERT_THRESHOLD}%!")
            else:
                print(f"✅ Disk usage is healthy.")
            print()
        except Exception:
            print(f"⚠️  Could not check: {path}")

    print("=" * 45)

if __name__ == "__main__":
    main()
