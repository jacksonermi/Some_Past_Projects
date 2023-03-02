#!/usr/bin/env python3

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
from time import sleep 


red = [255,0,0]
white = [255,255,255]
blue = [0,0,255]
green = [0,255,0]
yellow = [255,255,0]
s = SenseHat()
clear = [0,0,0]


s.clear(clear)
s.show_message('level one')
event = s.stick.wait_for_event()
stick_dir = 0
score = 0
def pushed_up(event): 
    print('working')
    global stick_dir
    if event.action != ACTION_RELEASED:
        stick_dir = 1
        
def pushed_down(event):
    global stick_dir
    if event.action != ACTION_RELEASED:
        stick_dir = 2

s.stick.direction_up = pushed_up
s.stick.direction_down = pushed_down

def square(event):
    s.set_pixel(0,0,blue)
    s.set_pixel(0,1,blue)
    s.set_pixel(0,2,blue)
    s.set_pixel(0,3,blue)
    s.set_pixel(0,4,blue)
    s.set_pixel(0,5,blue)
    s.set_pixel(0,6,blue)
    s.set_pixel(0,7,blue)
    s.set_pixel(1,0,blue)
    s.set_pixel(2,0,blue)
    s.set_pixel(3,0,blue)
    s.set_pixel(4,0,blue)
    s.set_pixel(5,0,blue)
    s.set_pixel(6,0,blue)
    s.set_pixel(7,0,blue)
    s.set_pixel(7,1,blue)
    s.set_pixel(7,2,blue)
    s.set_pixel(7,3,blue)
    s.set_pixel(7,4,blue)
    s.set_pixel(7,5,blue)
    s.set_pixel(7,6,blue)
    s.set_pixel(7,7,blue)
    s.set_pixel(6,7,blue)
    s.set_pixel(5,7,blue)
    s.set_pixel(4,7,blue)
    s.set_pixel(3,7,blue)
    s.set_pixel(2,7,blue)
    s.set_pixel(1,7,blue)
    sleep(1.5)
    s.show_message('1. square')
    s.show_message('2. skware')
    sleep(1)
    if stick_dir == 1:
        global score
        s.clear(green)
        sleep(.5)
        s.show_message('Yes!, +1')
        score +=1
    else: 
        s.clear(red)
        sleep(.5)
        s.show_message('wrong')
def circle(event):
    s.show_message('level 2')
    s.set_pixel(0,2,blue)
    s.set_pixel(0,3,blue)
    s.set_pixel(0,4,blue)
    s.set_pixel(0,5,blue)
    s.set_pixel(2,0,blue)
    s.set_pixel(3,0,blue)
    s.set_pixel(4,0,blue)
    s.set_pixel(5,0,blue)
    s.set_pixel(7,2,blue)
    s.set_pixel(7,3,blue)
    s.set_pixel(7,4,blue)
    s.set_pixel(7,5,blue)
    s.set_pixel(2,7,blue)
    s.set_pixel(3,7,blue)
    s.set_pixel(4,7,blue)
    s.set_pixel(5,7,blue)
    s.set_pixel(1,1,blue)
    s.set_pixel(1,2,blue)
    s.set_pixel(2,1,blue)
    s.set_pixel(5,1,blue)
    s.set_pixel(6,1,blue)
    s.set_pixel(6,2,blue)
    s.set_pixel(6,5,blue)
    s.set_pixel(6,6,blue)
    s.set_pixel(5,6,blue)
    s.set_pixel(1,5,blue)
    s.set_pixel(1,6,blue)
    s.set_pixel(2,6,blue)
    sleep(1.5)
    s.show_message('1. circule')
    s.show_message('2. circle')
    sleep(1)
    if stick_dir == 2:
        global score
        s.clear(green)
        sleep(.5)
        s.show_message('Yes!, +1')
        score +=1
    else:
        s.clear(red)
        sleep(.5)
        s.show_message('wrong')
def triangle(event):
    s.show_message('level 3')
    s.set_pixel(0,7,blue)
    s.set_pixel(0,6,blue)
    s.set_pixel(1,7,blue)
    s.set_pixel(2,7,blue)
    s.set_pixel(3,7,blue)
    s.set_pixel(4,7,blue)
    s.set_pixel(5,7,blue)
    s.set_pixel(6,7,blue)
    s.set_pixel(7,7,blue)
    s.set_pixel(1,5,blue)
    s.set_pixel(2,4,blue)
    s.set_pixel(3,3,blue)
    s.set_pixel(4,3,blue)
    s.set_pixel(5,4,blue)
    s.set_pixel(6,5,blue)
    s.set_pixel(7,6,blue)
    sleep(1.5)
    s.show_message('1. tryangle')
    s.show_message('2. triangle')
    sleep(1)
    if stick_dir == 2:
        global score
        s.clear(green)
        sleep(.5)
        s.show_message('Yes!, +1')
        score +=1
    else:
        s.clear(red)
        sleep(.5)
        s.show_message('wrong')
def rectangle(event):
    s.show_message('level 4')
    s.set_pixel(0,2,blue)
    s.set_pixel(0,3,blue)
    s.set_pixel(0,4,blue)
    s.set_pixel(0,5,blue)
    s.set_pixel(7,2,blue)
    s.set_pixel(7,3,blue)
    s.set_pixel(7,4,blue)
    s.set_pixel(7,5,blue)
    s.set_pixel(1,2,blue)
    s.set_pixel(2,2,blue)
    s.set_pixel(3,2,blue)
    s.set_pixel(4,2,blue)
    s.set_pixel(5,2,blue)
    s.set_pixel(6,2,blue)
    s.set_pixel(1,5,blue)
    s.set_pixel(2,5,blue)
    s.set_pixel(3,2,blue)
    s.set_pixel(3,5,blue)
    s.set_pixel(5,5,blue)
    s.set_pixel(6,5,blue)
    s.set_pixel(4,5,blue)
    sleep(1.5)
    s.show_message('1. rectangle')
    s.show_message('2. rectangil')
    sleep(1)
    if stick_dir == 1:
        global score
        s.clear(green)
        sleep(.5)
        s.show_message('Yes!, +1')
        score +=1
    else: 
        s.clear(red)
        sleep(.5)
        s.show_message('wrong')
def ellipse(event):
    s.show_message('level 5')
    s.set_pixel(0,4,blue)
    s.set_pixel(7,4,blue)
    s.set_pixel(1,3,blue)
    s.set_pixel(1,5,blue)
    s.set_pixel(6,5,blue)
    s.set_pixel(2,2,blue)
    s.set_pixel(3,2,blue)
    s.set_pixel(4,2,blue)
    s.set_pixel(5,2,blue)
    s.set_pixel(6,3,blue)
    s.set_pixel(5,6,blue)
    s.set_pixel(4,6,blue)
    s.set_pixel(6,5,blue)
    s.set_pixel(2,6,blue)
    s.set_pixel(3,6,blue)
    sleep(1.5)
    s.show_message('1. ellipse')
    s.show_message('2. illipsee')
    sleep(1)
    if stick_dir == 1:
        global score
        s.clear(green)
        sleep(.5)
        s.show_message('Yes!, +1')
        score +=1
    else: 
        s.clear(red)
        sleep(.5)
        s.show_message('wrong')



square(event)
stick_dir = 0
circle(event)
stick_dir = 0
triangle(event)
stick_dir = 0
rectangle(event)
stick_dir = 0
ellipse(event)
print('final score', score)
score = str(score) 
s.show_message('final score')
s.show_message(score)



