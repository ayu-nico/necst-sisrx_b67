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

        self.pub_i = rospy.Publisher("/necst/sis/b7/i", Float64, queue_size=1)
        self.pub_v = rospy.Publisher("/necst/sis/b7/v", Float64, queue_size=1)



    def iv_publisher(self,ch=0):
        while not rospy.is_shutdown():
            try:
                self.com.open()
                data = self.com.send(":READ?").strip().split(',')
                self.pub_v.publish(data[0])
                self.pub_i.publish(data[1])
                self.com.close()
                time.sleep(1)
            except:
                pass
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
