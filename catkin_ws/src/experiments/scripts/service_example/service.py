#!/usr/bin/env python3
# Where did I get experiments.srv? Read: http://wiki.ros.org/rospy/Overview/Services
from experiments.srv import example, exampleResponse
import rospy

def handler(req):
    print('x_dist: ', req.x_dist)
    print('y_dist: ', req.y_dist)
    # print(dir(exampleResponse))
    res = exampleResponse()
    res.x_undis = req.x_dist * 2
    res.y_undis = req.y_dist * 2
    return res

def server():
    rospy.init_node('experimental_server')
    serv = rospy.Service(name = 'experimental_service',
                        service_class = example,
                        handler = handler)
    rospy.spin()

if __name__ == '__main__':
    # To call it: rosservice call /experimental_service 1.0 2.0
    # Where 1.0 and 2.0 are the values of x_dist and y_dist, respectively
    server()