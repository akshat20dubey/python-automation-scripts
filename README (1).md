# 🐍 Python Automation Scripts

A collection of practical Python automation scripts built while learning Python scripting as part of my Platform Engineer journey.

---

## 📁 Scripts Overview

| Script | Description |
|--------|-------------|
| `server_health_check.py` | Checks if websites are UP or DOWN and logs results |
| `log_analyzer.py` | Scans log files and extracts ERROR and WARNING lines |
| `disk_usage_monitor.py` | Monitors disk usage and alerts if space is low |
| `file_organizer.py` | Automatically organizes files into folders by type |

---

## 🚀 How to Use

**1. Clone the repo**
```bash
git clone https://github.com/akshat20dubey/python-automation-scripts.git
cd python-automation-scripts
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run any script**
```bash
# Check if servers are up
python3 server_health_check.py

# Analyze a log file
python3 log_analyzer.py /var/log/syslog

# Monitor disk usage
python3 disk_usage_monitor.py

# Organize a messy folder
python3 file_organizer.py /path/to/folder
```

---

## 💡 Sample Output

**server_health_check.py**
```
=============================================
        SERVER HEALTH CHECKER
=============================================
Checked at: 2026-03-15 10:30:00

✅ UP   | https://google.com (HTTP 200)
✅ UP   | https://github.com (HTTP 200)
✅ UP   | https://aws.amazon.com (HTTP 200)

Log saved to: health_log.txt
=============================================
```

**disk_usage_monitor.py**
```
=============================================
        DISK USAGE MONITOR
=============================================
Drive   : /
Total   : 50.0 GB
Used    : 15.3 GB (30.6%)
Free    : 34.7 GB
✅ Disk usage is healthy.
=============================================
```

---

## 🛠️ Tech Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

---

## 📚 What I Learned

- Python scripting for real automation tasks
- Working with files, folders, and system commands in Python
- Using `requests` library to make HTTP calls
- Parsing and analyzing log files with Python
- Writing clean, reusable Python functions

---

## 🗺️ Part of My Learning Roadmap

This is **Project 2** of my Platform Engineer roadmap.

| Project | Status |
|---------|--------|
| 1. Linux Bash Scripts | ✅ Done |
| 2. Python Automation Scripts | ✅ Done |
| 3. Docker Flask App | 🔄 Coming Soon |
| 4. CI/CD Pipeline | 🔄 Coming Soon |
| 5. Terraform AWS Infra | 🔄 Coming Soon |
| 6. Kubernetes Monitoring | 🔄 Coming Soon |

---

## 🔗 Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/akshatautomates)
