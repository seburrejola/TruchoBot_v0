#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 00:18:03 2020

@author: urre
"""

#from PIL import Image
#import find_pixel_by_color_v2 as finder
#import pandas as pd
import pyautogui
from PIL import ImageGrab
import time
import numpy as np
pyautogui.FAILSAFE = True



def percentage_HP2(img, coord_img_26x26):
    reds = np.array(list(map(lambda x: img.load()[x][0],coord_img_26x26)))
    ptg = round((np.count_nonzero(reds >50)*100)/len(coord_img_26x26),1)
    #print(f'{ptg}% HP')  
    return ptg
    

def main_HP():
    x_ss = 1735 - 91     
    y_ss = 82 + 21   
    w_ss = 33          
    h_ss = 33        
    coord_img = []
    top_white_line = 6     
    mid_white_line = 20  
    top_green_line = 16   
    mid_green_line = 6    



    for i in range(h_ss):
        if i<=top_white_line : 
            coord_img.append((top_green_line ,i))
        if i>top_white_line  and i<=top_white_line + mid_white_line :
            coord_img.append((mid_green_line,i))    
        if i>top_white_line + mid_white_line:
            coord_img.append((top_green_line ,i))

    start = time.time()

    img = ImageGrab.grab(bbox=(x_ss,y_ss,x_ss + w_ss ,y_ss + h_ss))
    ptg = percentage_HP2(img, coord_img)
    
    end = time.time()
    print(f'----------------- {ptg}% HP --------------------',round(end-start,3))
    return ptg

    
    
    


