import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        os.chdir(folder_selected)
        subprocess.run(["jupyter", "notebook"])

# Create the main window
root = tk.Tk()
root.title("Jupyter Notebook Launcher")
root.geometry("300x150")

# Create and place a button on the main window
button = tk.Button(root, text="Choose Folder", command=select_folder)
button.pack(expand=True)

# Start the GUI event loop
root.mainloop()
