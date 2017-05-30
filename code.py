"""
 All coordinates assume a screen resolution of 1280x1024, and Chrome
maximized with the Bookmarks Toolbar enabled.
"""

# Globals
# ----------------------------
x_pad=187
y_pad=242

import os
from PIL import ImageGrab
import time
import win32api,win32con
from PIL import ImageOps
from numpy import *

def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+641,y_pad+481)
    im = ImageGrab.grab(box)
    ## im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    return im

def grab():
    box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    return a

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('click')      #completely optional. But nice for debugging purposes.
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

    f_shrimp = (37,322)
    f_rice = (96,325)
    f_nori = (31,381)
    f_roe = (83,379)
    f_salmon = (39,434)
    f_unagi = (96,439)
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

def clearTables():
    mousePos((80,203))
    leftClick()

    mousePos((176,201))
    leftClick()

    mousePos((278,203))
    leftClick()

    mousePos((374,207))
    leftClick()

    mousePos((477,208))
    leftClick()

    mousePos((576,206))
    leftClick()
    time.sleep(1)

def makeFood(food):
    if food == 'caliroll':
        print ('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
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
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
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
        time.sleep(1.5)

    elif food == 'gunkan':
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
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

def buyFood(food):

    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print ('test')
        time.sleep(.1)
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            print ('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print ('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (33, 30, 11):
            print ('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()

        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (127, 61, 0):
            print ('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print (i+'is low and needs to be replenished')
                buyFood(i)

def get_seat_one():
    box = (215,305,215+63,305+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_two():
    box = (315,305,315+63,305+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_three():
    box = (416,305,416+63,305+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_four():
    box = (518,305,518+63,305+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_five():
    box = (619,305,619+63,305+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_six():
    box = (720,305,720+63,305+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

sushiTypes = {3954:'onigiri',
              4211:'caliroll',
              2899:'gunkan',}
class Blank:
    seat_1 = 7926
    seat_2 = 5986
    seat_3 = 11435
    seat_4 = 10280
    seat_5 = 5831
    seat_6 = 8294

def check_bubs():

    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print ('table 1 is occupied and needs ' + sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print ('sushi not found!\n sushiType = ' + str(s1))

    else:
        print ('Table 1 unoccupied')

    clearTables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print ('table 2 is occupied and needs ' + sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print ('sushi not found!\n sushiType = ' + str(s2))

    else:
        print ('Table 2 unoccupied')

    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print ('table 3 is occupied and needs ' + sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print ('sushi not found!\n sushiType = ' + str(s3))

    else:
        print ('Table 3 unoccupied')

    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print ('table 4 is occupied and needs ' + sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print ('sushi not found!\n sushiType = ' + str(s4))

    else:
        print ('Table 4 unoccupied')

    clearTables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print ('table 5 is occupied and needs ' + sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print ('sushi not found!\n sushiType = ' + str(s5))

    else:
        print ('Table 5 unoccupied')

    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print ('table 1 is occupied and needs ' + sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print ('sushi not found!\n sushiType = ' + str(s6))

    else:
        print ('Table 6 unoccupied')

    clearTables()

def main():
    startGame()
    while True:
        check_bubs()

if __name__ == '__main__':
    main()








