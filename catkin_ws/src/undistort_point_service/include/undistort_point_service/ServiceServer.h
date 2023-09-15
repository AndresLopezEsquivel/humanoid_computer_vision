//
// Academic License - for use in teaching, academic research, and meeting
// course requirements at degree granting institutions only.  Not for
// government, commercial, or other organizational use.
// File: ServiceServer.h
//
// MATLAB Coder version            : 5.6
// C/C++ source code generated on  : 31-Aug-2023 18:25:47
//

#ifndef SERVICESERVER_H
#define SERVICESERVER_H

// Include Files
#include "rtwtypes.h"
#include "undistort_point_service_types.h"
#include "mlroscpp_svcserver.h"
#include <cstddef>
#include <cstdlib>

// Type Definitions
namespace coder {
namespace ros {
class ServiceServer {
public:
  void callback();
  ServiceServer *init();
  char ServiceName[20];
  char RequestType[26];

private:
  experiments_exampleRequestStruct_T ReqMsgStruct;
  experiments_exampleResponseStruct_T RespMsgStruct;
  std::unique_ptr<MATLABSvcServer<
      experiments::exampleRequest, experiments::exampleResponse,
      experiments_exampleRequestStruct_T, experiments_exampleResponseStruct_T>>
      SvcServerHelper;
  bool IsInitialized;
};

} // namespace ros
} // namespace coder

#endif
//
// File trailer for ServiceServer.h
//
// [EOF]
//
