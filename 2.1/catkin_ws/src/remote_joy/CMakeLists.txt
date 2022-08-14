cmake_minimum_required(VERSION 2.8.3)
project(remote_joy)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  diagnostic_updater
  sensor_msgs
)

catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS sensor_msgs
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(rc_node
  src/rc_node.cpp
)

target_link_libraries(rc_node
  ${catkin_LIBRARIES}
)
