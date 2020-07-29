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


class magnet_current(object):

    def __init__(self):
        self.coil = rospy.Publisher("/necst/sisrxb67/sis_b7/coil/v_cmd",Float64, queue_size=1)
        self.dsb  = rospy.Publisher("/necst/sisrxb67/sis_b7/dsb/v_cmd" ,Float64, queue_size=1)

        date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
        self.file_name = "magnet_current" + '/' + date + '.necstdb'
        print(self.file_name)
        self.logger = core_controller.logger()

    def sis_set_v(self,offset,v=0):
        vol = (v+offset)
        self.dsb.publish(vol)

    def measure(self, initv, interval, repeat):
        self.coil.publish(initv)
        time.sleep(3)
        self.logger.start(self.file_name)
        for i in range(repeat+1):
            in_vol = (initv+interval*i)
            self.coil.publish(in_vol)
            time.sleep(1)
        logger.stop()
        self.coil.publish(0)

if __name__ == "__main__" :
    rospy.init_node("measure")

    initv = 0
    end_v = 20
    interval = 0.05
    sisv = 0

    repeat = (end_v-initv)/interval
    ctrl = magnet_current()

    ctrl.sis_set_v(sisv)
    ctrl.measure(initv,interval,repeat)
