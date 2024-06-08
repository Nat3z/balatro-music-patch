# Balatro Music Patcher
A simple program for patching custom music into Balatro. (Specifically Dom Palombi's covers.)

This program uses 7zip to replace in-game files with the custom music. If 7zip is not installed, the program will download it for you, but it is
recommended to install it yourself. (here)[https://www.7-zip.org/]

[Latest Windows Release](https://github.com/Nat3z/balatro-music-patch/releases/tag/1.0)

## Usage
1. Download the latest release from the link above.
2. Extract the zip file.
3. Run the executable. (Windows might give you a warning from SmartScreen, but press `More Info -> Run Anyway`.)
4. Follow the instructions in the program.

## Manually Patching Music
1. Download 7zip from [here](https://www.7-zip.org/download.html).
2. Open the repository and navigate to the `resources/sounds/` folder.
3. Download the music from this folder.
4. Open where Balatro is located on your computer and right click on the Balatro executable (Balatro.exe).
5. Go to `7-Zip -> Open Archive`.
6. Navigate to the `resources/sounds/` folder in the archive.
7. Drag and drop the music files into the archive.
8. Close the archive and run Balatro.

## Building from Source
1. Clone the repository.
2. Install pyinstaller with `pip install pyinstaller`.
3. Run `pyinstaller --onefile main.py`.
4. The executable will be in the `dist/` folder.

## Credit
- Dom Palombi for the music covers.
- - [Balatro Boss Blind Cover](https://www.youtube.com/watch?v=Uxc0m4GRiuc)
- - [Balatro Main Theme Cover](https://www.youtube.com/watch?v=WJi6m7R8ADY)
- 7zip for opening archives.
- PyInstaller for .exe creation.
- The Balatro team for the game.

