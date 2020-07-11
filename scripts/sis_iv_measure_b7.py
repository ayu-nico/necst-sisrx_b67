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
        self.pub1 = rospy.Publisher("/dev/cpz340816/rsw0/ch2",Float64,queue_size=1)
        self.sub1 = rospy.Subscriber("/dev/cpz3177/rsw0/ch3",Float64,self.stock_data1)
        self.sub2 = rospy.Subscriber("/dev/cpz3177/rsw0/ch4",Float64,self.stock_data2)

        #self.vol = np.nan
        #self.cur = np.nan
        self.path = "/home/telescopio/data_konishi/"

        self.t = datetime.datetime.now()
        self.ut = self.t.strftime("%Y%m%d-%H%M%S")

#データ用意する
    def stock_data1(self,vol):
        self.vol = vol.data

    def stock_data2(self,cur):
        self.cur = cur.data

#データ保存
    def measure(self, initv, interval, repeat):
        self.da_all=[]
        self.pub1.publish(initv/3)
        time.sleep(3)
        for i in range(repeat+1):
            da = []
            in_vol = (initv+interval*i)/3
            data = in_vol
            self.pub1.publish(in_vol)
            time.sleep(0.3)
            da.append(self.vol/0.2)
            da.append(self.cur/0.002)
            print(da)
            self.da_all.append(da)
            time.sleep(0.01)
        self.pub1.publish(0)
        #print((da_all[-1][1]-da_all[0][1])/(da_all[-1][0]-da_all[0][0])) 傾き
        np.savetxt(self.path + "sis_iv_{}.txt".format(self.ut), np.array(self.da_all), delimiter=" ")

#データプロット

    def plot(self):
        da_all = np.array(self.da_all)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(da_all[:,0], da_all[:,1], marker="o", color="red")
        ax.set_xlabel("voltage[mV]")
        ax.set_ylabel("current[uA]")
        ax.set_title("SIS-IV")
        ax.grid(True)
        plt.savefig(self.path + "sis_iv_{}.png".format(self.ut))
        plt.show()


if __name__ == "__main__" :
    rospy.init_node("measure")
    ctrl = sis_iv()
    initv = -3.5
    interval = 0.05
    repeat = 140
    date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
    file_name = "sis_iv_b7" + '/' + date + '.necstdb'
    print(file_name)
    logger = core_controller.logger()
    logger.start(file_name)
    ctrl.measure(initv,interval,repeat)
    logger.stop()
    ctrl.plot()
