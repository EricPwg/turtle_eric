#!/usr/bin/env python
# license removed for brevity

import time

import rospy
from std_msgs.msg import Int32

import Tkinter as tk

rospy.init_node('turtle_contorl', anonymous = True)

pub1 = rospy.Publisher('/turtle/1/forward', Int32, queue_size = 10)
pub2 = rospy.Publisher('/turtle/1/turn', Int32, queue_size = 10)

win = tk.Tk()
win.title('Turtle control')
win.geometry('200x200')

def for_onclick():
    pub1.publish(50)

def back_onclick():
    pub1.publish(-50)

def right_onclick():
    pub2.publish(15)

def left_onclick():
    pub2.publish(-15)

b1 = tk.Button(win, text = 'forward', command = for_onclick)
b2 = tk.Button(win, text = 'back', command = back_onclick)
b3 = tk.Button(win, text = 'right', command = right_onclick)
b4 = tk.Button(win, text = 'left', command = left_onclick)

b1.grid(row = 0, column = 1)
b2.grid(row = 2, column = 1)
b3.grid(row = 1, column = 2)
b4.grid(row = 1, column = 0)
win.mainloop()
