import cv2
from matplotlib import pyplot as plt
import numpy as np

def show_image(img):
    if img is None:
        print('None!')
        return 
    plt.axis('off')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

def load_img(path, n=None):
    fname = n or 1
    img = cv2.imread("%s/%d.jpg" % (path, fname))
    return fname, img

def foo(img):
    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    d = min(gimg.shape)
    
    circles = cv2.HoughCircles(gimg, cv2.HOUGH_GRADIENT, 1, minDist=15,
                               param1=50,
                               param2=30, minRadius=45, maxRadius=60)
    
    if circles is None:
        return
    timg = img.copy()
    for i in circles[0, :]:
        cv2.circle(timg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(timg, (i[0], i[1]), 2, (0, 0, 255), 3)
    return timg


def wheelDetector(img, min_Rad, max_Rad, accumulatorThreshold):
    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    d = min(gimg.shape)
    
    circles = cv2.HoughCircles(gimg, cv2.HOUGH_GRADIENT, 1, minDist=15,
                               param1=50,
                               param2=accumulatorThreshold, minRadius=min_Rad, maxRadius=max_Rad)
    
    if circles is None:
        return
    timg = img.copy()
    hasCar = False
    for i in circles[0, :]:
        cv2.circle(timg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(timg, (i[0], i[1]), 2, (0, 0, 255), 3)
        for j in circles[0, :]:
            if (abs(i[0] - j[0]) >= 10) and (abs(i[1] - j[1]) <= 20) and (abs(i[2] != j[2]) <= 10):
                hasCar = True
    
    return timg, hasCar
