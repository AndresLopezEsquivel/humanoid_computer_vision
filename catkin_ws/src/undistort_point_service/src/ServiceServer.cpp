//
// Academic License - for use in teaching, academic research, and meeting
// course requirements at degree granting institutions only.  Not for
// government, commercial, or other organizational use.
// File: ServiceServer.cpp
//
// MATLAB Coder version            : 5.6
// C/C++ source code generated on  : 31-Aug-2023 18:25:47
//

// Include Files
#include "ServiceServer.h"
#include "anonymous_function1.h"
#include "anonymous_function11.h"
#include "cameraParameters.h"
#include "driver.h"
#include "experiments_exampleRequestStruct.h"
#include "experiments_exampleResponseStruct.h"
#include "rt_nonfinite.h"
#include "undistort_point_service_internal_types11.h"
#include "undistort_point_service_internal_types111.h"
#include "undistort_point_service_types.h"
#include "coder_array.h"
#include "mlroscpp_svcserver.h"
#include <algorithm>

// Function Definitions
//
// Arguments    : void
// Return Type  : void
//
namespace coder {
namespace ros {
void ServiceServer::callback()
{
  static const double dv[9]{531.16719459, 0.0,          0.0,
                            0.0,          532.5711697,  0.0,
                            686.90394518, 364.00099154, 1.0};
  anonymous_function b_this;
  b_anonymous_function c_this;
  cameraParameters cameraParams;
  array<double, 2U> jacobian;
  array<double, 2U> residual;
  double b_expl_temp[2];
  double c_expl_temp[2];
  double d_expl_temp;
  double e_expl_temp;
  double exitflag;
  double f_expl_temp;
  double g_expl_temp;
  char input[26];
  char expl_temp[19];
  for (int i{0}; i < 26; i++) {
    input[i] = RequestType[i];
  }
  //(&input[0]);
  if (IsInitialized) {
    double dist_points[2];
    MATLABSvcServer_lock(SvcServerHelper);
    MATLABSvcServer_unlock(SvcServerHelper);
    MATLABSvcServer_lock(SvcServerHelper);
    MATLABSvcServer_unlock(SvcServerHelper);
    //  == CAMERA PARAMETERS ==
    //  Camera instrinsic parameters
    //  function response = serviceCallback(src,reqMsg,defaultRespMsg)
    //      class(defaultRespMsg)
    //      properties(defaultRespMsg)
    //      response = defaultRespMsg;
    //      response.XUndis = 10;
    //  end
    //  Radial distortion coefficients
    //  Tangential distortion coefficients
    //  Camera parameters
    std::copy(&dv[0], &dv[9], &cameraParams.K[0]);
    cameraParams.RadialDistortion[0] = -0.31429497;
    cameraParams.RadialDistortion[1] = 0.09157624;
    cameraParams.RadialDistortion[2] = -0.01083083;
    cameraParams.TangentialDistortion[0] = -0.00064995;
    cameraParams.TangentialDistortion[1] = 0.00094649;
    //  class(defaultRespMsg)
    //  properties(defaultRespMsg)
    //  properties(reqMsg)
    dist_points[0] = ReqMsgStruct.XDist;
    dist_points[1] = ReqMsgStruct.YDist;
    b_this.workspace.b_this = &cameraParams;
    c_this.workspace.fun = b_this;
    c_this.workspace.ydata[0] = dist_points[0];
    c_this.workspace.ydata[1] = dist_points[1];
    optim::coder::levenbergMarquardt::driver(
        c_this, dist_points, residual, expl_temp, b_expl_temp, c_expl_temp,
        jacobian, exitflag, d_expl_temp, e_expl_temp, f_expl_temp, g_expl_temp);
    //  response = ros.msggen.experiments.exampleResponse;
    //  class(defaultRespMsg)
    RespMsgStruct.XUndis = dist_points[0];
    RespMsgStruct.YUndis = dist_points[1];
  }
}

//
// Arguments    : void
// Return Type  : ServiceServer *
//
ServiceServer *ServiceServer::init()
{
  static const char cv[26]{'e', 'x', 'p', 'e', 'r', 'i', 'm', 'e', 'n',
                           't', 's', '/', 'e', 'x', 'a', 'm', 'p', 'l',
                           'e', 'R', 'e', 'q', 'u', 'e', 's', 't'};
  static const char svcname[20]{'e', 'x', 'p', 'e', 'r', 'i', 'm',
                                'e', 'n', 't', 'a', 'l', '_', 's',
                                'e', 'r', 'v', 'i', 'c', 'e'};
  ServiceServer *obj;
  obj = this;
  obj->IsInitialized = false;
  for (int i{0}; i < 20; i++) {
    obj->ServiceName[i] = svcname[i];
  }
  for (int i{0}; i < 26; i++) {
    obj->RequestType[i] = cv[i];
  }
  obj->ReqMsgStruct = experiments_exampleRequestStruct();
  obj->RespMsgStruct = experiments_exampleResponseStruct();
  experiments::exampleRequest *reqMsgPtr = nullptr;   //();
  experiments::exampleResponse *respMsgPtr = nullptr; //();
  auto reqStructPtr = (&obj->ReqMsgStruct);
  auto respStructPtr = (&obj->RespMsgStruct);
  obj->SvcServerHelper = std::unique_ptr<MATLABSvcServer<
      experiments::exampleRequest, experiments::exampleResponse,
      experiments_exampleRequestStruct_T, experiments_exampleResponseStruct_T>>(
      new MATLABSvcServer<experiments::exampleRequest,
                          experiments::exampleResponse,
                          experiments_exampleRequestStruct_T,
                          experiments_exampleResponseStruct_T>(
          [this]() { this->callback(); }, reqStructPtr, respStructPtr)); //();
  MATLABSvcServer_createSvcServer(obj->SvcServerHelper, &obj->ServiceName[0],
                                  20.0);
  obj->callback();
  obj->IsInitialized = true;
  return obj;
}

} // namespace ros
} // namespace coder

//
// File trailer for ServiceServer.cpp
//
// [EOF]
//
