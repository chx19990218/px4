project(remote_control)
cmake_minimum_required(VERSION 3.1)
add_compile_options(-std=c++11)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake_module)
set(CMAKE_BUILD_TYPE Release)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  roslib
  actionlib
  dynamic_reconfigure #TODO
)
generate_dynamic_reconfigure_options(cfg/dynamic.cfg)#TODO
catkin_package(
  INCLUDE_DIRS
  CATKIN_DEPENDS roscpp std_msgs roslib
)


include_directories(include/)

#云台自稳
add_executable(${PROJECT_NAME}_gimbalStabilize src/gimbalStabilize.cpp)
target_include_directories(${PROJECT_NAME}_gimbalStabilize
  PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${catkin_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME}_gimbalStabilize
  ${catkin_LIBRARIES}
)
add_dependencies(${PROJECT_NAME}_gimbalStabilize ${PROJECT_NAME}_gencfg)
