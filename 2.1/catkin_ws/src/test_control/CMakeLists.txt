project(test_control)
cmake_minimum_required(VERSION 3.1)
add_compile_options(-std=c++11)

set(CMAKE_BUILD_TYPE Release)
#$find_package(OpenCV 4.1.1 EXACT REQUIRED)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  roslib
  nlink_parser
)
catkin_package(
	INCLUDE_DIRS	
	CATKIN_DEPENDS roscpp std_msgs roslib
)

#数据融合
add_executable(${PROJECT_NAME}_fusion src/fusion.cpp)
target_include_directories(${PROJECT_NAME}_fusion
	PUBLIC 
	${CMAKE_CURRENT_SOURCE_DIR}
	${catkin_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME}_fusion
	${catkin_LIBRARIES}
)
#动作捕捉定位数据
add_executable(${PROJECT_NAME}_vision src/vision.cpp)
target_include_directories(${PROJECT_NAME}_vision
	PUBLIC 
	${CMAKE_CURRENT_SOURCE_DIR}
	${catkin_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME}_vision
	${catkin_LIBRARIES}
)
#控制测试1
add_executable(${PROJECT_NAME}_control1 src/control1.cpp)
target_include_directories(${PROJECT_NAME}_control1
	PUBLIC 
	${CMAKE_CURRENT_SOURCE_DIR}
	${catkin_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME}_control1
	${catkin_LIBRARIES}
)
#控制测试2
add_executable(${PROJECT_NAME}_control2 src/control2.cpp)
target_include_directories(${PROJECT_NAME}_control2
	PUBLIC 
	${CMAKE_CURRENT_SOURCE_DIR}
	${catkin_INCLUDE_DIRS}
)
target_link_libraries(${PROJECT_NAME}_control2
	${catkin_LIBRARIES}
)


