from tkinter import Tk
from tkinter.filedialog import askdirectory
from PIL import Image
import os
import ctypes
import sys
import shutil


Tk().withdraw()  # closes small Tk window when filedialog is open

images_dir = askdirectory(title='Wybierz folder z zdjęciami')
try:
    files = os.listdir(images_dir)
except FileNotFoundError:
    os.system("python main.py")
    sys.exit()
    Tk().destroy()
counter = 0
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')
save_path = os.path.join(desktop_path + "Zdjęcia NxView\\")

try:
    os.makedirs(save_path)
except OSError:
    ctypes.windll.user32.MessageBoxW(0, 'Folder docelowy "Zdjęcia NxView" na pulpicie nie jest pusty. '
                                        'Skasuj folder i spróbuj ponownie.', "Wystąpił błąd", 0x10)
    os.system("python main.py")
    sys.exit()

for i in files:
    myimg = Image.open(images_dir + "\\" + i)
    width = int(myimg.size[0] * 0.22)
    height = int(myimg.size[1] * 0.22)
    newimg = myimg.resize((width, height))
    newimg.save(str(counter) + ".jpg")
    shutil.move(os.getcwd() + "\\" + str(counter) + ".jpg", save_path)
    counter += 1

ctypes.windll.user32.MessageBoxW(0, f'Wygenerowano {counter} zdjęć, znajdziesz je w folderze '
                                    f'"Zdjęcia NxView" na pulpicie.', "Informacja", 0x40)

Tk().destroy()  # destroy Tk window to avoid freezes by multiple Tk instances in background. Trust me :)
