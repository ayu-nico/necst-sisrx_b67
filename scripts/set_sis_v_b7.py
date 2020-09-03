#!/usr/bin/env python3

v = input("How mush voltage ?? = ")

sis_b7_sisv = v #mv

##################

name = 'sis_v_set'
import sys
import rospy
import std_msgs.msg

host = "192.168.100.45"
gpibport = 2
com = ogameasure.gpib_prologix(host, gpibport)
com.open()
com.send(":SOUR:VOLT:LEV " + str(initv/1000))
