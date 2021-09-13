import opc
import cv2
import pickle
import PIL
import time

from PIL import Image
def video_function(video_name):
    pix = list()
# Locate and add the video file, temporarily using laptop camera as VideoCapture(0). The 0 is the camera. A file can be called here instead.
vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
success = True
client = opc.Client('10.80.31.24:7890')
#ADDED MAPPED PIXEL
mapped_pixel = (0,1)
try:
    while success:
        success,image = vidcap.read()
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    pix = []
    im = Image.fromarray(image)
    im = im.resize((85,85), Image.ANTIALIAS)
# Only want RGB, not RGBA
    for i in range(0,4661):
        pix.append(im.getpixel((mapped_pixel[i][0],mapped_pixel[i][1]))[:3]) 
    client.put_pixels(pix)
    time.sleep(1/60)         
except:
    print ("Video terminated unexpectedly!!")
