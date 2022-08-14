cmake_minimum_required(VERSION 3.0.2)
project(cmd_ctrl)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
  quadrotor_msgs
  uav_utils
  Eigen3
)

catkin_package(

)


include_directories(
# include
	${EIGEN3_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
  include
)


add_executable(cmd_node
	src/cmd_node.cpp
	src/cmd_ctrl.cpp
)

target_link_libraries(cmd_node
	${catkin_LIBRARIES}
)


