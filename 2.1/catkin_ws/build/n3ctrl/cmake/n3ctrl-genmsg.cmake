# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "n3ctrl: 1 messages, 0 services")

set(MSG_I_FLAGS "-In3ctrl:/home/chx/catkin_ws/src/n3ctrl/msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(n3ctrl_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg" NAME_WE)
add_custom_target(_n3ctrl_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "n3ctrl" "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg" "geometry_msgs/Vector3:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(n3ctrl
  "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/n3ctrl
)

### Generating Services

### Generating Module File
_generate_module_cpp(n3ctrl
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/n3ctrl
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(n3ctrl_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(n3ctrl_generate_messages n3ctrl_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg" NAME_WE)
add_dependencies(n3ctrl_generate_messages_cpp _n3ctrl_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(n3ctrl_gencpp)
add_dependencies(n3ctrl_gencpp n3ctrl_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS n3ctrl_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(n3ctrl
  "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/n3ctrl
)

### Generating Services

### Generating Module File
_generate_module_eus(n3ctrl
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/n3ctrl
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(n3ctrl_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(n3ctrl_generate_messages n3ctrl_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg" NAME_WE)
add_dependencies(n3ctrl_generate_messages_eus _n3ctrl_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(n3ctrl_geneus)
add_dependencies(n3ctrl_geneus n3ctrl_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS n3ctrl_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(n3ctrl
  "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/n3ctrl
)

### Generating Services

### Generating Module File
_generate_module_lisp(n3ctrl
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/n3ctrl
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(n3ctrl_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(n3ctrl_generate_messages n3ctrl_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg" NAME_WE)
add_dependencies(n3ctrl_generate_messages_lisp _n3ctrl_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(n3ctrl_genlisp)
add_dependencies(n3ctrl_genlisp n3ctrl_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS n3ctrl_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(n3ctrl
  "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/n3ctrl
)

### Generating Services

### Generating Module File
_generate_module_nodejs(n3ctrl
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/n3ctrl
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(n3ctrl_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(n3ctrl_generate_messages n3ctrl_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg" NAME_WE)
add_dependencies(n3ctrl_generate_messages_nodejs _n3ctrl_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(n3ctrl_gennodejs)
add_dependencies(n3ctrl_gennodejs n3ctrl_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS n3ctrl_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(n3ctrl
  "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/n3ctrl
)

### Generating Services

### Generating Module File
_generate_module_py(n3ctrl
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/n3ctrl
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(n3ctrl_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(n3ctrl_generate_messages n3ctrl_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chx/catkin_ws/src/n3ctrl/msg/ControllerDebug.msg" NAME_WE)
add_dependencies(n3ctrl_generate_messages_py _n3ctrl_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(n3ctrl_genpy)
add_dependencies(n3ctrl_genpy n3ctrl_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS n3ctrl_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/n3ctrl)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/n3ctrl
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(n3ctrl_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(n3ctrl_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/n3ctrl)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/n3ctrl
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(n3ctrl_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(n3ctrl_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/n3ctrl)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/n3ctrl
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(n3ctrl_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(n3ctrl_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/n3ctrl)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/n3ctrl
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(n3ctrl_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(n3ctrl_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/n3ctrl)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/n3ctrl\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/n3ctrl
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(n3ctrl_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(n3ctrl_generate_messages_py std_msgs_generate_messages_py)
endif()
