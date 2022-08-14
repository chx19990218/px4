#ifndef __CMD_CTRL_H
#define __CMD_CTRL_H

#include <uav_utils/utils.h>
#include <nav_msgs/Odometry.h>
#include <quadrotor_msgs/PositionCommand.h>

#define C_PI (double)3.141592653589793  //! pi

#define DEG2RAD(DEG) ((DEG) * ((C_PI) / (180.0)))
#define RAD2DEG(RAD) ((RAD) * (180.0) / (C_PI))
class CMD
{
	public:
		Eigen::MatrixXd A;
		Eigen::MatrixXd B;
		Eigen::MatrixXd R;
		Eigen::MatrixXd Ru;
		Eigen::MatrixXd Rpv;
		Eigen::MatrixXd Ak;
		Eigen::MatrixXd Bk;
		Eigen::MatrixXd F;
		Eigen::MatrixXd PHI;
		Eigen::VectorXd U;
		Eigen::VectorXd ref;
		double inter;
		int Np;
		int Nc;
		int dimension;
		int row_A;
		int col_A;
		int row_B;
		int col_B;
		int row_Cp;
		int row_Cv;
		int row_Rpv;
		int col_Rpv;
		bool init_flag;
		bool odom_state;
		
		Eigen::Vector3d p;
    Eigen::Vector3d v;

		
		ros::Publisher cmd_pub;
		ros::Publisher target_pub;
		ros::Subscriber odom_sub;
		
		Eigen::Vector3d des_p;
		Eigen::Vector3d des_v;
		Eigen::Vector3d des_a;
		
		Eigen::Vector3d cmd_p;
		Eigen::Vector3d cmd_v;
		Eigen::Vector3d cmd_a;
		
		Eigen::Vector3d real_p;
		Eigen::Vector3d real_v;
		
		ros::Time now_time;
		ros::Time rcv_stamp;
		nav_msgs::Odometry odom_data;
		
		uint32_t trajectory_id;
    uint8_t trajectory_flag;
    ros::Time start_time;
    double omega;
	
		CMD();
		void process();
		void delta_lmpc();
		void self_lmpc();
		bool lmpc_init();
		bool self_lmpc_init();
		void nmpc();
		bool nmpc_init();
		void get_odom(nav_msgs::OdometryConstPtr pMsg);
		void publish_cmd();
		void get_ref_trajectory();
		void get_rectangle(Eigen::Vector3d& pt, Eigen::Vector3d& vt, double flight_t, double v, double r);
};

#endif
