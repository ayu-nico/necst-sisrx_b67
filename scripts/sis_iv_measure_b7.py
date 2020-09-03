#! /usr/bin/env python3

name = "sis_iv_b7"

import time
import datetime
import sys
import ogameasure
import rospy
import threading
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Int32

sys.path.append("/home/telescopio/ros/src/necst-core/scripts")
import core_controller

class sis_b7_iv(object):
    def __init__(self):
        self.host = "192.168.100.45"
        self.gpibport = 2
        self.com = ogameasure.gpib_prologix(self.host, self.gpibport)
        #print(host)
        #print(gpibport)
        self.com.open()
        self.pub_i = rospy.Publisher('/necst/sisrxb67/sis_b7/i', Float64, queue_size=1)
        self.pub_v = rospy.Publisher('/necst/sisrxb67/sis_b7/v', Float64, queue_size=1)
        time.sleep(3)


    def iv_measure(self,initv,interval,repeat):
        self.com.send(":SOUR:VOLT:LEV " + str(initv/1000))
        time.sleep(1)
        date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
        file_name = 'sis_iv_b7' + '/' + date + '.necstdb'
        print(file_name)
        logger = core_controller.logger()
        logger.start(file_name)

        for i in range(repeat+1):
            self.com.send(":SOUR:VOLT:LEV " + str((initv+interval*i)/1000))
            time.sleep(0.3)
            self.com.send(":READ?")
            time.sleep(0.3)
            data = self.com.readline().strip().split(",")
            print(data)
            self.pub_v.publish(float(data[0]))
            self.pub_i.publish(float(data[1]))
            time.sleep(0.1)
            continue
        logger.stop()


if __name__ == '__main__':
    rospy.init_node(name)

    initv = -3.0 #mV
    end_v = 3
    interval = 0.05

    repeat = int((end_v-initv)/interval)

    iv = sis_b7_iv()
    iv.iv_measure(initv,interval,repeat)
