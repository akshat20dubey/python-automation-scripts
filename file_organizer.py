#!/usr/bin/env python3
# =============================================
# Script: file_organizer.py
# Description: Automatically organizes files into folders by type
# Author: Akshat Dubey
# Usage: python3 file_organizer.py /path/to/folder
# =============================================

import os
import shutil
import sys
from datetime import datetime

# File type categories
CATEGORIES = {
    "Images"     : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos"     : [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents"  : [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Scripts"    : [".py", ".sh", ".js", ".ts", ".rb"],
    "Archives"   : [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Others"     : []
}

def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        sys.exit(1)

    print("=" * 45)
    print("          FILE ORGANIZER")
    print("=" * 45)
    print(f"Folder  : {folder_path}")
    print(f"Started : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    moved = 0
    skipped = 0

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(filepath):
            skipped += 1
            continue

        ext = os.path.splitext(filename)[1]
        category = get_category(ext)

        dest_folder = os.path.join(folder_path, category)
        os.makedirs(dest_folder, exist_ok=True)

        dest_path = os.path.join(dest_folder, filename)
        shutil.move(filepath, dest_path)
        print(f"✅ Moved: {filename} → {category}/")
        moved += 1

    print()
    print(f"Total Moved   : {moved}")
    print(f"Total Skipped : {skipped}")
    print("✅ Folder organized successfully!")
    print("=" * 45)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 file_organizer.py /path/to/folder")
        sys.exit(1)
    organize_folder(sys.argv[1])
