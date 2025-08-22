import pandas as pd
import tkinter as tk
from asammdf import MDF
from rich import print as print_
from tkinter import ttk, filedialog
import time, math, random, os
import urllib, urllib3
import webbrowser
from pathlib import Path
from urllib.parse import urlparse
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn, TimeElapsedColumn
import pynput
import Helper_Functions_Failsafe_Log_Downloader as h


# ------------------------------------------------------ RICH FORMATTER ------------------------------------------------------
def gen(text: str, style: str = 'bold'):
    """Generate styled rich text"""
    return f"[{style}]{text}[/{style}]"

# ---------------------------------------------------------------------------------------------------------------------------------------

def show_banner(version="1.0"):
    """Displays a randomly selected banner with the provided version number."""
    banners = [
        """
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
⣿⣿⣿⣿⣿⣿⡿⢠⣿⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⡄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⢛⣛⡋  \\_   _____/|    |    \\_   _____/\\   \\/  /
⣿⣿⣿⣿⣿⣿⠇⣾⠁⠀⠿⠂⢹⣿⣿⣿⣿⣿⣿⣿⡟⠁⣶⡀⠙⣿⣿⣿⡇⢿⣿⣿⡿⠟⣛⣫⣭⣴⣶⣶⣿⣿⣿⣿⡿⢡   |    __)  |    |     |    __)_  \\     / 
⣿⣿⣿⣿⣿⡿⢰⣿⣆⣀⣀⣠⣾⣿⣏⣙⣿⣿⣿⣿⣇⠀⠀⠀⢀⣿⣿⣿⡧⢘⣩⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣿   |     \\   |    |___  |        \\ /     \\ 
⣿⣿⣿⣿⣿⠃⣙⠻⣿⣿⡟⠿⠿⠋⣠⣉⠻⢿⣿⣿⢿⣿⣶⣾⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣾⣿   \\___  /   |_______ \\/_______  //___/\\  \\
⣿⣿⣿⣿⡏⢸⣿⣷⢸⣿⣿⣇⢁⣾⣿⣿⣿⣶⣶⢰⣿⣿⣿⠟⣩⣶⣬⡛⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣼⣿⣿       \\/            \\/        \\/       \\_/
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
        """,

        """
⣿⣿⣿⣿⢃⣾⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢳⡌⢿⣿⣿⣿
⣿⣿⣿⠇⣼⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣷⠘⣿⣿⣿
⣿⣿⡟⢰⣿⡇⠸⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⡇⢸⣿⡇⢹⣿⣿
⣿⣿⡇⢸⣿⣧⡀⣿⣿⠟⣋⣥⣶⣶⣾⣿⣶⣶⣤⣉⠻⢿⣿⠃⣼⣿⣿⢸⣿⣿
⢹⣿⡇⢸⣿⣿⣷⣌⠁⠒⢦⣿⣿⣿⣿⣿⣿⣿⣿⣰⠒⠀⢁⣼⣿⣿⣿⢸⣿⡟
⢀⢻⣧⠸⣿⣿⡿⣿⣿⡆⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠰⣾⣿⢿⣿⣿⡇⣸⡿⡁
⡇⢦⡻⣆⠹⡻⣿⣾⡍⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠩⣵⣿⡟⠛⣰⡟⡵⢁
⣇⢢⠳⣌⠓⢠⣄⣤⣔⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⣤⣠⣅⠰⣫⡾⣵⢸      ___________.____     _______________  ___
⣿⠘⣶⢙⠃⢿⣿⢎⣿⣿⣿⣿⣿⣿⢻⡿⣵⣿⣿⣿⣿⣿⣕⣿⡿⠀⣋⣾⡇⣾      \\_   _____/|    |    \\_   _____/\\   \\/  /
⣿⣿⣷⣄⠻⢰⣿⣷⡄⢩⣙⠻⢿⡟⣿⣿⢸⣿⠿⣛⡭⢀⣾⣿⡆⠻⢃⣾⣿⣿       |    __)  |    |     |    __)_  \\     /  
⣿⣿⣿⣿⣇⢸⣿⣿⣿⣷⣬⣥⣴⣥⣿⣿⣬⣤⣬⣭⣾⣿⣿⣿⡿⢰⣿⣿⣿⣿       |     \\   |    |___  |        \\ /     \\ 
⣿⣿⣿⣿⣿⣦⠙⣿⡛⠫⣭⣿⣿⡆⣿⣿⠳⣿⣿⣭⡭⡛⣻⠏⣠⣿⣿⣿⣿⣿       \\___  /   |_______ \\/_______  //___/\\  \\
⣿⣿⣿⣿⣿⣿⣧⠘⣷⣵⠘⢿⣿⢱⣾⣿⡇⢿⣿⠋⣜⣾⠏⢸⣿⣿⣿⣿⣿⣿           \\/            \\/        \\/       \\_/
⣿⣿⣿⣿⣿⣿⣿⡀⢿⣿⣧⢣⣝⡃⠹⡟⢐⣫⡵⣰⣿⡿⠇⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⢿⡔⣅⡛⡀⠑⢙⣭⢆⡿⢋⣴⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⡵⢌⡛⠷⠾⠛⢩⢎⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢻⣶⣶⣶⣶⡿⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠹⠿⠿⠟⣠⣿⣿⣟⣩⣭⣭⣭⣽⣿⣿⣿⣿
        """
        
        ]
    separator = '[bold #00ff00]-+-[/bold #00ff00]' * 36
    F = gen(f"F", "bold #00ffff")
    L = gen(f"L", "bold #00ffff")
    EX = gen(f"EX", "bold #00ffff")
    abbreviation = gen(f"{F}ailsafe {L}og {EX}tractor", "bold #FFFF00")
    selected_banner = random.choice(banners)
    print_(f"\n\n{separator}{gen(f"\n{selected_banner}", "bold #00ffff")}\nVersion - {version}\n{abbreviation}\n{separator}\n")
    print_("Failsafe Log EXtractor")

#---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------
#---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------

def main():

    DOWNLOAD_DIR = Path.home() / "Downloads"
    #FAILED_DIR = Path("D:/Docs/04_Python Codes/01_Conti_Tools/12_FAME_Run_Logs_Downloader/FAILED")
    HTML_REPORT_PATH : Path
    KEYWORD = "measurement"

    HTML_REPORT_PATH = h.get_HTML_path() # type: ignore
    
    # Loading the links from the TR
    links = h.extract_links_from_html(HTML_REPORT_PATH, KEYWORD)
    passed_links = h.segregate_links(links)['passed_testcases_links']

    # Downloading all the PASSED test cases
    print_("\n{}{}".format(gen('---> ', 'bold #FEFA02'), gen(f"Press Enter Key to download all the {len(passed_links)} PASSED logs - ", 'bold #00ffff')))
    pause = input("")
    h.z_FAME_downloader(passed_links)

    # Moving the PASSED logs from Download folder to User selected folder
    print_("\n{}{}".format(gen('---> ', 'bold #FEFA02'), gen("Press Enter Key to select the folder where you want to store the PASSED test cases - ", 'bold #00ffff')))
    pause = input("")
    PASSED_DIR = filedialog.askdirectory()
    print_("\n{}{}".format(gen('---> ', 'bold #FEFA02'), gen("Press Enter Key to move the logs to Selcted Folder from Downloads - ", 'bold #00ffff')))
    pause = input("")
    h.move_files(DOWNLOAD_DIR, PASSED_DIR)

    # Updating the TR sheet.
    tr_sheet_path = h.TR_path_fetch()
    h.TR_update(tr_sheet_path, PASSED_DIR)







#---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------
#---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------+++---------

def continue_prompt() -> bool:
    """Prompt the user to continue running the main function."""
    try:
        user_input = input("\nType 'yes' or 'y' to repeat execution: ").strip().lower() 
        return user_input in ('yes', 'y', '', ' ')
    except Exception as e:
            print_(gen(f"Error {str(e)} occurred while fetching prompt :(", 'bold #ff471a'))
            return False

# Main execution loop with error handling
def run_program():
    show_banner()
    while True:
        try:
            start = time.time()
            main()
            stop = time.time()
            t = round(stop-start, 2)
            print_(f"\nThat took {gen(str(t), "bold purple")}s....next version will be time optimised :)\n")
        except Exception as e:
            print_(gen(f"Error occurred during executing main function: {str(e)}", 'bold #ff471a'))
        if not continue_prompt():
            break
    print_(gen("\nExiting program...\n", "bold #ff6347"))


# Run the program
if __name__ == "__main__":
    run_program()