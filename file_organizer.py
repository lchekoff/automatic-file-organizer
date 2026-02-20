folder_path="/Users/lianachekoff/Downloads"

def organize_files():
    import os
    import shutil

    file_types={
        "Images": [".jpg", ".png", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xls", ".xlsx", ".csv", ".pages", ".pptx", ".ppt", ".rtf", ".doc"],
        "Videos": [".mp4", ".mov"],
        "Codes": [".py", ".html", ".ipynb", ".json"]
    }

    for filename in os.listdir(folder_path):
        file_path= os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            for folder, extensions in file_types.items():
                if filename.lower().endswith(tuple(extensions)):
                    destination_folder=os.path.join(folder_path, folder)

                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    
                    shutil.move(file_path, destination_folder)
                    print(f"Moved {filename} to {folder}")
                    break

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        organize_files()

observer=Observer()
observer.schedule(FileHandler(), folder_path, recursive=False)
observer.start()

print("Watching downloads...")

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
