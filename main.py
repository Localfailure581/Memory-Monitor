import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import psutil


# Create the GUI window
root = tk.Tk()
root.title("Process Monitor")

# Get the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size and position of the window to fill the screen
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Create the title label
title_label = tk.Label(root, text="Process Monitor", font=("Helvetica", 32), bg="#0066CC", fg="white", height=2, width=30)
title_label.place(relx=0.5, rely=0.1, anchor='center')

# Get a list of all running processes
all_processes = [p for p in psutil.process_iter()]

# Sort the processes by their memory usage (from highest to lowest)
sorted_processes = sorted(all_processes, key=lambda p: p.memory_info().rss, reverse=True)

# Create the label to show the total memory and memory used
total_memory = psutil.virtual_memory().total / 1024 / 1024 / 1024
used_memory = (psutil.virtual_memory().total - psutil.virtual_memory().available) / 1024 / 1024 / 1024
memory_label = tk.Label(root, text=f"Total Memory: {total_memory:.2f} GB\nUsed Memory: {used_memory:.2f} GB",
                        font=("Helvetica", 16))
memory_label.place(relx=0.1, rely=0.2, anchor='nw')

# Create the listbox to show the top 10 processes by memory usage
listbox = tk.Listbox(root, font=("Helvetica", 16), width=50, height=10)
for p in sorted_processes[:10]:
    listbox.insert(tk.END, f"{p.name()}: {p.memory_info().rss / 1024 / 1024:.2f} MB")
listbox.place(relx=0.5, rely=0.5, anchor='center')

# Create the figure and subplot for the memory usage chart
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
ax.set_title("Memory Usage", fontdict={"fontsize": 16})
ax.set_xlabel("Time (s)")
ax.set_ylabel("Memory Used (GB)")
chart = FigureCanvasTkAgg(fig, root)

# Update the memory usage chart every second
def update_chart():
    global chart
    global ax
    global fig
    x, y = [], []
    i = 0
    while i < 60:
        x.append(i)
        y.append((psutil.virtual_memory().total - psutil.virtual_memory().available) / 1024 / 1024 / 1024)
        i += 1
    ax.clear()
    ax.set_title("Memory Usage", fontdict={"fontsize": 16})
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Memory Used (GB)")
    ax.plot(x, y)
    chart.draw()
    root.after(1000, update_chart)

chart.get_tk_widget().place(relx=0.8, rely=0.5, anchor='center')
update_chart()

# Start the GUI event loop
root.mainloop()