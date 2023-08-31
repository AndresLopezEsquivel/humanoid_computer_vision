#!/usr/bin/env python3
from experiments.srv import example, exampleResponse, exampleRequest
import rospy

def client():
    serv_name = 'experimental_service'
    rospy.wait_for_service(serv_name)
    try:
        service_func = rospy.ServiceProxy(name = serv_name,
                                        service_class = example)

        req = exampleRequest()
        req.x_dist = 1280
        req.y_dist = 0

        res = service_func(req)
        
        print('x_dist: ', res.x_undis)
        print('y_dist: ', res.y_undis)

    except rospy.ServiceException as e:
        print("Service call failed: ", e)

if __name__ == '__main__':
    client()