import subprocess
import os
import urllib.request
import shutil

sevenzip_download = "https://www.7-zip.org/a/7z1900-x64.exe"
def look_for_balatro():
    path = "C:/Program Files (x86)/Steam/steamapps/common/Balatro/Balatro.exe"
    does_balatro_exist = os.path.isfile(path)
    if does_balatro_exist:
        print("Balatro found! " + path)
    else:
        print("Balatro not found in default path!")
    
    while not does_balatro_exist:
        path = input("Enter the file path of Balatro (including /Balatro.exe at the end): ")
        path = path.removeprefix("\"").removesuffix("\"")

        does_balatro_exist = os.path.isfile(path)
        if does_balatro_exist:
            print("Balatro found! " + path)
        else:
            print("Balatro not found in the path you entered!")

    return os.path.realpath(path)

def check_7zip():
    try:
        os.system("\"C:/Program Files/7-Zip/7z.exe\"")
        print("7zip found!")
    except FileNotFoundError:
        print("7zip not found! Installing 7zip...")
        # download 7zip
        urllib.request.urlretrieve(sevenzip_download, "7zip.exe")
        print("We will now open the 7zip installer. You will be asked for admin permissions.")
        input("Press Enter to continue...")
        print("Installing 7zip...")
        subprocess.call("7zip.exe /S /D=C:/Program Files/7-Zip/")
        print("7zip installed!")


path = look_for_balatro()
# check if 7zip is installed
check_7zip()

# open music folder read files
music_folder = os.path.join(os.getcwd(), "resources", "sounds")
music_files = os.listdir(music_folder)
sevenzip_path = "C:/Program Files/7-Zip/7z.exe"

if os.path.exists("./original/"):
    print("Original music already extracted! Reversing patch...")
    # change working directory to original
    os.chdir("original")
    # add files to balatro.exe
    for file in music_files:
        print("Replacing " + file + "...")
        process = subprocess.Popen([sevenzip_path, "a", path, f"resources/sounds/{file}"])
        process.wait()

    # delete original folder
    os.chdir("..")
    shutil.rmtree("original")

    print(chr(27) + "[2J")
    print("Patch reversed! Enjoy the original music!")
    exit()


# extract balatro in specific path
print("Extracting Balatro.exe's original music...")

# create folder for original music
os.makedirs("original/resources/sounds", exist_ok=True)
for file in music_files:
    print("Extracting " + file + "...")
    process = subprocess.Popen([sevenzip_path, "e", path, f"resources/sounds/{file}", "-o" + "original/resources/sounds/"])
    process.wait()
# replace files in balatro.exe's resources/sounds/ with 7zip
for file in music_files:
    print("Replacing " + file + "...")
    process = subprocess.Popen([sevenzip_path, "a", path, f"resources/sounds/{file}"])
    process.wait()

print(chr(27) + "[2J")
print("Patch applied! Enjoy your new music!")
