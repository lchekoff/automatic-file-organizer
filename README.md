## Name
Automatic Downloads Organizer

## Features
- Monitores the Downloads folder in real time
- Automatically sorts files into folders by type
- Creates folders if they do not exist
- Helps keep files organized and easy to find

## How It Works
The script watches the Downloads folder using the watchdog library.
When a new file appears, it checks the file extension and moves the file into a matching folder.

## Requirements
Python 3  
watchdog library

Install watchdog:

pip install watchdog

## Usage
1. Update the folder path if needed:

folder_path = "/Users/yourusername/Downloads"

2. Run the script:

python organizer.py

3. Download a file and it will be moved automatically.

## Why I Built It
I built this project to automate file organization and reduce clutter in my Downloads folder.

## Future Improvements
- Add support for more file types
- Allow custom categories

## License
This project is open source and free to use.
