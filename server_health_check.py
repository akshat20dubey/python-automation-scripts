#!/usr/bin/env python3
# =============================================
# Script: server_health_check.py
# Description: Checks if a website is UP or DOWN
# Author: Akshat Dubey
# Usage: python3 server_health_check.py
# =============================================

import requests
from datetime import datetime

# List of URLs to monitor
URLS = [
    "https://google.com",
    "https://github.com",
    "https://aws.amazon.com",
]

LOG_FILE = "health_log.txt"

def check_server(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "UP", response.status_code
        else:
            return "DOWN", response.status_code
    except requests.exceptions.RequestException:
        return "DOWN", "No Response"

def main():
    print("=" * 45)
    print("        SERVER HEALTH CHECKER")
    print("=" * 45)
    print(f"Checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    with open(LOG_FILE, "a") as log:
        for url in URLS:
            status, code = check_server(url)
            icon = "✅" if status == "UP" else "❌"
            result = f"{icon} {status} | {url} (HTTP {code})"
            print(result)
            log.write(f"{datetime.now()} | {status} | {url} | HTTP {code}\n")

    print()
    print(f"Log saved to: {LOG_FILE}")
    print("=" * 45)

if __name__ == "__main__":
    main()
