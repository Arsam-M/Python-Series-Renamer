# Python-Series-Renamer
# 🎬 Series Renamer & Organizer

A powerful, interactive Python tool to automatically rename and organize your TV series episodes into proper season folders.

## ✨ Features
- **Interactive CLI:** Guides you through the process step-by-step.
- **Two Modes:** 
  1. Rename **ALL** files based on total season/episode counts.
  2. Rename a **SPECIFIC RANGE** (e.g., from S02E04 to S03E02).
- **Smart Sorting:** Automatically organizes files into `Season_XX` folders.
- **Deep Search:** Finds video files even inside nested subfolders.
- **Error Handling:** Skips existing files and handles invalid inputs gracefully without crashing.
- **Regex Powered:** Uses Regular Expressions to accurately detect and rename files in the specific range.

## 📂 Project Structure
- `main.py`: The entry point of the application and user menu.
- `utils.py`: Helper functions for input validation and file searching.
- `renamers.py`: The core logic for renaming and moving files.

## 🚀 How to Use
1. Clone this repository or download the files.
2. Make sure you have Python installed.
3. Run the main script:
   ```bash
   python main.py
