import os, subprocess, signal

def captureImageAndDownload(fname):
  p = subprocess.Popen(['sudo', 'gphoto2', '--capture-image-and-download', '--filename='+fname+'.jpg', '--force-overwrite'], stdout=subprocess.PIPE)
  out, err = p.communicate()
  print(out)
  return out

def lapse(fname,interval,count):
  x = subprocess.Popen(['sudo', 'gphoto2', '-I '+interval, '-F '+count, '--capture-image-and-download', '--filename=%Y%m%d%H%M%S'+fname+'.jpg'], stdout$
  out, err = x.communicate()
  print(out)
  return out

def test():
  from time import sleep
  captureImageAndDownload('000')
  sleep(1)
  captureImageAndDownload('001')
  sleep(1)
  captureImageAndDownload('002')
  sleep(1)

if __name__=='__main__':
  test()
else:
  print("Loaded GPhotoWrapper")
