//飞行控制测试1
#include <ros/ros.h>
#include <nlink_parser/LinktrackTagframe0.h>//USB定位
#include <sensor_msgs/BatteryState.h>//电池电量
#include <mavros_msgs/Altitude.h>//海拔
#include <mavros_msgs/State.h>//飞控状态
#include <mavros_msgs/VFR_HUD.h>//地速和风速等
#include <geometry_msgs/PoseStamped.h>//位置指令
#include <sensor_msgs/Imu.h>//IMU状态
#include <mavros_msgs/RCIn.h>//遥控器控制信号原始值(高电平时间,us)
#include <std_msgs/Float64.h>//高度
#include <mavros_msgs/HilGPS.h>


#include "./transform.hpp"
#include "./myApi.hpp"//封装好的各类控制指令


//已经订阅的mavros消息：
//sensor_msgs/BatteryState.h		/mavros/battery					//电池电量
//mavros_msgs/Altitude.h		/mavros/altitude				//海拔
//mavros_msgs/State			/mavros/state					//飞控状态
//mavros_msgs/VFR_HUD.h			/mavros/vfr_hud					//地速和风速等
//sensor_msgs/Imu.h			/mavros/imu/data
//mavros_msgs/RCIn.h			/mavros/rc/in					//遥控器控制信号原始值(高电平时间,us)
//

//其它可以订阅但当前用不到的消息：
//mavros_msgs/EstimatorStatus.h		/mavros/estimator_status
//mavros_msgs/ExtendedState.h		/mavros/extended_state
//sensor_msgs/Imu.h			/mavros/imu/data_raw
//sensor_msgs/MagneticField.h		/mavros/imu/mag
//sensor_msgs/FluidPressure.h		/mavros/imu/static_pressure
//sensor_msgs/Temperature.h		/mavros/imu/temperature_imu
//nav_msgs/Odometry.h			/mavros/local_position/odom
//geometry_msgs/PoseStamped.h		/mavros/local_position/pose
//geometry_msgs/TwistStamped.h		/mavros/local_position/velocity_body
//mavros_msgs/ManualControl.h		/mavros/manual_control/control
//mavros_msgs/RCOut.h			/mavros/rc/out					//控制输出
//mavros_msgs/AttitudeTarget.h		/mavros/setpoint_raw/target_attitude
//sensor_msgs/TimeReference.h		/mavros/time_reference
//mavros_msgs/TimesyncStatus.h		/mavros/timesync_status
//
//
//
//
//
//
//
//
//其它可以发送但当前用不到的消息
//
//
//mavros_msgs/OverrideRCIn		/mavros/rc/override
//
//
//
//
//
//
//
//
//
//
//
//
//

uint16_t ctrlCmd[8] = {};//遥控器控制指令

inline unsigned long long getTimeNsec(void)//获取当前时间（纳秒）
{
	timespec tvNow;
	clock_gettime(CLOCK_REALTIME, &tvNow);//当前时间(从1970.1.1到目前的时间)
	return tvNow.tv_sec * (unsigned long long)1000000000 + tvNow.tv_nsec;
}

double pos3D[3] = {10000000,10000000,10000000};
int posUpdate = 0;
void uwb_subscriber_callback(const nlink_parser::LinktrackTagframe0& msg)//订阅位置信息
{
	//msg.local_time;
	//msg.system_time;
	//msg.voltage;
	//msg.pos_3d[3];
	//msg.eop_3d[3];
	//msg.vel_3d[3];
	//msg.dis_arr[8];
	//msg.angle_3d[3];
	//msg.quaternion[4];//xyzw
	//msg.imu_gyro_3d[3];
	//msg.imu_acc_3d[3];
	//unsigned long long timeuwb = msg.local_time*(unsigned long long)1000000;
	//printf("%d\t%llu\t%llu\r\n", msg.camId[0], timePass, timgImg - timeLast);
	//timeLast = timgImg;
	//printf("UWB: %f\t%f\t%f\r\n", msg.pos_3d[0], msg.pos_3d[1], msg.pos_3d[2]);
	for(int i = 0; i < 3; i++) pos3D[i] = msg.pos_3d[i];
	posUpdate = 1;
}

void battery_subscriber_callback(const sensor_msgs::BatteryState& msg)//订阅电池信息
{
	printf("BAT: %f\t%f\r\n", msg.voltage, msg.current);
	//msg.header.seq;
	//msg.header.stamp.sec;
	//msg.header.stamp.nsec;
	//msg.header.frame_id;
	//msg.voltage;
	//msg.current;
	//msg.capacity;
	//msg.design_capacity;
	//msg.percentage;
	//msg.power_supply_status;
	//msg.power_supply_health;
	//msg.power_supply_technology;
	//msg.present;
	//msg.cell_voltage[];
	//msg.location;
	//msg.serial_number;
}

void altitude_subscriber_callback(const mavros_msgs::Altitude& msg)//订阅海拔信息
{
	//printf("ALT: %f\t%f\r\n",,);
	//msg.header.seq;
	//msg.header.stamp.sec;
	//msg.header.stamp.nsec;
	//msg.header.frame_id;
	//msg.monotonic;
	//msg.amsl;
	//msg.local;
	//msg.relative;
	//msg.terrain;
	//msg.bottom_clearance;
}

void px4state_subscriber_callback(const mavros_msgs::State& msg)//订阅飞控状态信息
{
	//msg.header.seq;
	//msg.header.stamp.sec;
	//msg.header.stamp.nsec;
	//msg.header.frame_id;
	//msg.connected;
	//msg.armed;
	//msg.guided;
	//msg.manual_input;
	//msg.mode;
	//msg.system_status;
}

void vrf_hud_subscriber_callback(const mavros_msgs::VFR_HUD& msg)//订阅地速和风速等信息
{
	//msg.header.seq;
	//msg.header.stamp.sec;
	//msg.header.stamp.nsec;
	//msg.header.frame_id;
	//msg.airspeed;
	//msg.groundspeed;
	//msg.heading;
	//msg.throttle;
	//msg.altitude;
	//msg.climb;
}

void imu_subscriber_callback(const sensor_msgs::Imu& msg)//订阅地速和风速等信息
{
	double x = msg.orientation.x;
	double y = msg.orientation.y;
	double z = msg.orientation.z;
	double w = msg.orientation.w;
	double rx = atan2(2*(w*z+x*y),1-2*(z*z+x*x))*180/3.1415926;
	double ry = asin(2*(w*x-y*z))*180/3.1415926;
	double rz = atan2(2*(w*y+z*x),1-2*(x*x+y*y))*180/3.1415926;
	//printf("%f\t%f\t%f\t%f\t%f\t%f\t%f\r\n", msg.orientation.w, msg.orientation.x, msg.orientation.y, msg.orientation.z, rx, ry, rz);
	//msg.header.seq;
	//msg.header.stamp.sec;
	//msg.header.stamp.nsec;
	//msg.header.frame_id;
	//msg.airspeed;
	//msg.groundspeed;
	//msg.heading;
	//msg.throttle;
	//msg.altitude;
	//msg.climb;
}
//mavros_msgs/RCIn.h			/mavros/rc/in					//遥控器控制信号原始值(高电平时间,us)
void rcIn_subscriber_callback(const mavros_msgs::RCIn& msg)//订阅地速和风速等信息
{
	for(int i = 0; i < 8; i++)
	{
		ctrlCmd[i] = msg.channels[i];
		//printf("%d\t", ctrlCmd[i]);
	}
	//printf("\r\n");
}

double height = 0;
void height_subscriber_callback(const std_msgs::Float64& msg)//订阅地速和风速等信息
{
	height = msg.data;
	//printf("%f\n", height);
}
#include <std_msgs/Float64.h>//高度

int main(int argc, char** argv)
{
	ros::init(argc, argv, "test_control_control1");
	ros::NodeHandle my_node;
	ros::Subscriber uwb_subscriber = my_node.subscribe("/nlink_linktrack_tagframe0",1,&uwb_subscriber_callback);//订阅UWB定位信息
	ros::Subscriber height_subscriber = my_node.subscribe("/serial_gpio/height",1,&height_subscriber_callback);//订阅高度信息
	//ros::Subscriber battery_subscriber = my_node.subscribe("/mavros/battery",1,&battery_subscriber_callback);//订阅电池信息
	//ros::Subscriber altitude_subscriber = my_node.subscribe("/mavros/altitude",1,&altitude_subscriber_callback);//订阅海拔信息
	//ros::Subscriber px4state_subscriber = my_node.subscribe("/mavros/state",1,&px4state_subscriber_callback);//订阅飞控状态信息
	//ros::Subscriber vrf_hud_subscriber = my_node.subscribe("/mavros/vfr_hud",1,&vrf_hud_subscriber_callback);//订阅地速和风速等信息
	//ros::Subscriber imu_subscriber = my_node.subscribe("/mavros/imu/data",1,&imu_subscriber_callback);//订阅IMU信息
	//ros::Subscriber rcIn_subscriber = my_node.subscribe("/mavros/rc/in",1,&rcIn_subscriber_callback);//订阅遥控器控制信号原始值(高电平时间,us)
	ros::Publisher fake_gps_pub = my_node.advertise<mavros_msgs::HilGPS>("/mavros/hil/gps", 10);
	//sendHomePosition(my_node);//设置初始位置(全0)
	int isSetRate = setStreamRate(my_node, 50);//设定数据更新频率
	if(isSetRate != 0) printf("erreo! can't set stream rate\r\n");
	ros::Rate rate(20);
/*
	//设定目标点位置
	ros::Publisher local_pos_pub = my_node.advertise<geometry_msgs::PoseStamped>("mavros/setpoint_position/local", 10);
	geometry_msgs::PoseStamped pose;
	pose.pose.position.x = 0;
	pose.pose.position.y = 0;
	pose.pose.position.z = 2;
	//send a few setpoints before starting
	
	for(int i = 100; ros::ok() && i > 0; --i)
	{
		local_pos_pub.publish(pose);
		ros::spinOnce();
		rate.sleep();
	}
*/
	int timeCnt = -100;
	mavros_msgs::HilGPS fakeGps;
	while(ros::ok())
	{
		rate.sleep();
		ros::spinOnce();
		if(height > 0.001 && posUpdate && pos3D[2] < 0.9)//定位与定高数据就绪，发送伪造GPS数据
		{
			printf("%f\t%f\t%f\r\n", pos3D[0], pos3D[1], height);
			fakeGps.header.stamp = ros::Time::now();
			fakeGps.fix_type = 3;
			fakeGps.geo.latitude = pos3D[0]/40030173.0*180.0+45.7324710;
			fakeGps.geo.longitude = pos3D[1]/40030173.0*180.0/cos(fakeGps.geo.latitude/180*3.1415926)+126.6279384;
			fakeGps.geo.altitude = height;
			fakeGps.eph = 0;
			fakeGps.epv = 0;
			fakeGps.vel = 0;
			fakeGps.vn = 0;
			fakeGps.ve = 0;
			fakeGps.vd = 0;
			fakeGps.cog = 0;
			fake_gps_pub.publish(fakeGps);
			if(++timeCnt== 0)
			{
				//int isArmed = armPlane(my_node);//解锁飞行器（0成功，1失败）
				//if(isArmed == 0) printf("unlock plane\r\n");
				//else printf("erreo! can't unlock plane\r\n");
			}
			if(timeCnt > 100)
			{
			}
		}
	}
	return 0;
while(ros::ok())
{
	rate.sleep();
	ros::spinOnce();
	setPos(my_node, 10, 10, 10);
}
return 0;
	//int isTakeoff = takeoff(my_node);//起飞指令（0成功，1失败）
	//if(isTakeoff == 0) printf("takeoff\r\n");
	//else printf("erreo! can't take off\r\n");
//double yaw = 2;
int loopCnt = 0;
	while(ros::ok())
	{
		rate.sleep();
		ros::spinOnce();
		if(ctrlCmd[0] != 0)
		{
			ctrlCmd[0] = 1500+250*sin(loopCnt / 31.415926);
			ctrlCmd[1] = 1500+250*cos(loopCnt / 31.415926);
			setControl(my_node, ctrlCmd);
			ctrlCmd[0] = 0;
		}
		loopCnt++;
//setPointAttitude(my_node, 0, 0, yaw);
//pose.pose.position.z += 0.05;
//local_pos_pub.publish(pose);
	}
	//ros::spin();
	return 0;
}



