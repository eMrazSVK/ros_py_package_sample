import rospy

class RsArucoTf(object):
    def __init__(self):
        pass
        
    def run(self):
        rate = rospy.Rate(10)
        
        while not rospy.is_shutdown():
            rate.sleep()
