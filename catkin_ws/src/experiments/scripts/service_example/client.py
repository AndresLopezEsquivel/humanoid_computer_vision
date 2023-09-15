#!/usr/bin/env python3
from experiments.srv import example, exampleResponse, exampleRequest
import rospy
import matplotlib.pyplot as plt
from pprint import pprint

def client():
    serv_name = 'experimental_service'
    rospy.wait_for_service(serv_name)
    try:
        service_func = rospy.ServiceProxy(name = serv_name,
                                        service_class = example)

        # req = exampleRequest()
        # req.x_dist = 1280
        # req.y_dist = 0
        # res = service_func(req)
        # print('x_dist: ', res.x_undis)
        # print('y_dist: ', res.y_undis)

        # x_data = [0] * 721 + list(range(1,1281)) + [1280] * 720 + list(range(1279,0,-1))

        # y_data = list(range(0,721)) + [720] * 1280 + list(range(719,-1,-1)) + [0] * 1279

        x_data = [0] * 721

        y_data = list(range(0,721))

        x_undis_data = []
        y_undis_data = []

        # print(len(x_data))

        # print(len(y_data))

        for i, data in enumerate(x_data):
            req = exampleRequest()
            req.x_dist = x_data[i]
            req.y_dist = y_data[i]
            res = service_func(req)
            x_undis_data.append(res.x_undis)
            y_undis_data.append(res.y_undis)
        """
        for w in range(10):
            req = exampleRequest()
            req.x_dist = w
            req.y_dist = 0
            res = service_func(req)
            x_data.append(res.x_undis)
            y_data.append(res.y_undis)
        """
        # pprint(x_data)
        # pprint(y_data)

        plt.plot(x_undis_data, y_undis_data)
        plt.show()

    except rospy.ServiceException as e:
        print("Service call failed: ", e)

if __name__ == '__main__':
    client()