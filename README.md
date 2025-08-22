# Failsafe Log Extractor (FLEX)


```
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣴⣶⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣼⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⢰⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠛⠛⠛⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢰⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣋⣭⣵⣶⣶⣿⣿⠀⠀⠀⣀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⡿⢟⣃⣋⣭⣭⣭⣭⣙⣛⣛⠻⠿⣿⡿⠟⣋⣥⣶⣿⣿⣿⣿⣿⣿⣿⣿⠃⣀⣴⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠸⣫⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣩⣴⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⣛⣭⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ___________.____     _______________  ___
⣿⣿⣿⣿⣿⣿⡿⢠⣿⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⡄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⢛⣛⡋  \_   _____/|    |    \_   _____/\   \/  /
⣿⣿⣿⣿⣿⣿⠇⣾⠁⠀⠿⠂⢹⣿⣿⣿⣿⣿⣿⣿⡟⠁⣶⡀⠙⣿⣿⣿⡇⢿⣿⣿⡿⠟⣛⣫⣭⣴⣶⣶⣿⣿⣿⣿⡿⢡   |    __)  |    |     |    __)_  \     / 
⣿⣿⣿⣿⣿⡿⢰⣿⣆⣀⣀⣠⣾⣿⣏⣙⣿⣿⣿⣿⣇⠀⠀⠀⢀⣿⣿⣿⡧⢘⣩⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣿   |     \   |    |___  |        \ /     \ 
⣿⣿⣿⣿⣿⠃⣙⠻⣿⣿⡟⠿⠿⠋⣠⣉⠻⢿⣿⣿⢿⣿⣶⣾⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣾⣿   \___  /   |_______ \/_______  //___/\  \
⣿⣿⣿⣿⡏⢸⣿⣷⢸⣿⣿⣇⢁⣾⣿⣿⣿⣶⣶⢰⣿⣿⣿⠟⣩⣶⣬⡛⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣼⣿⣿       \/            \/        \/       \_/
⣿⣿⣿⣿⣿⡘⠿⢃⣼⣿⣿⣿⡘⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⠘⣿⣿⣿⠇⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣷⡘⢿⣿⣿⣿⣿⣧⠹⣿⣿⣿⡟⣰⣿⣿⣿⣿⣷⣌⣛⣩⣼⢠⣿⣿⣿⡁⣤⣤⣤⣤⣤⣤⣤⣤⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⠹⣿⣿⣿⣿⣷⣙⠿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣦⡙⣿⣿⣧⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⢸⣦⣙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣋⣴⣇⢸⣷⡌⢿⣿⡆⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⢃⠿⣿⣿⣷⣦⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⠈⣋⣥⣾⣿⠿⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢋⣾⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠹⢋⣥⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠃⡈⢹⣿⠟⢋⣘⠻⠸⣿⣿⣿⣿⣿⣿⣿⡍⣿⢠⣿⣿⣿⣿⣿⣿⣿⡿⢸⠟⠂⡙⠻⡿⠋⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢀⠃⠂⢡⣾⣿⣿⣿⡆⢿⣿⣿⣿⣿⣿⣿⣷⠈⣼⣿⣿⣿⣿⣿⣿⣿⠃⣶⣾⣿⣿⡟⡠⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠈⣶⣾⡌⣿⣿⣿⣿⣷⠘⣿⣿⣿⣿⣿⣿⣿⠄⣿⣿⣿⣿⣿⣿⣿⠏⣼⣿⣿⣿⣿⣰⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣆⢹⣿⣷⢸⣿⣿⣿⣿⣧⠹⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⠇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡌⢿⣿⣦⣿⣿⣿⣿⣿⣧⠹⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⠏⣼⣿⣿⣿⣿⡿⢻⣿⡟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡌⢿⠏⠿⠿⠿⣿⣿⣿⣧⠙⠿⣿⣿⣿⢸⣿⣿⣿⡿⢋⣼⣿⣿⣿⣿⣿⡇⢸⡟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣶⣶⣿⣿⣷⣶⣶⣶⣦⣄⣀⣁⣁⣄⣬⡙⣙⢉⢉⣀⣤⣤⣬⣭⣭⣥⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
```

## Overview
Failsafe Log Extractor (FLEX) is a Python-based tool designed to automate the process of extracting, segregating, and updating test logs from HTML reports and structured data files. It simplifies workflows by leveraging automation libraries and user-friendly interfaces.

---

## Features
- **HTML Report Parsing**: Extracts test case links from HTML reports based on user-defined keywords.
- **Log Segregation**: Automatically categorizes logs into PASSED, FAILED, and OTHER test cases.
- **Log Downloading**: Downloads logs from provided URLs with robust error handling and progress tracking.
- **Log Organization**: Moves downloaded logs to user-specified directories.
- **Excel Sheet Updates**: Updates test result sheets with log details and statuses.
- **Interactive User Interface**: Provides an intuitive interface for selecting files and directories.
- **Rich Progress Tracking**: Displays detailed progress bars and summaries using the `rich` library.

---

## Requirements
- Python 3.8 or later
- Libraries:
  - `shutil`
  - `BeautifulSoup` (from `bs4`)
  - `webbrowser`
  - `rich`
  - `pynput`
  - `tkinter`
  - `openpyxl`
  - `asammdf`
  - `pandas`
  - `urllib`

---

## Installation
1. Clone the repository:
   
   ```bash
   git clone https://github.com/yourusername/Failsafe-Log-Extractor.git cd Failsafe-Log-Extractor
   ```


2. Install dependencies:
   
   ```bash
    pip install -r requirements.txt
   ```


---

## Usage
The Failsafe_Log_Downloader program extracts test case links from an HTML report, segregates them, downloads logs, and updates an Excel sheet.

#### Steps:
1. Run the script:
```bash
python Failsafe_Log_Downloader.py
```
2. Follow the interactive prompts:
   - Provide the HTML report path or URL.
   - Specify the keyword for filtering links (e.g., `"measurement"`).
   - Choose a directory to store the logs.
   - Select the Excel sheet to update test case statuses.

---


---

## Contributions
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

---

### `Stay Curious !`


   
