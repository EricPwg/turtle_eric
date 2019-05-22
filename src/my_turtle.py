#!/usr/bin/env python
#license removed for brevity

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float32
from std_msgs.msg import Int32MultiArray
import turtle
import time

forward_value = 0
turn_value = 0

rospy.init_node('Turtle_view', anonymous=True)

tur = turtle.Turtle()
tur.shape("turtle")
tur.color("blue")

def forward_hd(data):
    global forward_value
    forward_value = data.data
    print(forward_value)

def turn_hd(data):
    global turn_value
    turn_value = data.data

pub1 = rospy.Publisher('/turtle/position', Int32MultiArray, queue_size = 10)
pub2 = rospy.Publisher('/turtle/heading', Float32, queue_size = 10)

rospy.Subscriber('/turtle/forward', Int32, forward_hd)
rospy.Subscriber('/turtle/turn', Int32, turn_hd)

print(123)

while not rospy.is_shutdown():
    print(forward_value)
    time.sleep(0.5)
    tur.forward(forward_value)
    tur.right(turn_value)
    pos = tur.position()
    pos = [pos[0], pos[1]]
    pub_data = Int32MultiArray(data = pos)
    pub1.publish(pub_data)
    pub2.publish(tur.heading())
    forward_value = 0
    turn_value = 0
