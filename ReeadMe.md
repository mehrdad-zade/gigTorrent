# gigTorrent - Torrent Downloader

This application allows you to download torrents using magnet links. It is implemented in Python and is intended to be used on macOS. The application is accompanied by an AppleScript which automates the process of opening a terminal and running the Python script with a user-provided magnet link.

## Prerequisites

Before you start using this application, ensure you have Python installed on your Mac. You will also need to install `libtorrent` and `tqdm` Python packages.

## Installation

1. **Install Python Packages**:
   Open your terminal and run the following commands:

   ```bash
   pip install libtorrent
   pip install tqdm
   ```

2. **Update the code and provide the DOWNLOAD_PATH

3. **Ensure the Script is Executable

    ```bash
    chmod +x app.py
    ```

4. **Create and Configure the AppleScript

- Open Script Editor on your Mac, found in Applications > Utilities.
- Write the AppleScript with the following content, adjusting the path to where your app.py script is located:

```applescript
tell application "Finder"
	set magnetLink to text returned of (display dialog "Paste the magnet link and press Enter:" default answer "")
end tell

tell application "Terminal"
	do script "export PYTHONWARNINGS='ignore'; cd /Users/zade/Downloads/github.com/mehrdad-zade/torrent-dowloader; clear; python app.py \"" & magnetLink & "\""
	activate
end tell

```
- Save the Script as an Application: Go to File > Save. Choose a name for your application and select Application as the file format.

## Usage

Go to the PirateBay site of choice, copy the magnet link and open the apple script application you built. It will open a small window for you to paste the magnet link. Click OK and it will open the terminal. Sometimes the link is not enclosed with quotation. Add a double quotation to the end of the magnet link that appears on the terminal and hit enter.