#ifndef EXPERIMENTS__VISIBILITY_CONTROL_H_
#define EXPERIMENTS__VISIBILITY_CONTROL_H_
#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define EXPERIMENTS_EXPORT __attribute__ ((dllexport))
    #define EXPERIMENTS_IMPORT __attribute__ ((dllimport))
  #else
    #define EXPERIMENTS_EXPORT __declspec(dllexport)
    #define EXPERIMENTS_IMPORT __declspec(dllimport)
  #endif
  #ifdef EXPERIMENTS_BUILDING_LIBRARY
    #define EXPERIMENTS_PUBLIC EXPERIMENTS_EXPORT
  #else
    #define EXPERIMENTS_PUBLIC EXPERIMENTS_IMPORT
  #endif
  #define EXPERIMENTS_PUBLIC_TYPE EXPERIMENTS_PUBLIC
  #define EXPERIMENTS_LOCAL
#else
  #define EXPERIMENTS_EXPORT __attribute__ ((visibility("default")))
  #define EXPERIMENTS_IMPORT
  #if __GNUC__ >= 4
    #define EXPERIMENTS_PUBLIC __attribute__ ((visibility("default")))
    #define EXPERIMENTS_LOCAL  __attribute__ ((visibility("hidden")))
  #else
    #define EXPERIMENTS_PUBLIC
    #define EXPERIMENTS_LOCAL
  #endif
  #define EXPERIMENTS_PUBLIC_TYPE
#endif
#endif  // EXPERIMENTS__VISIBILITY_CONTROL_H_
// Generated 24-Aug-2023 18:55:53
// Copyright 2019-2020 The MathWorks, Inc.
