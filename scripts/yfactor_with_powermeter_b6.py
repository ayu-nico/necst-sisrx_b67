# coding:utf_8
import sys
import time
import pyinterface
import threading
import rospy
import os,datetime
import numpy as np
import matplotlib.pyplot as plt
import std_msgs

sys.path.append("/home/telescopio/ros/src/necst-core/scripts")
import core_controller

from std_msgs.msg import String
from std_msgs.msg import Int32
from std_msgs.msg import Float64


class yfactor_b6(object):

    def __init__(self):
        self.lsb = rospy.Publisher("/necst/sisrxb67/sis_b6/lsb/v_cmd",Float64,queue_size=1)
        self.usb = rospy.Publisher("/necst/sisrxb67/sis_b6/usb/v_cmd",Float64,queue_size=1)

        date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
        file_name = "yfactor_with_powermeter_b6" + '/' + date + '.necstdb'
        print(file_name)
        self.logger = core_controller.logger()

    def measure_lsb(self, initv, interval, repeat):
        self.lsb.publish(initv)
        time.sleep(3)
        self.logger.start(file_name)
        for i in range(repeat+1):
            vol = (initv+interval*i)
            self.lsb.publish(vol)
            time.sleep(0.3)
        self.logger.stop()
        self.lsb.publish(0)

    def measure_usb(self, initv, interval, repeat):
        self.usb.publish(initv)
        time.sleep(3)
        self.logger.start(file_name)
        for i in range(repeat+1):
            vol = (initv+interval*i)
            self.usb.publish(vol)
            time.sleep(0.3)
        self.logger.stop()
        self.usb.publish(0)

    def measure_2sb(self, initv, interval, repeat):
        self.lsb.publish(initv)
        self.usb.publish(initv)
        time.sleep(3)
        self.logger.start(file_name)
        for i in range(repeat+1):
            vol = (initv+interval*i)
            self.lsb.publish(vol)
            self.usb.publish(vol)
            time.sleep(0.3)
        self.logger.stop()
        self.lsb.publish(0)
        self.usb.publish(0)

if __name__ == "__main__" :
    rospy.init_node("measure")

    mode = "lsb" #lsb or usb or 2sb
    initv = -8
    interval = 0.05
    end_v = 8

    repeat = (end_v-initv)/interval
    ctrl = yfactor_b6()
    if mode == "lsb":
        ctrl.measure_lsb(initv,interval,repeat)
    elif mode == "usb":
        ctrl.measure_usb(initv,interval,repeat)
    elif mode == "2sb":
        ctrl.measure_2sb(initv,interval,repeat)
