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
        self.pub1 = rospy.Publisher('/necst/sisrxb67/sis_b6/lsb/v_cmd',Float64,queue_size=1)
        self.pub2 = rospy.Publisher('/necst/sisrxb67/sis_b6/usb/v_cmd',Float64,queue_size=1)

        self.sub1 = rospy.Subscriber('/necst/sisrxb67/sis_b6/lsb/i',Float64,self.stock_data1)
        self.sub2 = rospy.Subscriber('/necst/sisrxb67/sis_b6/lsb/v',Float64,self.stock_data2)
        self.sub3 = rospy.Subscriber('/necst/sisrxb67/sis_b6/usb/i',Float64,self.stock_data3)
        self.sub4 = rospy.Subscriber('/necst/sisrxb67/sis_b6/usb/v',Float64,self.stock_data4)

        self.t = datetime.datetime.now()
        self.ut = self.t.strftime("%Y%m%d-%H%M%S")

#データ用意する
    def stock_data1(self,vol):
        self.vol1 = vol.data

    def stock_data2(self,cur):
        self.cur1 = cur.data

    def stock_data3(self,vol):
        self.vol2 = vol.data

    def stock_data4(self,cur):
        self.cur2 = cur.data

#データ保存
    def measure(self, initv, interval, repeat):

        date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
        file_name = 'sis_iv_b6' + '/' + date + '.necstdb'
        print(file_name)
        logger = core_controller.logger()
        self.da_all1=[]
        self.da_all2=[]
        self.pub1.publish(initv)
        self.pub2.publish(initv)
        time.sleep(3)
        logger.start(file_name)

        for i in range(repeat+1):
            da1 = []
            da2 = []
            in_vol1 = (initv+interval*i)
            in_vol2 = (initv+interval*i)

            self.pub1.publish(in_vol1)
            self.pub2.publish(in_vol2)
            time.sleep(1)
            da1.append(self.vol1)
            da1.append(self.cur1)
            da2.append(self.vol2)
            da2.append(self.cur2)
            self.da_all1.append(da1)
            self.da_all2.append(da2)
        time.sleep(1)
        logger.stop()
        time.sleep(2)
        self.pub1.publish(0)
        self.pub2.publish(0)
        #print((da_all[-1][1]-da_all[0][1])/(da_all[-1][0]-da_all[0][0])) 傾き
        np.savetxt(self.path + "sis_iv_{}.txt".format(self.ut), np.array(self.da_all), delimiter=" ")

#データプロット

    def plot(self):
        da_all1 = np.array(self.da_all1)
        da_all2 = np.array(self.da_all2)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(da_all1[:,0], da_all1[:,1], marker="o", color="red")
        ax.scatter(da_all2[:,0], da_all2[:,1], marker="o", color="red")
        ax.set_xlabel("voltage[mV]")
        ax.set_ylabel("current[uA]")
        ax.set_title("SIS-IV")
        ax.grid(True)
        plt.savefig(self.path + "sis_iv_{}.png".format(self.ut))
        plt.show()

if __name__ == "__main__" :
    rospy.init_node("measure")
    ctrl = sis_iv()
    initv = -8 #mV
    interval = 0.05 #mV
    repeat = 320

    ctrl.measure(initv,interval,repeat)
    ctrl.plot()
