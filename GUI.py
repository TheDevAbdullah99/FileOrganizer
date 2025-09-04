# NOTE!
# This GUi Powerd By Egycode Himself For File Orgaznier Desktop App. 
# This is Only GUi Without Any Actions Means the Buttons wont do anything or take any actions by the user & And its Only Made for Test.
# Thank You.



# Imports ALL the Modulces That Are Used.
import os 
import shutil
import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox

# The Main GUi.
frame = tk.Tk()
frame.title("File Orgaznier")
frame.geometry("400x300")
# frame.resizable(False, False) Its For cant Resize the Window of the app.
frame.resizable(False, False)


# Main buttons

# Choose Folder Button.
select_folder_B = tk.Button(text="Choose Folder" ,)
select_folder_B.pack(side="left" , pady=9)

# File Orgaznier Button 
File_Orgaznier_Button = tk.Button(text="File Orgaznier" , )
File_Orgaznier_Button.pack(side="left" , pady=7)

# Log Box
log_box = tk.Text(frame)
log_box.pack(side="right", pady=1)
log_box.config(state="disabled")







# About Frame.
def about_us():
    messagebox.showinfo("About", "Powerd By Egycode (File Orgaznier 1.0)")

# button_about
button_about_us = tk.Button(text="About", command=about_us)
button_about_us.pack(side="top")




# Main Loop Of the App.
frame.mainloop()