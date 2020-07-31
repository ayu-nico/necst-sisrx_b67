#!/usr/bin/env python3


name = "yfactorspecana"

import time
import sys
import ogameasure
import datetime
import rospy
import threading
sys.path.append("/home/telescopio/ros/src/necst-core/scripts")
import core_controller

host = "192.168.100.45"
gpibport = 2
com = ogameasure.gpib_prologix(host, gpibport)

com.open()
time.sleep(2)

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = 'yfactor_with_sa_b7' + '/' + date + '.necstdb'
print(file_name)
logger = core_controller.logger()

v  = -1.9
meas_t = 30

rospy.init_node(name)
com.send(":SOUR:VOLT:LEV " + str(v/1000))
time.sleep(2)
logger.start(file_name)
time.sleep(meas_t)
logger.stop()
