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
def screenGrab():
    box = (x_pad+1,y_pad+1,x_pad+641,y_pad+481)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()