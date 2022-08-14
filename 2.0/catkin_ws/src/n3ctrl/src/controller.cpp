#include "controller.h"
#include <Eigen/Dense>
#include <Eigen/Geometry>
#include <uav_utils/converters.h>
#include <geometry_msgs/Vector3Stamped.h>
#include <geometry_msgs/QuaternionStamped.h>
#include <geometry_msgs/WrenchStamped.h>
#include <boost/format.hpp>
#include <n3ctrl/ControllerDebug.h>

using namespace Eigen;
using std::cout;
using std::endl;
using namespace uav_utils;

Controller::Controller(Parameter_t& param_,HovThrKF& hov_thr_kf_):
	param(param_),hov_thr_kf(hov_thr_kf_)
{
	is_configured = false;

	int_e_v.setZero();
	prev_e_v.setZero();
	prev_e_p.setZero();
}

void Controller::config()
{
	config_gain(param.hover_gain);
	is_configured = true;
}

//Vector3d e_p_int;//TODO:delete
void Controller::config_gain(const Parameter_t::Gain& gain)
{
//e_p_int.setZero();//TODO:delete
	Kp.setZero();
	Kpd.setZero();
	Kv.setZero();
	Kvi.setZero();
	Kvd.setZero();
	Ka.setZero();

	Kp(0,0) = gain.Kp0;
	Kp(1,1) = gain.Kp1;
	Kp(2,2) = gain.Kp2;

	Kpd(0,0) = gain.Kpd0;
	Kpd(1,1) = gain.Kpd1;
	Kpd(2,2) = gain.Kpd2;

	Kv(0,0) = gain.Kv0;
	Kv(1,1) = gain.Kv1;
	Kv(2,2) = gain.Kv2;

	Kvi(0,0) = gain.Kvi0;
	Kvi(1,1) = gain.Kvi1;
	Kvi(2,2) = gain.Kvi2;

	Kvd(0,0) = gain.Kvd0;
	Kvd(1,1) = gain.Kvd1;
	Kvd(2,2) = gain.Kvd2;

	Ka(0,0) = gain.Ka0;
	Ka(1,1) = gain.Ka1;
	Ka(2,2) = gain.Ka2;
	Kyaw = gain.Kyaw;
}

void Controller::update(
	const Desired_State_t& des, 
	const Odom_Data_t& odom, 
	Controller_Output_t& u
)
{
	ROS_INFO("des pose: %lf %lf %lf", des.p.x(), des.p.y(), des.p.z());
	ROS_INFO("des velo: %lf %lf %lf", des.v.x(), des.v.y(), des.v.z());
	ROS_INFO("des orie: %lf", des.yaw);

	ROS_INFO("odom pose: %lf %lf %lf", odom.p.x(), odom.p.y(), odom.p.z());
	ROS_INFO("odom velo: %lf %lf %lf", odom.v.x(), odom.v.y(), odom.v.z());
	ROS_INFO("odom quan: %lf %lf %lf %lf", odom.q.w(), odom.q.x(), odom.q.y(), odom.q.z());
	ROS_INFO("odom orie: %lf", 2*std::atan2(odom.q.z(), odom.q.w()) / M_PI * 180.0 );
	ROS_INFO("hov_percent: %lf", hov_thr_kf.get_hov_thr() );
//	ROS_INFO("Kp: %lf,%lf,%lf", Kp(0,0),Kp(1,1),Kp(2,2));
//	ROS_INFO("Kv: %lf,%lf,%lf", Kv(0,0),Kv(1,1),Kv(2,2));

	ROS_ASSERT_MSG(is_configured, "Gains for controller might not be initialized!");
	std::string constraint_info("");
	Vector3d e_p, e_v, F_des;
	Vector3d u_p_p,u_p_i,u_p_d;
	Vector3d u_v_p,u_v_i,u_v_d;
	double e_yaw = 0.0;

	if (des.v(0) != 0.0 || des.v(1) != 0.0 || des.v(2) != 0.0) {
	  int_e_v.setZero();
	}


	double yaw_curr = get_yaw_from_quaternion(odom.q);
	double	yaw_des = des.yaw;
	Matrix3d wRc = rotz(yaw_curr);
	Matrix3d cRw = wRc.transpose();
//p
	e_p = des.p - odom.p;

	Eigen::Vector3d delta_e_p = (e_p - prev_e_p) * param.ctrl_rate;
	delta_e_p_smooth = delta_e_p_smooth * 0.5 + delta_e_p * 0.5;
	prev_e_p = e_p;

	u_p_p = wRc * Kp * cRw * e_p;
	u_p_d = wRc * Kpd * cRw * delta_e_p_smooth;

	Eigen::Vector3d u_p = u_p_p + u_p_d;

	
//v
	e_v = des.v + u_p - odom.v;
	for (size_t k = 0; k < 3; ++k) 
	{
		if (std::fabs(e_v(k)) < 0.2) 
		{
			int_e_v(k) += e_v(k) * 1.0 / param.ctrl_rate;   //! 50Hx
		}
	}

	Eigen::Vector3d delta_e_v = (e_v - prev_e_v) * param.ctrl_rate;
	delta_e_v_smooth = delta_e_v_smooth * 0.5 + delta_e_v * 0.5;
	prev_e_v = e_v;

	u_v_p = wRc * Kv * cRw * e_v;
	u_v_i = wRc * Kvi * cRw * int_e_v;
	u_v_d = wRc * Kvd * cRw * delta_e_v_smooth;


	const std::vector<double> integration_output_limits_int_e_v = {0.4, 0.4, 0.4};
	for (size_t k = 0; k < 3; ++k) 
	{
		if (std::fabs(u_v_i(k)) > integration_output_limits_int_e_v[k]) 
		{
			uav_utils::limit_range(u_v_i(k), integration_output_limits_int_e_v[k]);
			ROS_INFO("Integration saturate for axis %zu, value=%.3f", k, u_v_i(k));
		}
	}

	Eigen::Vector3d u_v = u_v_p + u_v_i + u_v_d;

//yaw
	e_yaw = yaw_des - yaw_curr;

	while(e_yaw > M_PI) e_yaw -= (2 * M_PI);
	while(e_yaw < -M_PI) e_yaw += (2 * M_PI);

	double u_yaw = Kyaw * e_yaw;
	
//F_des
	F_des = u_v * param.mass + 
		Vector3d(0, 0, param.mass * param.gra) + Ka * param.mass * des.a; //!TODO: Frames be ENU (World) and FLU (Body)
	
	if (F_des(2) < 0.5 * param.mass * param.gra)
	{
		constraint_info = boost::str(
			boost::format("thrust too low F_des(2)=%.3f; ")% F_des(2));
		F_des = F_des / F_des(2) * (0.5 * param.mass * param.gra);
	}
	else if (F_des(2) > 2 * param.mass * param.gra)
	{
		constraint_info = boost::str(
			boost::format("thrust too high F_des(2)=%.3f; ")% F_des(2));
		F_des = F_des / F_des(2) * (2 * param.mass * param.gra);
	}

	if (std::fabs(F_des(0)/F_des(2)) > std::tan(toRad(50.0)))
	{
		constraint_info += boost::str(boost::format("x(%f) too tilt; ")
			% toDeg(std::atan2(F_des(0),F_des(2))));
		F_des(0) = F_des(0)/std::fabs(F_des(0)) * F_des(2) * std::tan(toRad(30.0));
	}

	if (std::fabs(F_des(1)/F_des(2)) > std::tan(toRad(50.0)))
	{
		constraint_info += boost::str(boost::format("y(%f) too tilt; ")
			% toDeg(std::atan2(F_des(1),F_des(2))));
		F_des(1) = F_des(1)/std::fabs(F_des(1)) * F_des(2) * std::tan(toRad(30.0));	
	}


	{	
		Vector3d F_c =wRc.transpose()*F_des;
		Matrix3d wRb_odom = odom.q.toRotationMatrix();
		Vector3d z_b_curr = wRb_odom.col(2);

		double u1 = F_des.dot(z_b_curr); 
		double fx = F_c(0);
		double fy = F_c(1);
		double fz = F_c(2);

		u.roll = std::atan2(-fy, std::sqrt(fx*fx+fz*fz));  //! TODO

                double pitch_bias = -2 / 180 * 3.1415926;

		u.pitch = std::atan2(fx, fz); //! TODO   //! external rotation

		u.thrust = u1 / param.full_thrust;
		uav_utils::limit_range(u.thrust,0.1 ,1.0);
		u.mode = Controller_Output_t::VERT_THRU;
		if(param.use_yaw_rate_ctrl){
			u.yaw_mode = Controller_Output_t::CTRL_YAW_RATE;
			u.yaw = u_yaw;
		}
		else{
			u.yaw_mode = Controller_Output_t::CTRL_YAW;
			u.yaw = des.yaw;
		}
	}

  ROS_INFO("ctrl output: %lf %lf %lf %lf", toDeg(u.roll), toDeg(u.pitch), toDeg(u.yaw), u.thrust);

};

void Controller::publish_ctrl(const Controller_Output_t& u, const ros::Time& stamp, const ros::Time& extra_stamp)
{
	sensor_msgs::Joy msg;

	msg.header.stamp = stamp;
	msg.header.frame_id = std::string("FRD");

	// need to translate to forward-right-down frame
	msg.axes.push_back(toDeg(u.roll));
	msg.axes.push_back(toDeg(u.pitch));
	//! msg.axes.push_back(toDeg(-u.pitch));
	if (u.mode < 0)
	{
		msg.axes.push_back(u.thrust);
	}
	else
	{
		msg.axes.push_back(u.thrust);
	}
	//! msg.axes.push_back(toDeg(-u.yaw));
	msg.axes.push_back(toDeg(u.yaw));
	msg.axes.push_back(u.mode);
	msg.axes.push_back(u.yaw_mode);

	//add time stamp for debug
  msg.buttons.push_back(100000);
  msg.buttons.push_back(extra_stamp.sec/msg.buttons[0]);
  msg.buttons.push_back(extra_stamp.sec%msg.buttons[0]);
  msg.buttons.push_back(extra_stamp.nsec/msg.buttons[0]);
  msg.buttons.push_back(extra_stamp.nsec%msg.buttons[0]);

  ctrl_pub.publish(msg);
  
  ROS_INFO("ctrl publish: %lf %lf %lf %lf", msg.axes[0], msg.axes[1], msg.axes[3], msg.axes[2]);

}

void Controller::output_visualization(const Controller_Output_t& u)
{
	double fn = u.thrust;
	double tan_r = std::tan(u.roll);
	double tan_p = std::tan(u.pitch);
	double fz = std::sqrt(fn*fn/(tan_r*tan_r+tan_p*tan_p+1));
	double fx = fz * tan_p;
	double fy = -fz * tan_r;

	sensor_msgs::Imu msg;
	msg.header.stamp = ros::Time::now();
	msg.header.frame_id = std::string("intermediate");
	msg.linear_acceleration.x = fx;
	msg.linear_acceleration.y = fy;
	msg.linear_acceleration.z = fz;

	ctrl_vis_pub.publish(msg);
};
