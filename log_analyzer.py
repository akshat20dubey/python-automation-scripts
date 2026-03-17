#!/usr/bin/env python3
# =============================================
# Script: log_analyzer.py
# Description: Scans log files for ERRORS and WARNINGS
# Author: Akshat Dubey
# Usage: python3 log_analyzer.py /path/to/file.log
# =============================================

import sys
from datetime import datetime
from collections import Counter

def analyze_log(filepath):
    errors = []
    warnings = []

    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        sys.exit(1)

    for line in lines:
        if "error" in line.lower():
            errors.append(line.strip())
        elif "warning" in line.lower():
            warnings.append(line.strip())

    print("=" * 45)
    print("          LOG FILE ANALYZER")
    print("=" * 45)
    print(f"File     : {filepath}")
    print(f"Scanned  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Lines : {len(lines)}")
    print(f"Errors      : {len(errors)}")
    print(f"Warnings    : {len(warnings)}")
    print()

    if errors:
        print("=" * 45)
        print("         ERROR LINES:")
        print("=" * 45)
        for e in errors[:10]:
            print(f"  🔴 {e}")

    if warnings:
        print()
        print("=" * 45)
        print("         WARNING LINES:")
        print("=" * 45)
        for w in warnings[:10]:
            print(f"  🟡 {w}")

    print()
    print("✅ Analysis complete!")
    print("=" * 45)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 log_analyzer.py /path/to/logfile.log")
        sys.exit(1)
    analyze_log(sys.argv[1])
