//
// Academic License - for use in teaching, academic research, and meeting
// course requirements at degree granting institutions only.  Not for
// government, commercial, or other organizational use.
// File: undistort_point_service.cpp
//
// MATLAB Coder version            : 5.6
// C/C++ source code generated on  : 31-Aug-2023 18:25:47
//

// Include Files
#include "undistort_point_service.h"
#include "ServiceServer.h"
#include "rt_nonfinite.h"
#include "undistort_point_service_data.h"
#include "undistort_point_service_initialize.h"
#include "coder_posix_time.h"

// Function Definitions
//
// Remember to:
//  rosgenmsg from the dir where you have all your packages
//  clear
//  rosshutdown
//  rosinit
//
// Arguments    : void
// Return Type  : void
//
void undistort_point_service()
{
  coder::ros::ServiceServer testserver;
  coderTimespec b_timespec;
  if (!isInitialized_undistort_point_service) {
    undistort_point_service_initialize();
  }
  testserver.init();
  //  testserver.NewRequestFcn = @serviceCallback;
  while (1) {
    if (pauseState == 0) {
      b_timespec.tv_sec = 0.0;
      b_timespec.tv_nsec = 1.0E+8;
      coderTimeSleep(&b_timespec);
    }
  }
}

//
// File trailer for undistort_point_service.cpp
//
// [EOF]
//
