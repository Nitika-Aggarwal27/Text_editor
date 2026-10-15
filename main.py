# Text-editor project

# import tkinter for creating GUI 
import tkinter as tk
from tkinter import filedialog, messagebox

# Main window code
root = tk.Tk()
root.title("My Text-Editor")
root.geometry("800x900")


# create text area
text = tk.Text(
    root,
    wrap = tk.WORD,
    font=("Helvetica", 12)
)

text.pack(expand = True, fill=tk.BOTH)


# start and keeps the window open
root.mainloop()