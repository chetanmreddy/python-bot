"""
 All coordinates assume a screen resolution of 1280x1024, and Chrome
maximized with the Bookmarks Toolbar enabled.

x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 828, 723
"""

# Globals
# ----------------------------
x_pad=187
y_pad=242

import os
from PIL import ImageGrab
import time
import win32api,win32con

def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+641,y_pad+481)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("Click.")         #completely optional. But nice for debugging purposes.
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)
def startGame():
    #location of first menu
    mousePos((318,194))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((267,385))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((343,397))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((583,442))
    leftClick()
    time.sleep(.1)
    
    #location of fourth menu
    mousePos((315,370))
    leftClick()
    time.sleep(.1)
    
class Cord:
        
    f_shrimp = (37,239)
    f_rice = (96,227)
    f_nori = (31,279)
    f_roe = (83,283)
    f_salmon = (39,327)
    f_unagi = (96,341)
# -------------------------------------------

    phone = (587,344)
 
    menu_toppings = (526,268)
     
    t_shrimp = (496,209)
    t_nori = (497,277)
    t_roe = (573,274)
    t_salmon = (493,326)
    t_unagi = (575,217)
    t_exit = (569,336)
 
    menu_rice = (529,289)
    buy_rice = (545,268)
     
    delivery_norm = (489,290)
    
def clear_tables():
    mousePos((87,205))
    leftClick()
 
    mousePos((186,201))
    leftClick()
 
    mousePos((292,199))
    leftClick()
 
    mousePos((392,204))
    leftClick()
 
    mousePos((493,205))
    leftClick()
 
    mousePos((600,204))
    leftClick()
    time.sleep(1)
    
def makeFood(food):
    if food == 'caliroll':
        print ('Making a caliroll')
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print ('Making a onigiri')
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)
         
        time.sleep(1.5)
 
    elif food == 'gunkan':
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
    leftClick()
    time.sleep(.1)
    
def call_for():
    for i in range(6):
        time.sleep(5.0)
        print(get_cords())
        
def main():
    pass

if __name__ == '__main__':
    main()
    
    
    




