//飞行控制测试1
#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include "./myApi.hpp"

uint16_t ctrlCmd[8] = {};//遥控器控制指令

inline unsigned long long getTimeNsec(void)//获取当前时间（纳秒）
{
	timespec tvNow;
	clock_gettime(CLOCK_REALTIME, &tvNow);//当前时间(从1970.1.1到目前的时间)
	return tvNow.tv_sec * (unsigned long long)1000000000 + tvNow.tv_nsec;
}
//rostopic type /mavros/vision_pose/pose
//geometry_msgs/PoseStamped
//hitcsc-uav-01@hitcsc-uav-01:~$ rostopic type /mavros/vision_pose/pose_cov
//geometry_msgs/PoseWithCovarianceStamped

int main(int argc, char** argv)
{
	ros::init(argc, argv, "test_control_control1");
	ros::NodeHandle my_node;
	//ros::Subscriber uwb_subscriber = my_node.subscribe("/nlink_linktrack_tagframe0",1,&uwb_subscriber_callback);//订阅UWB定位信息
	//ros::Subscriber height_subscriber = my_node.subscribe("/serial_gpio/height",1,&height_subscriber_callback);//订阅高度信息
	ros::Publisher pose_pub = my_node.advertise<geometry_msgs::PoseStamped>("/mavros/vision_pose/pose", 10);//发送定位信息
	ros::Publisher pose_cov_pub = my_node.advertise<geometry_msgs::PoseWithCovarianceStamped>("/mavros/vision_pose/pose_cov", 10);//发送定位信息
	int isSetRate = setStreamRate(my_node, 50);//设定数据更新频率
	if(isSetRate != 0) printf("erreo! can't set stream rate\r\n");
	ros::Rate rate(20);
	geometry_msgs::PoseStamped pose;
	geometry_msgs::PoseWithCovarianceStamped pose_cov;
	while(ros::ok())
	{
		rate.sleep();
		ros::spinOnce();
		pose.header.stamp = ros::Time::now();
		pose.pose.position.x = ;
		pose.pose.position.y = ;
		pose.pose.position.z = ;
		pose.pose.orientation.x = ;
		pose.pose.orientation.y = ;
		pose.pose.orientation.z = ;
		pose.pose.orientation.w = ;
		pose_cov.header.stamp = ros::Time::now();

		pose_pub.publish(pose);
		pose_cov_pub.publish(pose_cov);
		//printf("%f\t%f\t%f\t%f\t%f\r\n",posTemp[0],posTemp[1],fakeGps.geo.latitude,fakeGps.geo.longitude,fakeGps.geo.altitude);
	}
	return 0;
}



