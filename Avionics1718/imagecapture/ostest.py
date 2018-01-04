import os
from time import sleep
os.system("sudo gphoto2 --capture-image-and-download --filename=000.jpg --force-overwrite")
sleep(1)
os.system("sudo gphoto2 --capture-image-and-download --filename=001.jpg --force-overwrite")