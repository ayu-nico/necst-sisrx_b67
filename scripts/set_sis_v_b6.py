#!/usr/bin/env python3
import sys
import rospy
import std_msgs.msg

name = "sis_b6_set_v"
rospy.init_node(name)

sis_set1 = rospy.Publisher("/dev/cpz340816/rsw0/ch3", std_msgs.msg.Float64, queue_size=1)
sis_set2 = rospy.Publisher("/dev/cpz340816/rsw0/ch4", std_msgs.msg.Float64, queue_size=1)

lsb_v = float(input("How mush voltage for lsb?? = [mV]"))
usb_v = float(input("How mush voltage for usb?? = [mV]"))

v1 = lsb_v/3
v2 = usb_v/3
sis_set1.publish(v1)
sis_set2.publish(v2)
