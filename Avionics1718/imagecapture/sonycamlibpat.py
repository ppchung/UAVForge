"""
This is a test program for using gphoto2 to operate a Sony a6000 mini dslr.
Written By: Patrick Chung
From: https://www.youtube.com/watch?v=1eAYxnSU2aw&t=179s
"""

from time import sleep
import os
import subprocess
from sh import gphoto2 as gp
import signal

print('hello')
print('how do ya do')

print('HOLY MOLY!')

"""
#Sony a6000 does not have a true need for process killing, this is just part of the tutorial
def killgphoto2Process():
		p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
		out, err = p.communicate()
		
		#Search for the line that has the process we want to kill
		for line in out.splitlines():
			if b'gvfsd-gphoto2' in line:
				#Kill
				pid = int(line.split(None,1)[0])
				os.kill(pid, signal.SIGKILL)
"""
photoNum = 0
wakeupCommand = "--summary"
captureCommand = "--capture-image-and-download --filename=sony0.jpg --force-overwrite"
gp(captureCommand)
"""
sleep(4)
p = subprocess.Popen(['gphoto2', '--capture-image-and-download'], stdout=subprocess.PIPE)
out, err = p.communicate()
for line in out.splitlines():
	print(line)
"""

