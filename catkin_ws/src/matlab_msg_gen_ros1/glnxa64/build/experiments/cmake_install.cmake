# Install script for directory: /home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/experiments/srv" TYPE FILE FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/srv/example.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/experiments/cmake" TYPE FILE FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/build/experiments/catkin_generated/installspace/experiments-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/devel/include/experiments")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/home/andreslopez/.matlab/R2023a/ros1/glnxa64/venv/bin/python3" -m compileall "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/devel/lib/python3/dist-packages/experiments")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/devel/lib/python3/dist-packages/experiments")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/build/experiments/catkin_generated/installspace/experiments.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/experiments/cmake" TYPE FILE FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/build/experiments/catkin_generated/installspace/experiments-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/experiments/cmake" TYPE FILE FILES
    "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/build/experiments/catkin_generated/installspace/experimentsConfig.cmake"
    "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/build/experiments/catkin_generated/installspace/experimentsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/experiments" TYPE FILE FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/include/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/devel/lib/libexperiments_matlab.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libexperiments_matlab.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libexperiments_matlab.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libexperiments_matlab.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/m/" TYPE DIRECTORY FILES "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/m/" FILES_MATCHING REGEX "/[^/]*\\.m$")
endif()

