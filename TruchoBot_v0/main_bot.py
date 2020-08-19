# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:09:30 2020

@author: urre
"""

import mov_det_screen_v1 as detector
import HP_detection as HP
import time
import pyautogui
import random

pyautogui.FAILSAFE = True


Action = False
action_time = 0


win_index = pyautogui.getAllTitles().index('Old School RuneScape')
#x0 = 1920-pyautogui.getAllWindows()[win_index].size.width + 20

x0 = pyautogui.getAllWindows()[win_index].topleft.x + 30




def eating_function(ptg,threshold,clicked_positions):
    inventory_positions= [[(1732, 769), (1774, 769), (1816, 769), (1858, 769)],
                         [(1732, 805), (1774, 805), (1816, 805), (1858, 805)],
                         [(1732, 841), (1774, 841), (1816, 841), (1858, 841)],
                         [(1732, 877), (1774, 877), (1816, 877), (1858, 877)],
                         [(1732, 913), (1774, 913), (1816, 913), (1858, 913)],
                         [(1732, 949), (1774, 949), (1816, 949), (1858, 949)],
                         [(1732, 985), (1774, 985), (1816, 985), (1858, 985)]]

    should_eat = False
    if ptg < threshold:
        should_eat = True
    else:
        should_eat = False
        
    if should_eat == True:
        pos = random.choice(random.choice(inventory_positions))
        
        if pos not in clicked_positions:
            pyautogui.moveTo(pos)
            pyautogui.click()
            print('-----------------  WE ATE   --------------------')
            clicked_positions.append(pos)
            time.sleep(0.6)
            
        
        
#        pyautogui.moveTo(random.choice(random.choice(inventory_positions)))
        

    

clicked_positions = []
threshold = 40.0 #hacer que venga de un input del usuario.

while True: 
    start = time.time()
    posXY = pyautogui.position()
    
    if time.time() - action_time > 7:
        Action = False
    
    if not Action:
        detector.main_detect_mov(x0)
        Action = True
        action_time = time.time()
        print(f'----------------- Action =  {Action} --------------')
    
    ptg = HP.main_HP()
    eating_function(ptg,threshold,clicked_positions)
    
    
    
    
    end = time.time()
    time.sleep(3)
    print(f'\n----------------- Round completed ----{round(time.time()-action_time,2)}------',round(end-start,3))
    if posXY[0] == 0 or len(clicked_positions) == 28:
        break 







