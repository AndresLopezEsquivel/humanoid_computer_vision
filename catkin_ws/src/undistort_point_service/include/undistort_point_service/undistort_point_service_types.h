//
// Academic License - for use in teaching, academic research, and meeting
// course requirements at degree granting institutions only.  Not for
// government, commercial, or other organizational use.
// File: undistort_point_service_types.h
//
// MATLAB Coder version            : 5.6
// C/C++ source code generated on  : 31-Aug-2023 18:25:47
//

#ifndef UNDISTORT_POINT_SERVICE_TYPES_H
#define UNDISTORT_POINT_SERVICE_TYPES_H

// Include Files
#include "rtwtypes.h"

// Type Definitions
struct experiments_exampleRequestStruct_T {
  char MessageType[26];
  double XDist;
  double YDist;
};

struct experiments_exampleResponseStruct_T {
  char MessageType[27];
  double XUndis;
  double YUndis;
};

#endif
//
// File trailer for undistort_point_service_types.h
//
// [EOF]
//
