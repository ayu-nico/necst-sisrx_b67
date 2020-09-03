#!/usr/bin/env python3


v1 = input("How mush voltage for lsb?? = ")
v2 = input("How mush voltage for usb?? = ")

sis_b6_lsb_sisv = v1 #mv
sis_b6_usb_sisv = v2 #mv

##################

name = 'sis_v_set'
import sys
import rospy
import std_msgs.msg

sis_set1 = rospy.Publisher("/dev/cpz340816/rsw0/ch1", std_msgs.msg.Float64, queue_size=1)
sis_set2 = rospy.Publisher("/dev/cpz340816/rsw0/ch2", std_msgs.msg.Float64, queue_size=1)

v = sis_v/3
sis_set1.publish(v)
sis_set2.publish(v)
