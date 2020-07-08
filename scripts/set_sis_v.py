#!/usr/bin/env python3

name = 'sis_v_set'

import sys
import rospy

b = 6
sis_v = 4.5 #mv


##################
rospy.init_node(name)
if b == 6:
    sis_set = rospy.Publisher("/dev/cpz340816/rsw0/ch1", std_msgs.msg.Float64, queue_size=1)
elif b == 7:
    sis_set = rospy.Publisher("/dev/cpz340816/rsw0/ch2", std_msgs.msg.Float64, queue_size=1)
else:
    pass

v = sis_v/3
sis_set.publish(v)
