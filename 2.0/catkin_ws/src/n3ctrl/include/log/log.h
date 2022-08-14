#ifndef __LOG_H
#define __LOG_H

#include <ros/ros.h>
#include <fstream>
#include <sstream>
#include <iostream>
#include <time.h>


#include "input.h"
#include "controller.h"
#include "hovthrkf.h"
#include "N3CtrlParam.h"


using namespace std;
using namespace uav_utils;

struct flightlog_t
{
/*	ofstream log_t;*/
	ofstream log_p_x;
	ofstream log_p_y;
	ofstream log_p_z;
	ofstream log_v_x;
	ofstream log_v_y;
	ofstream log_v_z;
	ofstream log_yaw;
	ofstream log_u_roll;
	ofstream log_u_pitch;
	ofstream log_u_yaw;
	ofstream log_u_thr;
	ofstream log_hovper;
	ofstream log_t;
	ofstream log_acc_x;
	ofstream log_acc_y;
	ofstream log_acc_z;
	ofstream log_q;
	ofstream log_odom_q;
};

class Logger {
  public:
		Parameter_t& param;
		std::stringstream create_time;
		flightlog_t flightlog;
		string folderPath;

		Logger(Parameter_t&);
		void record_log(const ros::Duration& now_time,const Desired_State_t& des,const Odom_Data_t& odom_data, 
										const Controller_Output_t& u,const RC_Data_t& rc_data,const Imu_Data_t& imu_data,const double& hovper);

};
#endif
