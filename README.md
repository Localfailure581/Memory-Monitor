Process Monitor
A Python script that monitors the top 10 processes with the highest memory usage, displays total memory and memory used, and updates a memory usage chart every second. The script uses the psutil module to retrieve process and memory information, and the tkinter and matplotlib modules for the graphical user interface.

Requirements
Python 3.x
psutil module (pip install psutil)
tkinter module (included with most Python installations)
matplotlib module (pip install matplotlib)

Usage
Open a terminal or command prompt.
Navigate to the directory containing the script.
Run the script by executing python process_monitor.py.
The GUI window will appear, displaying the top 10 processes by memory usage, total memory, and memory used. A memory usage chart will also be displayed and updated every second.
