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
        self.pub1 = rospy.Publisher("/dev/pmx18/ip_192_168_100_175/volt_cmd",Float64,queue_size=1)
        self.pub2 = rospy.Publisher("/dev/cpz340816/rsw0/ch2",Float64,queue_size=1)
        self.t = datetime.datetime.now()
        self.ut = self.t.strftime("%Y%m%d-%H%M%S")



    def sis_set_v(self,offset,v=0):
        vol = (v+offset)/3
        self.pub2.publish(vol)

    def measure(self, initv, interval, repeat):
        self.pub1.publish(initv/100)
        time.sleep(3)
        for i in range(repeat+1):
            in_vol = (initv+interval*i)/100
            self.pub1.publish(in_vol)
            time.sleep(2)
            print("\r {0}% [{1}]".format(int(i/repeat*100),int(i/repeat)*"#"),end="")
        self.pub1.publish(0)




if __name__ == "__main__" :
    rospy.init_node("measure")
    initv = 0
    interval = 0.05
    repeat = 500
    #offset = 0.5
    ctrl = magnet_current()
    date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
    file_name = "magnet_current" + '/' + date + '.necstdb'
    print(file_name)
    logger = core_controller.logger()
    #ctrl.sis_set_v(offset)
    logger.start(file_name)
    ctrl.measure(initv,interval,repeat)
    time.sleep(1)
    logger.stop()
