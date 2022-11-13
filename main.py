import os
import shutil

ans = input("Hello !!! Wanna order Some Files pdf, sheets, and images? (Y or N): ")

if ans == "Y":
    source = input("Enter The Source Path: ")
    if os.path.exists(source):

        all_folders = ['PDFS_Files', 'IMAGES_Files', 'ZIP_Files', 'SHEETS_Files', 'TEXT_Files']
        for folder in all_folders:
            if os.path.exists(source + f"\\{folder}"):
                print(f"File Exist: {folder}")
            else:
                os.mkdir(source + f"\\{folder}")
        all_files = os.listdir(source)
        for file in all_files:
            extension = file.split(".")[-1]
            if extension == "pdf":
                shutil.move(source + f"\\{file}", source + "\\PDFS_Files")
            elif extension == "xlsx":
                shutil.move(source + f"\\{file}", source + "\\SHEETS_Files")
            elif extension == "png" or extension == "PNG" or extension == "gif":
                shutil.move(source + f"\\{file}", source + "\\IMAGES_Files")
            elif extension == "zip":
                shutil.move(source + f"\\{file}", source + "\\ZIP_Files")
            elif extension == "txt" or extension == "docs":
                shutil.move(source + f"\\{file}", source + "\\TEXT_Files")

        os.system(f"start {source}")
        print("Done Sorting")
    else:
        print("Sorry this path does not exist")
elif ans == "N":
    print("Stopped")

print("Thanks For Using .. ")
