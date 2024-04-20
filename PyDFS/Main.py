import tkinter as tk
from tkinter import filedialog
import subprocess
from DFS import *

file_path = None

def open_file_dialog():
    global file_path
    file_path = filedialog.askopenfilename(title="Choose input file", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)


root = tk.Tk()
root.title("Import")
root.geometry("300x200")

button = tk.Button(root, text="Import file", command=open_file_dialog)
button.pack(pady=20)
root.mainloop()