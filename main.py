import os
import shutil

# Folder mapping (extensions are lowercase)
folder_mapping = {
    "Images": [".png", ".jpg", ".jpeg", ".bmp", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".accdb"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Shortcuts": [".lnk"],
    "Others": []  # Fallback category
}

# Ask user for folder
folder_path = input("Enter the path of the folder to organize: ")

if not os.path.exists(folder_path):
    print("❌ Folder does not exist!")
    exit()

# Loop through files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip if it's a folder
    if os.path.isdir(file_path):
        continue

    # Get file extension (in lowercase)
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    # Find matching folder
    moved = False
    for folder, extensions in folder_mapping.items():
        if ext in extensions:
            target_folder = os.path.join(folder_path, folder)
            os.makedirs(target_folder, exist_ok=True)  # Create folder if missing
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved {filename} → {folder}")
            moved = True
            break

    # If no match, put in "Others"
    if not moved:
        target_folder = os.path.join(folder_path, "Others")
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Moved {filename} → Others")
