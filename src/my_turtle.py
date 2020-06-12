#!/usr/bin/env python
#license removed for brevity

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float32
from std_msgs.msg import Int32MultiArray
import turtle
import time

forward_value = [0 for i in range(5)]
turn_value = [0 for i in range(5)]

rospy.init_node('Turtle_view', anonymous=True)

tur = []
colorL = ['blue', 'red', 'yellow', 'green', 'black']
for i in range(5):
    tur_t = turtle.Turtle()
    tur_t.shape("turtle")
    tur_t.color(colorL[i])
    tur.append(tur_t)

def forward_hd(data, index):
    global forward_value
    data = int(data.data)
    if data >= 300:
        data = 300
    if data <= -300:
        data = -300
    forward_value[index] = data
    print(forward_value)

def turn_hd(data, index):
    global turn_value
    data = int(data.data)
    while data > 1800:
        data = data-360
    while data < -1800:
        data = data+360
    turn_value[index] = data

pub1 = []
pub2 = []
for i in range(5):
    pub1_1 = rospy.Publisher('/turtle/'+str(i+1)+'/position', Int32MultiArray, queue_size = 10)
    pub2_1 = rospy.Publisher('/turtle/'+str(i+1)+'/heading', Float32, queue_size = 10)
    pub1.append(pub1_1)
    pub2.append(pub2_1)
rospy.Subscriber('/turtle/1/forward', Int32, lambda data : forward_hd(data, 0))
rospy.Subscriber('/turtle/1/turn', Int32, lambda data : turn_hd(data, 0))
rospy.Subscriber('/turtle/2/forward', Int32, lambda data : forward_hd(data, 1))
rospy.Subscriber('/turtle/2/turn', Int32, lambda data : turn_hd(data, 1))
rospy.Subscriber('/turtle/3/forward', Int32, lambda data : forward_hd(data, 2))
rospy.Subscriber('/turtle/3/turn', Int32, lambda data : turn_hd(data, 2))
rospy.Subscriber('/turtle/4/forward', Int32, lambda data : forward_hd(data, 3))
rospy.Subscriber('/turtle/4/turn', Int32, lambda data : turn_hd(data, 3))
rospy.Subscriber('/turtle/5/forward', Int32, lambda data : forward_hd(data, 4))
rospy.Subscriber('/turtle/5/turn', Int32, lambda data : turn_hd(data, 4))

'''
pub1 = rospy.Publisher('/turtle/position', Int32MultiArray, queue_size = 10)
pub2 = rospy.Publisher('/turtle/heading', Float32, queue_size = 10)

rospy.Subscriber('/turtle/forward', Int32, forward_hd)
rospy.Subscriber('/turtle/turn', Int32, turn_hd)
'''

print(123)

while not rospy.is_shutdown():
    time.sleep(0.1)
    for i in range(5):
        tur[i].forward(forward_value[i])
        tur[i].right(turn_value[i])
        pos = tur[i].position()
        pos = [pos[0], pos[1]]
        pub_data = Int32MultiArray(data = pos)
        pub1[i].publish(pub_data)
        pub2[i].publish(tur[i].heading())
        forward_value[i] = 0
        turn_value[i] = 0
