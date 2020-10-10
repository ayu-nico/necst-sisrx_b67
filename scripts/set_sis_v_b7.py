#!/usr/bin/env python3

v = input("How mush voltage ?? = ")

sis_b7_sisv = float(v) #mv

##################

name = 'sis_v_set'
import sys
import rospy
import std_msgs.msg
import ogameasure

host = "192.168.100.46"
gpibport = 2
com = ogameasure.gpib_prologix(host, gpibport)
com.open()
com.send(":SOUR:VOLT:LEV " + str(sis_b7_sisv/1000))
