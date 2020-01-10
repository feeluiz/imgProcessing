#!/usr/bin/env python3
from PIL import Image
import numpy as np

# * limits rgb between 0 and 255
def contrains(x):
    return (255 if x > 255 else 0 if x < 0 else x) 
# * convert array in  pillow Image
def arrayToIMG(arr):
    newIMG = Image.fromarray(arr)
    # save -> newIMG.save("img.jpg")
    newIMG.show()
# * simple treshold filter
def tresholdIMG(treshold, img):
    data = np.array(img)
    for y in range(0, img.height):
        for x in range(0, img.width):
            data[y][x] = ([255,255,255] if (data[y][x].sum() // 3) > treshold 
                        else  [0,0,0])
    return data
# * Simple image bright filter
def brightIMG(perc, img):
    data = np.array(img)
    for y in range(0, img.height):
        for x in range(0, img.width):
            rgb = []
            for i in data[y][x]:
                rgb.append((contrains(int(i+perc))))
            data[y][x] = rgb
    return data
# *  Rotate a image
def rotateIMG(angle, img):
    data = np.array(img)
    data2 = np.zeros((img.width,img.height,3),dtype="uint8")
    
    x0 = img.width//2
    y0 = img.height//2
    
    radians =float(angle*(np.pi /180))

    for x in range(img.width):
        for y in range(img.height):
            sinT =  np.sin(radians)          
            cosT = np.cos(radians)
            
            x2 = cosT * (x - x0) - sinT * (y - y0) + x0
            y2 = sinT * (x - x0) + cosT * (y - y0) + y0
            
            x2 = int(x2)
            y2 = int(y2)
            
            if(x2 in range(img.width) and y2 in range(img.height)):
                data2[x2][y2] = data[x][y]  
    return data2

if __name__ == "__main__":
    im = Image.open("flower.jpg")
    im.show()

    data = tresholdIMG(100, im)
    arrayToIMG(data)
    data = brightIMG(-100, im)
    arrayToIMG(data)
    data = brightIMG(100, im)
    arrayToIMG(data)
    data = rotateIMG(90, im)
    arrayToIMG(data)
