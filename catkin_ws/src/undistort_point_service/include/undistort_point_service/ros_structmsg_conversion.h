#ifndef _ROS_STRUCTMSG_CONVERSION_H_
#define _ROS_STRUCTMSG_CONVERSION_H_

#include <ros/ros.h>
#include <experiments/example.h>
#include <experiments/exampleRequest.h>
#include <experiments/exampleResponse.h>
#include "undistort_point_service_types.h"
#include "mlroscpp_msgconvert_utils.h"


void struct2msg(experiments::exampleRequest* msgPtr, experiments_exampleRequestStruct_T const* structPtr);
void msg2struct(experiments_exampleRequestStruct_T* structPtr, experiments::exampleRequest const* msgPtr);

void struct2msg(experiments::exampleResponse* msgPtr, experiments_exampleResponseStruct_T const* structPtr);
void msg2struct(experiments_exampleResponseStruct_T* structPtr, experiments::exampleResponse const* msgPtr);


#endif
