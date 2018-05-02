import pypylon
import cv2
import numpy as np
import time


Nblocks = 1000  # arbitrary number of frames to plot

devices = pypylon.factory.find_devices()

def connect(camdev, camind=0):
    cam = pypylon.factory.create_device(camdev[camind])

    cam.open()
    cam.properties['PixelFormat'] = 'RGB8'
    return cam

cam = connect(devices, 0)

for i in range(Nblocks):

    images = cam.grab_images(1)
    img = [o for o in images][0]
    out = np.zeros((img.shape[0], img.shape[1] / 3, 3), dtype=np.uint8)
    for m in range(img.shape[1]):
        c = int(m / 3)
        out[:, c, 2 - (m % 3)] = img[:, m]
    cv2.imshow('ss', out)

    cv2.waitKey(5000)

cam.close()

