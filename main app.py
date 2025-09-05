# This GUI Powered By Egycode Himself For File Organizer Desktop App.
# Now it is connected with the file organizing function.

import os 
import shutil
import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox

# Folder mapping for file types
folder_mapping = {
    "Images": [".png", ".jpg", ".jpeg", ".bmp", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".accdb"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Shortcuts": [".lnk"],
    "Others": []  # Fallback category
}

folder_path = None  
# Function to select folder
def choose_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        log_box.config(state="normal")
        log_box.insert(tk.END, f"Selected Folder: {folder_path}\n")
        log_box.config(state="disabled")

# Function to organize files
def organize_files():
    global folder_path
    if not folder_path:
        messagebox.showwarning("Warning", "Please choose a folder first!")
        return
    
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "❌ Folder does not exist!")
        return

    log_box.config(state="normal")
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False
        for folder, extensions in folder_mapping.items():
            if ext in extensions:
                target_folder = os.path.join(folder_path, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                log_box.insert(tk.END, f"Moved {filename} → {folder}\n")
                moved = True
                break

        if not moved:
            target_folder = os.path.join(folder_path, "Others")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            log_box.insert(tk.END, f"Moved {filename} → Others\n")

    log_box.config(state="disabled")

# The Main GUI
frame = tk.Tk()
frame.title("File Organizer")
frame.geometry("500x350")
frame.resizable(False, False)

# Buttons
select_folder_B = tk.Button(frame, text="Choose Folder", command=choose_folder)
select_folder_B.pack(side="left", pady=9, padx=5)

File_Organizer_Button = tk.Button(frame, text="File Organizer", command=organize_files)
File_Organizer_Button.pack(side="left", pady=7, padx=5)

# Log Box
log_box = tk.Text(frame, height=13, width=30)
log_box.pack(side="right", pady=5, padx=5)
log_box.config(state="disabled")

# About

def about_us():
    messagebox.showinfo("About", "Powered By Egycode (File Organizer 1.0)")

button_about_us = tk.Button(frame, text="About", command=about_us)
button_about_us.pack(side="left",)

# Main loop
frame.mainloop()