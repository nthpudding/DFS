import tkinter as tk
from tkinter import filedialog
import subprocess
from DFS import *

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Choose input file", filetypes=[("Text files", "input.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
        order, title, G, pos, stack_list, start_node, end_node = perform_dfs(file_path)
        print_result(order, stack_list, G)
def graph_dfs(file_path):
    order, title, G, pos, stack_list, start_node, end_node = perform_dfs(file_path)
    visualize(order, title, G, pos, start_node, end_node)
root = tk.Tk()
root.title("Import")
root.geometry("300x200")

button = tk.Button(root, text="Import file", command=open_file_dialog)
button.pack(pady=20)
button_dfs = tk.Button(root, text="Graph DFS", command=lambda: graph_dfs("input.txt"))
button_dfs.pack(pady=20)

root.mainloop()