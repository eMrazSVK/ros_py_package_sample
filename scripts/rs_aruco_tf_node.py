#!/usr/bin/env python
import rospy
from ae_drone.control.rs_aruco_tf import RsArucoTf

    
if __name__ == '__main__':
    rs_aruco_tf = RsArucoTf()
    try:
        rs_aruco_tf.run()
    except rospy.ROSInterruptException:
        pass  
