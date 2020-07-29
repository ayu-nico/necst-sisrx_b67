#!/usr/bin/env python3

name = 'sis_v_set'

import sys
import rospy
import std_msgs.msg

b6_lsb_sis_v = 4.3 #mv
b6_usb_sis_v = 4.3 #mv
b7_dsb_sis_v = 4.3 #mv


##################
rospy.init_node(name)

usb = rospy.Publisher("/necst/sisrxb67/sis_b6/usb/v_cmd",Float64,queue_size=1)
lsb = rospy.Publisher("/necst/sisrxb67/sis_b6/lsb/v_cmd",Float64,queue_size=1)
dsb = rospy.Publisher("/necst/sisrxb67/sis_b7/dsb/v_cmd",Float64,queue_size=1)

usb.publish(b6_usb_sis_v/3)
lsb.publish(b6_lsb_sis_v/3)
dsb.publish(b7_lsb_sis_v/3)
