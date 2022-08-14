#ifndef __CONTROLLER_H
#define __CONTROLLER_H

#include <std_msgs/Header.h>
#include <sensor_msgs/Imu.h>
#include <uav_utils/geometry_utils.h>
#include <geometry_msgs/QuaternionStamped.h>
#include <geometry_msgs/WrenchStamped.h>

#include "input.h"
#include "hovthrkf.h"

struct Desired_State_t
{
	Eigen::Vector3d p;
	Eigen::Vector3d v;
	double yaw;
	Eigen::Quaterniond q;
	Eigen::Vector3d a;
};

struct Controller_Output_t
{
	static constexpr double VERT_VELO = -1.0;
	static constexpr double VERT_THRU = 1.0;

	// static constexpr double CTRL_YAW_RATE = -1.0; //zxzxzxzx
  //    static constexpr double CTRL_YAW = 1.0;
  static constexpr double CTRL_YAW_RATE = 1.0;
  static constexpr double CTRL_YAW = 0.0;

	double roll;
	double pitch;
	double yaw;
	double thrust;
	double mode; // if mode > 0, thrust = 0~100%;
				// if mode < 0, thrust = -? m/s ~ +? m/s
	double yaw_mode; // if yaw_mode > 0, CTRL_YAW;
				// if yaw_mode < 0, CTRL_YAW_RATE
};

struct Eso_t{
	double inter;
	double b0;
	double w0;
	Eigen::MatrixXd Ak;
	Eigen::MatrixXd Bk;
	
	init();
};

class Controller
{
public:
	Parameter_t& param;
	HovThrKF& hov_thr_kf;
	
	Eso_t eso;
	ros::Publisher ctrl_pub;
	// ros::Publisher ctrl_so3_pub;
/*	ros::Publisher ctrl_so3_attitude_pub;*/
/*	ros::Publisher ctrl_so3_thrust_pub;*/
	ros::Publisher ctrl_vis_pub;
	ros::Publisher ctrl_dbg_pub;
	ros::Publisher ctrl_val_dbg_pub;
	ros::Publisher ctrl_dbg_p_pub;
	ros::Publisher ctrl_dbg_v_pub;
	ros::Publisher ctrl_dbg_a_pub;
	ros::Publisher ctrl_dbg_att_des_pub;
	ros::Publisher ctrl_dbg_att_real_pub;

	Eigen::Matrix3d Kp;
	Eigen::Matrix3d Kpd;
	Eigen::Matrix3d Kv;
	Eigen::Matrix3d Kvi;
	Eigen::Matrix3d Kvd;
	Eigen::Matrix3d Ka;
	Eigen::Vector3d delta_e_v_smooth;
	Eigen::Vector3d delta_e_p_smooth;
	double Kyaw;

	Eigen::Vector3d int_e_v;
	Eigen::Vector3d prev_e_v;
	Eigen::Vector3d prev_e_p;


	Controller(Parameter_t&, HovThrKF&);
	void config_gain(const Parameter_t::Gain& gain);
	void config();
	void update(Desired_State_t& des, const Odom_Data_t& odom,Controller_Output_t& u);
	
	void output_visualization(const Controller_Output_t& u);
	void publish_ctrl(const Controller_Output_t& u, const ros::Time& stamp, const ros::Time& extra_stamp);

private:
	bool is_configured;
};

#endif
