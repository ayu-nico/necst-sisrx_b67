#! /usr/bin/env python3

name = "source_gpib"

import time
import sys
import ogameasure
import rospy
import threading
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Int32
from socket import error as SocketError
import errno

class source(object):
    def __init__(self):
        self.host = "192.168.100.45"
        self.gpibport = 2
        self.com = ogameasure.gpib_prologix(self.host, self.gpibport)
        #print(host)
        #print(gpibport)
        self.com.open()
        self.pub_i = rospy.Publisher("/necst/sis/b7/i", Float64, queue_size=1)
        self.pub_v = rospy.Publisher("/necst/sis/b7/v", Float64, queue_size=1)
        time.sleep(3)


    def iv_publisher(self):
            for i in range(repeat+1):
                self.com.send(":READ?")
                time.sleep(0.2)
                data = self.com.readline().strip().split(",")
                print(data)
                self.pub_v.publish(float(data[0]))
                self.pub_i.publish(float(data[1]))
                time.sleep(0.1)
                continue

    def start_thread(self):
        th = threading.Thread(target=self.iv_publisher)
        th.setDaemon(True)
        th.start()

if __name__ == '__main__':
    rospy.init_node(name)

    iv = source()
    iv.start_thread()
    rospy.spin()
