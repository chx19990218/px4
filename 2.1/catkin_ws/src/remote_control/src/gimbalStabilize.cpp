//说明：本程序用于对底盘进行扫频，同时尽量保证云台指向不变

#include <stdio.h>
#include <ros/ros.h>
#include <dynamic_reconfigure/server.h>//动态调参
#include <remote_control/dynamicConfig.h>//动态调参


//catkin_make -DCATKIN_WHITELIST_PACKAGES=remote_control

using namespace std;

double decouplingSpeed = 0;
double decouplingAcc = 0;
double decouplingVel = 0;
double decouplingSpeedDelay = 0;
double decouplingAccDelay = 0;
double decouplingVelDelay = 0;
void dynamic_reconfigure_callback(remote_control::dynamicConfig &config)
{
	printf("decouplingSpeed = %f\tdecouplingSpeedDelay = %f\tdecouplingAcc = %f\tdecouplingAccDelay = %f\tdecouplingVel = %f\tdecouplingVelDelay = %f\r\n", 
	config.decouplingSpeed, config.decouplingSpeedDelay, config.decouplingAcc, config.decouplingAccDelay, config.decouplingVel, config.decouplingVelDelay);
	decouplingSpeed = config.decouplingSpeed;
	decouplingSpeedDelay = config.decouplingSpeedDelay;
	decouplingAcc = config.decouplingAcc;
	decouplingAccDelay = config.decouplingAccDelay;
	decouplingVel = config.decouplingVel;
	decouplingVelDelay = config.decouplingVelDelay;
}


int main(int argc, char** argv)
{
	ros::init(argc, argv, "remote_control_freqScanBase");
	ros::NodeHandle my_node;
	dynamic_reconfigure::Server<remote_control::dynamicConfig> server;//动态调参
	server.setCallback(boost::bind(&dynamic_reconfigure_callback, _1));
	ros::Rate rate(100);
	while(ros::ok())
	{
		rate.sleep();
		ros::spinOnce();
	}
}







