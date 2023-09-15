//
// Academic License - for use in teaching, academic research, and meeting
// course requirements at degree granting institutions only.  Not for
// government, commercial, or other organizational use.
// File: experiments_exampleResponseStruct.cpp
//
// MATLAB Coder version            : 5.6
// C/C++ source code generated on  : 31-Aug-2023 18:25:47
//

// Include Files
#include "experiments_exampleResponseStruct.h"
#include "rt_nonfinite.h"
#include "undistort_point_service_types.h"

// Function Definitions
//
// Message struct definition for experiments/exampleResponse
//
// Arguments    : void
// Return Type  : experiments_exampleResponseStruct_T
//
experiments_exampleResponseStruct_T experiments_exampleResponseStruct()
{
  static const experiments_exampleResponseStruct_T b_msg{
      {'e', 'x', 'p', 'e', 'r', 'i', 'm', 'e', 'n', 't', 's', '/', 'e', 'x',
       'a', 'm', 'p', 'l', 'e', 'R', 'e', 's', 'p', 'o', 'n', 's', 'e'}, // MessageType
      0.0, // XUndis
      0.0  // YUndis
  };
  experiments_exampleResponseStruct_T msg;
  msg = b_msg;
  //(&b_msg);
  return msg;
}

//
// File trailer for experiments_exampleResponseStruct.cpp
//
// [EOF]
//
