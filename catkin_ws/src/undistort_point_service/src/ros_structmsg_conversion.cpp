#include "ros_structmsg_conversion.h"


// Conversions between experiments_exampleRequestStruct_T and experiments::exampleRequest

void struct2msg(experiments::exampleRequest* msgPtr, experiments_exampleRequestStruct_T const* structPtr)
{
  const std::string rosMessageType("experiments/exampleRequest");

  msgPtr->x_dist =  structPtr->XDist;
  msgPtr->y_dist =  structPtr->YDist;
}

void msg2struct(experiments_exampleRequestStruct_T* structPtr, experiments::exampleRequest const* msgPtr)
{
  const std::string rosMessageType("experiments/exampleRequest");

  structPtr->XDist =  msgPtr->x_dist;
  structPtr->YDist =  msgPtr->y_dist;
}


// Conversions between experiments_exampleResponseStruct_T and experiments::exampleResponse

void struct2msg(experiments::exampleResponse* msgPtr, experiments_exampleResponseStruct_T const* structPtr)
{
  const std::string rosMessageType("experiments/exampleResponse");

  msgPtr->x_undis =  structPtr->XUndis;
  msgPtr->y_undis =  structPtr->YUndis;
}

void msg2struct(experiments_exampleResponseStruct_T* structPtr, experiments::exampleResponse const* msgPtr)
{
  const std::string rosMessageType("experiments/exampleResponse");

  structPtr->XUndis =  msgPtr->x_undis;
  structPtr->YUndis =  msgPtr->y_undis;
}

