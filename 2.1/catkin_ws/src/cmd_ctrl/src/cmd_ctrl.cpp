#include "cmd_ctrl.h"
using namespace std;
//CMD::CMD(ros::NodeHandle& nh_)
//  : nh(nh_)
CMD::CMD()
{
	init_flag = false;
	cmd_p(0) = 0;
	cmd_p(1) = 0;
	cmd_p(2) = 1;
	
	cmd_v(0) = 0;
	cmd_v(1) = 0;
	cmd_v(2) = 0;
	
	cmd_a(0) = 0;
	cmd_a(0) = 0;
	cmd_a(0) = 0;
	
	start_time = ros::Time::now();
	trajectory_id = 0;
	trajectory_flag = quadrotor_msgs::PositionCommand::TRAJECTORY_STATUS_EMPTY;
}
void CMD::process()
{
	now_time = ros::Time::now();
	if(self_lmpc_init())
	{
		if ((now_time - rcv_stamp).toSec() < 0.5) {
        if (odom_data.child_frame_id.size() > 0) {
            odom_state = true;
        } else {
            odom_state = false;
            ROS_WARN("Odom data mistake");
        }
    } else {
        odom_state = false;
        ROS_WARN("Odom timeout for cmd!");
    }
		if(odom_state)
		
		{
			get_ref_trajectory();
			self_lmpc();
			
			trajectory_id++;
			trajectory_flag = quadrotor_msgs::PositionCommand::TRAJECTORY_STATUS_READY;
		}
		publish_cmd();
	}
}
void CMD::get_rectangle(Eigen::Vector3d& pt, Eigen::Vector3d& vt, double flight_t, double v, double r)
{
	double once_time = 4 * r/v;
	double relate_time = flight_t/once_time - (int)(flight_t/once_time);
//	std::cout << relate_time << std::endl;
	if(relate_time < 0.25)
	{
		pt.x() = -r/2;
		pt.y() = r/2 - v * (relate_time - 0.0) * once_time;
		vt.x() = 0;
		vt.y() = -v;
	}else if(relate_time >= 0.25 & relate_time <= 0.5)
	{
		pt.x() = -r/2 + v * (relate_time - 0.25) * once_time;
		pt.y() = -r/2;
		vt.x() = v;
		vt.y() = 0;
	}else if(relate_time >= 0.5 & relate_time <= 0.75)
	{
		pt.x() = r/2;
		pt.y() = -r/2 + v * (relate_time - 0.5) * once_time;
		vt.x() = 0;
		vt.y() = v;
	}else
	{
		pt.x() = r/2 - v * (relate_time  - 0.75) * once_time;
		pt.y() = r/2;
		vt.x() = -v;
		vt.y() = 0;
	}
	pt.z() = 0.6;
	vt.z() = 0;
}
void CMD::get_ref_trajectory()
{
	double flight_t = (now_time - start_time).toSec();
	
	if(false)
	{
		double r = 0.3;
		real_p.x() = r*cos(omega * flight_t);
		real_v.x() = -r*omega*sin(omega * flight_t);
		real_p.y() = r*sin(omega * flight_t);
		real_v.y() = r*omega * cos(omega * flight_t);
		real_p.z() = 0.6;
		real_v.z() = 0;
		
		ref = Eigen::VectorXd::Zero(Np * 2 *2);
		for(int i=0;i<Np;i++)
		{
			ref(4*i) = r*cos(omega * (flight_t + inter * (i + 1)));
			ref(4*i+1) = -r*omega*sin(omega * (flight_t + inter * (i + 1)));
			ref(4*i+2) = r*sin(omega * (flight_t + inter * (i + 1)));
			ref(4*i+3) = r*omega * cos(omega * (flight_t + inter * (i + 1)));
		}
	}
	else
	{
		double v = 0.3;
		double r = 2.0;
		
		get_rectangle(real_p, real_v, flight_t, v, r);
		
		ref = Eigen::VectorXd::Zero(Np * 2 *2);
		for(int i=0;i<Np;i++)
		{
			Eigen::Vector3d refpoint_p;
			Eigen::Vector3d refpoint_v;
			
			double ref_time = flight_t + inter * (i + 1);
			
			get_rectangle(refpoint_p, refpoint_v, ref_time, v, r);
			ref(4*i) = refpoint_p.x();
			ref(4*i+1) = refpoint_v.x();
			ref(4*i+2) = refpoint_p.y();
			ref(4*i+3) = refpoint_v.y();
		}
	}
	
	
}
void CMD::self_lmpc()
{
	Eigen::Vector4d xk0;
	xk0 << p.x(), v.x(), p.y(), v.y();

	U = (PHI.transpose() * PHI +Ru).inverse() * PHI.transpose() * R * (ref - F * xk0);

//	Eigen::Vector4d xk1 = Ak * xk0 + Bk * U.segment(0,2);
	Eigen::VectorXd xk1 = F * xk0 + PHI * U;


//	des_p.x() = xk1(0);
//	des_p.y() = xk1(2);
//	des_p.z() = 1.0;
//	
//	des_v.x() = xk1(1);
//	des_v.y() = xk1(3);
//	des_v.z() = 0;
//	
//	des_a.x() = 0;
//	des_a.y() = 0;
//	des_a.z() = 0;
	
	
	des_p.x() = xk1(0);
	des_p.y() = xk1(2);
	des_p.z() = 0.6;
	
	des_v.x() = xk1(1);
	des_v.y() = xk1(3);
	des_v.z() = 0;
	
//	uav_utils::limit_range(U(0), -1.0, 1.0);
//	uav_utils::limit_range(U(1), -1.0, 1.0);
	
	des_a.x() = U(0);
	des_a.y() = U(1);
	des_a.z() = 0;


//	des_p.x() = real_p.x();
//	des_p.y() = real_p.y();
//	des_p.z() = 1.0;
//	
//	
//	des_v.x() = 0;
//	des_v.y() = 0;
//	des_v.z() = 0;
//	
//	des_a.x() = 0;
//	des_a.y() = 0;
//	des_a.z() = 0;

	std::cout << real_p.x() << "," << real_p.y() << std::endl;
}
bool CMD::self_lmpc_init()
{
	if(!init_flag)
	{
		start_time = ros::Time::now();
		Np = 40;
		Nc = 20;
		inter = 0.1;
		dimension = 2;
		omega = 0.05;
		A = Eigen::Matrix<double, 4, 4>();
		A << 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0;
		
		B = Eigen::Matrix<double, 4, 2>();
		B << 0, 0, 1, 0, 0, 0, 0, 1;

		Rpv = Eigen::Matrix<double, 4, 4>();
		Rpv << 1.0, 0, 0, 0, 0, 0.0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0.0;
		
		row_A = A.rows();
		col_A = A.cols();
		row_B = B.rows();
		col_B = B.cols();
		row_Rpv = Rpv.rows();
		col_Rpv = Rpv.cols();
		
		R.setIdentity(Np*row_Rpv, Np*col_Rpv);
		for(int i=0;i<Np;i++)
		{
			R.block(i*row_Rpv, i*col_Rpv, row_Rpv, col_Rpv) = Rpv;
		}
		
		Ru = 0.0 * Eigen::MatrixXd::Identity(Nc*col_B, Nc*col_B);

		Ak = A * inter + Eigen::MatrixXd::Identity(row_A, col_A);
		Bk = B * inter;
		
		F = Eigen::MatrixXd::Zero(Np*row_A, col_A);
		for(int i=0;i<Np;i++)
		{
			Eigen::MatrixXd Aki = Eigen::MatrixXd::Identity(row_A, col_A);
			for(int j=1;j<=i+1;j++)
			{
				Aki *= Ak;
			} 
			F.block(i*row_A, 0, 4, 4) = Aki;
		}
		
		PHI = Eigen::MatrixXd::Zero(Np*row_A, Nc*col_B);
		for(int i=0;i<Np;i++)
		{
			for(int j=0;j<Nc;j++)
			{
				if(j<=i)
				{
					Eigen::MatrixXd Aki = Eigen::MatrixXd::Identity(row_A, col_A);
					for(int k=1;k<=i-j;k++)
					{
						Aki *= Ak;
					}
					PHI.block(i*row_A, j*col_B, row_A, col_B) = Aki * Bk;
				}
				else
				{
					PHI.block(i*row_A, j*col_B, row_A, col_B) = Eigen::MatrixXd::Zero(row_A, col_B);
				}
			}
		}
		init_flag = true;
		ROS_INFO("Self_lmpc init finished!");
	}
	return true;
}
void CMD::delta_lmpc()
{
	Eigen::Vector3d delta_p = cmd_p - p;
	Eigen::Vector3d delta_v = cmd_v - v;
	if(dimension==2)
	{
		Eigen::Vector4d EX;
		EX << delta_p(1), delta_v(1), delta_p(2), delta_v(2);
		U = (PHI.transpose() * PHI +R).inverse() * PHI.transpose() * F * EX;
		
		Eigen::Vector4d EX_next = Ak * EX + Bk * U.block(0, 0, dimension, 1);
		
		des_p.x() = EX_next(0) + cmd_p(0) + cmd_v(0) * inter;
		des_p.y() = EX_next(2) + cmd_p(1) + cmd_v(1) * inter;
		des_p.z() = 10;
		
		des_v.x() = EX_next(1) + cmd_v(0);
		des_v.y() = EX_next(3) + cmd_v(1);
		des_v.z() = 0;
		
		des_a.x() = U(0);
		des_a.y() = U(1);
		des_a.z() = 0;
	}
	else if(dimension == 3)
	{
		Eigen::VectorXd EX;
		EX << delta_p(1), delta_v(1), delta_p(2), delta_v(2), delta_p(3), delta_v(3);
		U = (PHI.transpose() * PHI +R).inverse() * PHI.transpose() * F * EX;
		
		Eigen::VectorXd EX_next = Ak * EX + Bk * U.block(0, 0, dimension, 1);
		
		des_p.x() = EX_next(0) + cmd_p(0) + cmd_v(0) * inter;
		des_p.y() = EX_next(2) + cmd_p(1) + cmd_v(1) * inter;
		des_p.z() = EX_next(4) + cmd_p(2) + cmd_v(2) * inter;
		
		des_v.x() = EX_next(1) + cmd_v(0);
		des_v.y() = EX_next(3) + cmd_v(1);
		des_v.z() = EX_next(5) + cmd_v(2);
		
		des_a.x() = U(0);
		des_a.y() = U(1);
		des_a.z() = U(2);
	}
	publish_cmd();
}
bool CMD::lmpc_init()
{
	if(init_flag==false)
	{
		Np = 3;
		Nc = 1;
		inter = 0.1;
		dimension = 2;
		row_A = 2 * dimension;
		col_A = 2 * dimension;
		row_B = 2 * dimension;
		col_B = dimension;
		if(dimension == 2)
		{
			A << 0,1,0,0,
				 0,0,0,0,
				 0,0,0,1,
				 0,0,0,0;
			B << 0,0,
					 1,0,
					 0,0,
					 0,1;
		}
		else if(dimension == 3)
		{
			A << 0,1,0,0,0,0,
					 0,0,0,0,0,0,
					 0,0,0,1,0,0,
					 0,0,0,0,0,0,
					 0,0,0,0,0,1,
					 0,0,0,0,0,0;
			B << 0,0,0,
					 1,0,0,
					 0,0,0,
					 0,1,0,
					 0,0,0,
					 0,0,1;
		}
		else
		{
			ROS_ERROR("lmpc init failed: dimension error");
			return false;
		}
		R = Eigen::MatrixXd::Identity(Nc*col_B, Nc*col_B);
		Ak = A * inter + Eigen::MatrixXd::Identity(row_A, col_A);
		Bk = B * inter;
		F = Eigen::MatrixXd::Zero(Np*row_A, col_A);
		for(int i=0;i<Np;i++)
		{
			Eigen::MatrixXd Aki = Eigen::MatrixXd::Identity(row_A, col_A);
			for(int j=1;j<=i+1;j++)
			{
				Aki *= Ak;
			} 
			F.block(i*row_A, 0, 4, 4) = Aki;
		}
		PHI = Eigen::MatrixXd::Zero(Np*row_A, Nc*col_B);
		for(int i=0;i<Np;i++)
		{
			for(int j=0;j<Nc;j++)
			{
				if(j<=i)
				{
					Eigen::MatrixXd Aki(row_A, col_A);
					for(int k=1;k<=i-j;k++)
					{
						Aki *= Ak;
					}
					PHI.block(i*row_A, j*col_B, row_A, col_B) = Aki * Bk;
				}
				else
				{
					PHI.block(i*row_A, j*col_B, row_A, col_B) = Eigen::MatrixXd::Zero(row_A, col_B);
				}
			}
		}
		init_flag = true;
	}
	return true;
}
void CMD::publish_cmd()
{
	quadrotor_msgs::PositionCommand pub1;
	nav_msgs::Odometry pub2;
	
  pub1.position.x = des_p(0);
  pub1.position.y = des_p(1);
  pub1.position.z = des_p(2);

  pub1.velocity.x = des_v(0);
  pub1.velocity.y = des_v(1);
  pub1.velocity.z = des_v(2);

  pub1.acceleration.x = des_a(0);
  pub1.acceleration.y = des_a(1);
  pub1.acceleration.z = des_a(2);
  
  pub2.pose.pose.position.x = real_p.x();
  pub2.pose.pose.position.y = real_p.y();
  pub2.pose.pose.position.z = real_p.z();
  
  pub2.twist.twist.linear.x = real_v.x();
  pub2.twist.twist.linear.y = real_v.y();
  pub2.twist.twist.linear.z = real_v.z();

//  yaw = uav_utils::normalize_angle(msg.yaw);

	pub1.trajectory_id = trajectory_id;
  pub1.trajectory_flag = trajectory_flag;
  cmd_pub.publish(pub1);
  
  target_pub.publish(pub2);
}
void CMD::nmpc()
{
	
}
bool CMD::nmpc_init()
{
	
}
void CMD::get_odom(nav_msgs::OdometryConstPtr pMsg)
{
	rcv_stamp = ros::Time::now();
	odom_data = *pMsg;
	p.x() = pMsg->pose.pose.position.x;
	p.y() = pMsg->pose.pose.position.y;
	p.z() = pMsg->pose.pose.position.z;
	
	v.x() = pMsg->twist.twist.linear.x;
	v.y() = pMsg->twist.twist.linear.y;
	v.z() = pMsg->twist.twist.linear.z;
	
}
