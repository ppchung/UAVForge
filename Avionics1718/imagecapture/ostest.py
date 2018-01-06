import os, subprocess, signal
from time import sleep
"""
p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
out, err = p.communicate()
for line in out.splitlines():
	if b'gvfsd-gphoto2' in line:
		pid = int(line.split(None, 1)[0])
		os.kill(pid, signal.SIGKILL)
"""
p = subprocess.Popen(['sudo', 'gphoto2', '--capture-image-and-download', '--filename=000.jpg', '--force-overwrite'], stdout=subprocess.PIPE)
out, err = p.communicate()
print(out)
#os.system("gphoto2 --camera "Sony Alpha-A6000 (Control)" --capture-image-and-download --filename=000.jpg --force-overwrite")
sleep(1)
p = subprocess.Popen(['sudo', 'gphoto2', '--capture-image-and-download', '--filename=001.jpg', '--force-overwrite'], stdout=subprocess.PIPE)
out, err = p.communicate()
print(out)
sleep(1)
photoNum = 3
p = subprocess.Popen(['sudo', 'gphoto2', '--capture-image-and-download', '--filename='+str(photoNum)+'.jpg', '--force-overwrite'], stdout=subprocess.PIPE)
out, err = p.communicate()
print(out)
sleep(1)
subprocess.call(['sudo', 'feh', str(photoNum)+'.jpg', '-.'])
"""
os.system("sudo gphoto2 --capture-image-and-download --filename=001.jpg --force-overwrite")
photoNum = 3
sleep(1)
os.system("sudo gphoto2 --camera "Sony Alpha-A6000 (Control)" --capture-image-and-download --filename=" + str(photoNum) + ".jpg --force-overwrite")
sleep(1)
os.system("sudo feh " + str(photoNum) + ".jpg -.")
"""