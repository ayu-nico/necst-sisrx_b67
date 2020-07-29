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


class sis_iv(object):

    def __init__(self):
        self.dsb = rospy.Publisher("/necst/sisrxb67/sis_b7/dsb/v_cmd",Float64,queue_size=1)

        date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
        self.file_name = 'sis_iv_b7' + '/' + date + '.necstdb'
        print(self.file_name)
        self.logger = core_controller.logger()

    def measure(self, initv, interval, repeat):
        self.dsb.publish(initv)
        time.sleep(3)
        self.logger.start(self.file_name)
        for i in range(repeat+1):
            vol = (initv+interval*i)
            self.dsb.publish(vol)
            time.sleep(0.3)
        self.logger.stop()
        self.dsb.publish(0)


if __name__ == "__main__" :
    rospy.init_node("measure")

    initv = -2.4
    end_v = 2.4
    interval = 0.05

    repeat = (end_v-initv)/interval
    ctrl = sis_iv()
    ctrl.measure(initv,interval,repeat)
