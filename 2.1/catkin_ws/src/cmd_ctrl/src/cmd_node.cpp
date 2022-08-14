#include <ros/ros.h>

#include "cmd_ctrl.h"


int main(int argc, char** argv) 
{
//	cout<<"begin"<<endl;
  ros::init(argc, argv, "cmd_ctrl");
  ros::NodeHandle nh;
  ros::Duration(1.0).sleep();
  ros::Rate rate(200.0);
  CMD cmd;
  cmd.cmd_pub = nh.advertise<quadrotor_msgs::PositionCommand>("/uav0/cmd",
                                     10);
  cmd.target_pub = nh.advertise<nav_msgs::Odometry>("/uav0/target",
                                     10);
  cmd.odom_sub = nh.subscribe<nav_msgs::Odometry>("/uav0/odom",
                                       1000,
                                       boost::bind(&CMD::get_odom, &cmd, _1),
                                       ros::VoidConstPtr(),
                                       ros::TransportHints().tcpNoDelay());
  while (ros::ok()) 
  {
    rate.sleep();
    ros::spinOnce();
    cmd.process();
  }
  return 0;
}
