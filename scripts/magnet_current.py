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
        self.pub1 = rospy.Publisher('/necst/sisrxb67/sis_b7/magnetic/v_cmd',Float64,queue_size=1)
        self.t = datetime.datetime.now()
        self.ut = self.t.strftime("%Y%m%d-%H%M%S")


    def measure(self, initv, interval, repeat):

        date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
        file_name = "magnet_current" + '/' + date + '.necstdb'
        print(file_name)
        logger = core_controller.logger()

        self.pub1.publish(initv)
        time.sleep(3)
        logger.start(file_name)
        for i in range(repeat+1):
            in_vol = (initv+interval*i)
            self.pub1.publish(in_vol)
            time.sleep(2)
            print("\r {0}% [{1}]".format(int(i/repeat*100),int(i/repeat)*"#"),end="")
        time.sleep(1)
        logger.stop()
        self.pub1.publish(0)


if __name__ == "__main__" :
    rospy.init_node("measure")
    initv = 0
    interval = 0.05
    repeat = 500
    ctrl = magnet_current()
    ctrl.measure(initv,interval,repeat)
