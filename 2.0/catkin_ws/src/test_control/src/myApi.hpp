#ifndef __MYAPI__HPP__
#define __MYAPI__HPP__

#include "./transform.hpp"

//测试可用的函数===================================================================================================================
#include <mavros_msgs/CommandBool.h>//解锁指令
int armPlane(ros::NodeHandle &my_node)//解锁飞行器（0成功，1失败）
{
	//控制无人机解锁
	ros::ServiceClient arming_client = my_node.serviceClient<mavros_msgs::CommandBool>("/mavros/cmd/arming");//控制解锁
	mavros_msgs::CommandBool arm_cmd;
	arm_cmd.request.value = true;
 	if(arming_client.call(arm_cmd) && arm_cmd.response.success) return 0;
	else return 1;
}

#include <mavros_msgs/StreamRate.h>//数据更新频率
int setStreamRate(ros::NodeHandle &my_node, unsigned short frequency)//设定数据更新频率（0成功，1失败）
{
	ros::ServiceClient stream_client = my_node.serviceClient<mavros_msgs::StreamRate>("/mavros/set_stream_rate");//设定数据更新频率
	mavros_msgs::StreamRate streamRate;
	streamRate.request.stream_id = 0;
	streamRate.request.message_rate = frequency;
	streamRate.request.on_off = 1;
	if(stream_client.call(streamRate)) return 0;
	else return 1;
}
//测试中的函数===================================================================================================================
#include <geometry_msgs/PoseStamped.h>
void setPos(ros::NodeHandle &my_node, float x, float y, float z)//设定当前位置(xyz)
{
	geometry_msgs::PoseStamped posPub;
	static ros::Publisher vision_pub;
	static int isFirstTime = 1;
	if(isFirstTime)
	{
		isFirstTime = 0;
		vision_pub = my_node.advertise<geometry_msgs::PoseStamped>("/mavros/vision_pose/pose", 100);
	}
	posPub.pose.position.x = x;
	posPub.pose.position.y = y;
	posPub.pose.position.z = z;
//posPub.pose.orientation.x = q_mocap.x();
//posPub.pose.orientation.y = q_mocap.y();
//posPub.pose.orientation.z = q_mocap.z();
//posPub.pose.orientation.w = q_mocap.w();
        posPub.header.stamp = ros::Time::now();
	vision_pub.publish(posPub);
}

//测试无效的函数===================================================================================================================
#include <mavros_msgs/CommandTOL.h>
int takeoff(ros::NodeHandle &my_node)//起飞指令（0成功，1失败）
{
	//控制无人机起飞
	ros::ServiceClient takeoff_client = my_node.serviceClient<mavros_msgs::CommandTOL>("/mavros/cmd/takeoff");//控制起飞
	mavros_msgs::CommandTOL takeoff_cmd;
	//takeoff_cmd.request.value = true;
 	if(takeoff_client.call(takeoff_cmd) && takeoff_cmd.response.success)//起飞指令发送成功
	{
		return 0;
	}
	else return 1;
}


#include <mavros_msgs/HomePosition.h>//初始位置
void sendHomePosition(ros::NodeHandle &my_node)//设置初始位置(全0)
{
	mavros_msgs::HomePosition homePosition;
	ros::Publisher homePosition_pub = my_node.advertise<mavros_msgs::HomePosition>("/mavros/global_position/home",100);//初始位置发送节点
	homePosition.position.x = 0;//x
	homePosition.position.y = 0;//y
	homePosition.position.z = 0;//z
	homePosition.orientation.x = 1;//x
	homePosition.orientation.y = 0;//y
	homePosition.orientation.z = 0;//z
	homePosition.orientation.w = 0;//w
	homePosition.approach.x = 0;//x
	homePosition.approach.y = 0;//y
	homePosition.approach.z = 0;//z
	homePosition_pub.publish(homePosition);
}

#include <geometry_msgs/PoseStamped.h>
void setPointAttitude(ros::NodeHandle &my_node, float r, float p, float y)//设定角度(roll滚转,pitch俯仰,yaw偏航)
{
	geometry_msgs::PoseStamped poseCmd;
	static ros::Publisher attitude_pub;
	static int isFirstTime = 1;
	if(isFirstTime)
	{
		isFirstTime = 0;
		attitude_pub = my_node.advertise<geometry_msgs::PoseStamped>("/mavros/setpoint_attitude/attitude",100);//初始位置发送节点
	}
HITCHC_transform::Quaternion q;
HITCHC_transform::Euler e;
e.e[0] = r;
e.e[1] = p;
e.e[2] = y;
HITCHC_transform::eulerXYZToQuaternion(&e, &q);
	poseCmd.pose.orientation.x = q.q[1];
	poseCmd.pose.orientation.y = q.q[2];
	poseCmd.pose.orientation.z = q.q[3];
	poseCmd.pose.orientation.w = q.q[0];
	attitude_pub.publish(poseCmd);
}

#include <mavros_msgs/OverrideRCIn.h>
void setControl(ros::NodeHandle &my_node, uint16_t channels[8])//设定遥控器数据(固定8通道uint16_t类型)(1000~2500)
{
	mavros_msgs::OverrideRCIn ctrlCmd;
	static ros::Publisher ctrl_pub;
	static int isFirstTime = 1;
	if(isFirstTime)
	{
		isFirstTime = 0;
		ctrl_pub = my_node.advertise<mavros_msgs::OverrideRCIn>("/mavros/rc/override",100);//初始位置发送节点
	}
	for(int i = 0; i < 8; i++) ctrlCmd.channels[i] = channels[i];
	ctrl_pub.publish(ctrlCmd);
}


#endif

