#ifndef __HOVTHRKF_H
#define __HOVTHRKF_H

#include <Eigen/Dense>
#include <ros/ros.h>
#include <std_msgs/Float64.h>
#include "input.h"
#include <uav_utils/geometry_utils.h>

using namespace Eigen;
using namespace std;

class HovThrKF
{
public:
	Parameter_t& param;
	ros::Publisher hov_thr_pub;

	HovThrKF(Parameter_t&);
	void init();
	void process(double u);
	void update(double a);
	double get_hov_thr();
	void set_hov_thr(double hov);
	void publish_thr();
	void simple_update(Eigen::Quaterniond q, double u, Eigen::Vector3d acc);
	void update_hor_k(Eigen::Matrix3d cRw, Eigen::Vector3d des_v, Eigen::Vector3d odom_v);
	double last_hov_thr;
	
	Vector3d last_error_v;
	
/*	struct record_hov_t*/
/*	{*/
/*		Vector3d acc_body;*/
/*		Vector3d acc_des;*/
/*		double hov_per;*/
/*		Eigen::Quaterniond q*/
/*	};*/
private:
	Eigen::VectorXd x;
	Eigen::MatrixXd P;
	Eigen::MatrixXd Q;
	Eigen::MatrixXd F;
	Eigen::MatrixXd H;
	Eigen::MatrixXd B;
	Eigen::MatrixXd R;
};

#endif
