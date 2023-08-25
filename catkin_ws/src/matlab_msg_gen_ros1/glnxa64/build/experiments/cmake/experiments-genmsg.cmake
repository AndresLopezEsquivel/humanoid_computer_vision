# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "experiments: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/usr/local/MATLAB/R2023a/sys/ros1/glnxa64/ros1/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(experiments_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/srv/example.srv" NAME_WE)
add_custom_target(_experiments_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "experiments" "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/srv/example.srv" ""
)

#
#  langs = gencpp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(experiments
  "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/srv/example.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/experiments
)

### Generating Module File
_generate_module_cpp(experiments
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/experiments
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(experiments_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(experiments_generate_messages experiments_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/srv/example.srv" NAME_WE)
add_dependencies(experiments_generate_messages_cpp _experiments_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(experiments_gencpp)
add_dependencies(experiments_gencpp experiments_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS experiments_generate_messages_cpp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(experiments
  "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/srv/example.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/experiments
)

### Generating Module File
_generate_module_py(experiments
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/experiments
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(experiments_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(experiments_generate_messages experiments_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/andreslopez/Andres/humanoid_computer_vision/catkin_ws/src/matlab_msg_gen_ros1/glnxa64/src/experiments/srv/example.srv" NAME_WE)
add_dependencies(experiments_generate_messages_py _experiments_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(experiments_genpy)
add_dependencies(experiments_genpy experiments_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS experiments_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/experiments)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/experiments
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(experiments_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/experiments)
  install(CODE "execute_process(COMMAND \"/home/andreslopez/.matlab/R2023a/ros1/glnxa64/venv/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/experiments\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/experiments
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(experiments_generate_messages_py std_msgs_generate_messages_py)
endif()
