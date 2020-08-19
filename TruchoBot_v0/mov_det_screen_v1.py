# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:34:47 2020

@author: urre
"""


from skimage.measure import compare_ssim

import imutils
import cv2


import time
import numpy as np
from PIL import ImageGrab , Image

#import pandas as pd
import pyautogui
pyautogui.FAILSAFE = True




def main_detect_mov(x0):
    start1 = time.time()
    

    pixel_x0 = x0
    
    screen_width = pyautogui.size().width
    screen_height = pyautogui.size().height

    imgA = np.array(ImageGrab.grab(bbox=(pixel_x0,0,screen_width,screen_height - 50)))
    grayA = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
    
    imgB = np.array(ImageGrab.grab(bbox=(pixel_x0,0,screen_width,screen_height - 50)))
    grayB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

    
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    
    thresh = cv2.threshold(diff, 0, 255,
    	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    f1 = lambda x: cv2.boundingRect(x)
    boxes = list(map(f1,cnts))
    
    def f(lista):
        lista_aux = []
        for i in range(len(lista)):
            Area = int(lista[i][2]*lista[i][3])
            indice = i
            lista_aux.append((Area, indice))
        
        return lista_aux
    
    areas = f(boxes)
    areas.sort(reverse=True)
    try:
        ID = areas[0][1]
        centro_mas_grande = (int( pixel_x0 + boxes[ID][0] + 0.5 * boxes[ID][2] ) , int( boxes[ID][1] + 0.5 * boxes[ID][3] ) )
        
        
        pyautogui.moveTo(centro_mas_grande[0],centro_mas_grande[1]) 
        pyautogui.click()
    except:
        print('No box found')
    

    end = time.time()
    print('----------------- Detect completo --------------',round(end-start1,3))
    
    
def get_image(img,img2,box):
    
    (x, y, w, h) = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    Image.fromarray(img).show()
    Image.fromarray(img2).show()







