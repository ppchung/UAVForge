import RPi.GPIO as pin
import GPhotoWrapper
from time import sleep

# Sets the image filename counter to zero
x = 0

# GPIO
pin.setmode(pin.BCM)     # set up BCM GPIO numbering
pin.setup(23, pin.IN)    # set GPIO23 as input (button) this pin has an internal pullup
pin.setup(25, pin.OUT)   # set GPIO25 as output (LED) if it is solid, then it is takingpictures, if it blinks, then it is not
try:
        while True:
                while pin.input(23):
                        pin.output(25,1)        # Hold LED on to indicate IMG CPT is on
                        x = x + 1
                        outputdata = GPhotoWrapper.captureImageAndDownload("%Y%m%d%H%M%S Flight"+str(x)) # the subprocess command to take the image
                pin.output(25,1)        # \
                sleep(0.1)              #  \__Blinking procedure
                pin.output(25,0)        #  /
                sleep(0.9)              # /
finally:
        pin.cleanup()
