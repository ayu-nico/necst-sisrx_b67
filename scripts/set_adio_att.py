#!/usr/bin/env python3

name = 'adios_att_set'

att1 = int(input("25 att1 = ?"))
att2 = int(input("25 att2 = ?"))
att3 = int(input("26 att1 = ?"))
att4 = int(input("26 att2 = ?"))

import time
import sys
import rospy
import std_msgs.msg

def set_att_ch1(cmd):
    data_class = std_msgs.msg.Int32
    topic_name = "/dev/adios/ip_192_168_100_25/att1_cmd"
    pub = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = False)
    time.sleep(1)
    pub.publish(cmd)
    return

def set_att_ch2(cmd):
    data_class = std_msgs.msg.Int32
    topic_name = "/dev/adios/ip_192_168_100_25/att2_cmd"
    pub = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = False)
    time.sleep(1)
    pub.publish(cmd)
    return

def set_att_ch3(cmd):
    data_class = std_msgs.msg.Int32
    topic_name = "/dev/adios/ip_192_168_100_26/att1_cmd"
    pub = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = False)
    time.sleep(1)
    pub.publish(cmd)
    return

def set_att_ch4(cmd):
    data_class = std_msgs.msg.Int32
    topic_name = "/dev/adios/ip_192_168_100_26/att2_cmd"
    pub = rospy.Publisher(name = topic_name, data_class = data_class, queue_size = 1, latch = False)
    time.sleep(1)
    pub.publish(cmd)
    return


rospy.init_node(name)
time.sleep(1)
set_att_ch1(att1)
set_att_ch2(att2)
set_att_ch3(att3)
set_att_ch4(att4)
