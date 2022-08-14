//飞行控制测试1
#include <ros/ros.h>
#include <nlink_parser/LinktrackTagframe0.h>//USB定位
#include <std_msgs/Float64.h>//高度
#include <mavros_msgs/HilGPS.h>
#include "./myApi.hpp"

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
	ros::Publisher fake_gps_pub = my_node.advertise<mavros_msgs::HilGPS>("/mavros/hil/gps", 10);//发送伪造GPS信息
	int isSetRate = setStreamRate(my_node, 50);//设定数据更新频率
	if(isSetRate != 0) printf("erreo! can't set stream rate\r\n");
	ros::Rate rate(20);
	mavros_msgs::HilGPS fakeGps;
	double posSmooth[2] = {0,0};//位置滤波
	//double speedTemp[3] = {0,0};//临时速度估计
	//double speedSmooth[3] = {0,0};//速度滤波
pos3D[0] = pos3D[1] = pos3D[2] = 0;
	while(ros::ok())
	{
		rate.sleep();
		ros::spinOnce();
//		if(height > 0.001 && posUpdate && pos3D[2] < 0.9)//定位与定高数据就绪，发送伪造GPS数据
		{
			//printf("%f\t%f\t%f\r\n", pos3D[0], pos3D[1], height);
			fakeGps.header.stamp = ros::Time::now();
			double posTemp[2] = {-pos3D[0]*sin(0.52)-pos3D[1]*cos(0.52), -pos3D[0]*cos(0.52)+pos3D[1]*sin(0.52)};
			posSmooth[0] = posSmooth[0] * 0.5 + posTemp[0] * 0.5;
			posSmooth[1] = posSmooth[1] * 0.5 + posTemp[1] * 0.5;
			fakeGps.fix_type = 3;
			fakeGps.geo.latitude = posSmooth[0]/40030173.0*180.0+45.7324710;
			fakeGps.geo.longitude = posSmooth[1]/40030173.0*180.0/cos(fakeGps.geo.latitude/180*3.1415926)+126.6279384;
			fakeGps.geo.altitude = height;
			fakeGps.eph = 1;
			fakeGps.epv = 1;
			fakeGps.vel = 0;
			fakeGps.vn = 0;
			fakeGps.ve = 0;
			fakeGps.vd = 0;
			fakeGps.cog = 0;
			fakeGps.satellites_visible = 12;
			fake_gps_pub.publish(fakeGps);
			//printf("%f\t%f\t%f\t%f\t%f\r\n",posTemp[0],posTemp[1],fakeGps.geo.latitude,fakeGps.geo.longitude,fakeGps.geo.altitude);
		}
	}
	return 0;
}



