#include "N3CtrlFSM.h"

using namespace Eigen;
using std::cout;
using std::endl;


void N3CtrlFSM::process_control(const ros::Time& now_time)
{
//	Controller_Output_t u;

	// ROS_WARN("[n3ctrl] state = %d",state); //zxzxzxzx
	// result: state always equals 2
	// ROS_WARN("[n3ctrl] js_ctrl_mode = %d",js_ctrl_mode); //zxzxzxzx
  //! ROS_WARN("ctrl state: %d", state);
	if ((state==JS_CTRL && js_ctrl_mode==JS_CTRL_MODE_FEEDBACK) // JS_CTRL hovering case
		|| (state==CMD_HOVER) // CMD_HOVER case
		|| (state==CMD_CTRL   // CMD_CTRL verticle stationary case
			&& idling_state==NOIDLING // NOT in idling mode
			&& std::fabs(cmd_data.v(2)) < param.hover.vert_velo_limit_for_update
			&& cmd_data.p(2) > param.hover.vert_height_limit_for_update
			&& odom_data.p(2) > param.hover.vert_height_limit_for_update))
	{
		#if 1		
					hov_thr_kf.update(imu_data.a(2));

					// This line may not take effect according to param.hov.use_hov_percent_kf
					param.config_full_thrust(hov_thr_kf.get_hov_thr());

					hov_thr_kf.process(u.thrust);
					hov_thr_kf.publish_thr();
		#else			
					hov_thr_kf.simple_update(odom_data.q, u.thrust, imu_data.a);
					// This line may not take effect according to param.hov.use_hov_percent_kf
					param.config_full_thrust(hov_thr_kf.get_hov_thr());
					hov_thr_kf.publish_thr();
		#endif
	}
//	ROS_INFO("delta_hov_thr:%lf",std::fabs(hov_thr_kf.last_hov_thr-hov_thr_kf.get_hov_thr()));	
//	if (idling_state == NOIDLING&&std::fabs(hov_thr_kf.last_hov_thr-hov_thr_kf.get_hov_thr())>param.delta_hov_percent_threshold)
//	{
//		param.config_full_thrust(hov_thr_kf.get_hov_thr());
//		hov_thr_kf.publish_thr();
//		ROS_INFO("hov_percent is changing,hov_percent:%lf",hov_thr_kf.get_hov_thr());	
//	}else{
//		ROS_INFO("hov_percent stops changing,hov_percent:%lf",hov_thr_kf.get_hov_thr());
//	}
//	hov_thr_kf.last_hov_thr = hov_thr_kf.get_hov_thr();	




	if (state == DIRECT_CTRL)
	{
		process_raw_control(u);
		
		ROS_INFO("DIRECT_CTRL");
		return;
	}	
	else if (state == JS_CTRL)
	{
		if (js_ctrl_mode==JS_CTRL_MODE_RAW)
		{
			ROS_WARN("[n3ctrl] js_ctrl_mode = JS_CTRL_MODE_RAW");//zxzxzxzx
			process_raw_control(u);
		}
		else
		{
			// This function is called when it is running normally. zxzxzxzx
			ROS_INFO("JS_CTRL_FEEDBACK");
			process_js_control(u);
		}
	}
	else if (state == JS_NO_CTRL)
	{
		ROS_WARN("[n3ctrl] state = JS_NO_CTRL");//zxzxzxzx
		process_no_control(u);
	}
	else if (state == JS_RESET_POS_CTRL)
	{
		ROS_INFO("JS_RESET_POS_CTRL");
		process_break_control(u);
	}
	else if (state == CMD_HOVER)
	{
		ROS_INFO("CMD_HOVER");
		process_hover_control(u);
	}
	else if (state == CMD_CTRL)
	{
		//ROS_WARN("[n3ctrl] state = CMD_CTRL");//zxzxzxzx
		ROS_INFO("CMD_CTRL");
		process_cmd_control(u);
	}
	else if (state == CMD_NO_CTRL)
	{
		ROS_INFO("CMD_NO_CTRL");
		process_no_control(u);
	}
	else if (state == CMD_RESET_POS_CTRL)
	{
		ROS_INFO("CMD_RESET_POS_CTRL");
		process_break_control(u);
	}
	else
	{
		ROS_ASSERT(false);
	}

//	if (idling_state != NOIDLING)
//	{
//	  ROS_WARN("idling.");
//		double idling_lasting_time = (now_time - idling_start_time).toSec();
//		process_idling_control(u, u_so3, idling_lasting_time);
//	}

//	controller.publish_so3_ctrl(u_so3, now_time);
	align_with_imu(u);
	controller.publish_ctrl(u, now_time, odom_data.msg.header.stamp);


}

void N3CtrlFSM::process_no_control(Controller_Output_t& u)
{
	u.roll = 0.0;
	u.pitch = 0.0;
	u.yaw = get_yaw_from_odom();
	//! u.thrust = 0.0;
	u.thrust = param.mass * param.gra / param.full_thrust;
  //! u.mode = Controller_Output_t::VERT_VELO;
	u.mode = Controller_Output_t::VERT_THRU;
}

void N3CtrlFSM::process_raw_control(Controller_Output_t& u)
{
	double des_yaw = yaw_add( get_yaw_from_odom(), -(rc_data.yaw * param.rc.yaw_scale));
//	des_yaw = yaw_add( get_yaw_from_odom(), -(rc_data.yaw * param.rc.yaw_scale));
	u.roll  = -(rc_data.roll * param.rc.attitude_scale);
	u.pitch = (rc_data.pitch * param.rc.attitude_scale);
	u.yaw   = des_yaw;
	//! u.thrust = rc_data.thr * param.rc.vert_velo_scale;
	u.thrust = (rc_data.thr + 1)/2.0*0.6;
	//! u.mode = Controller_Output_t::VERT_VELO;
	u.mode = Controller_Output_t::VERT_THRU;
}

void N3CtrlFSM::process_idling_control(Controller_Output_t& u, double idling_lasting_time)
{
	u.roll = 0.0;
	u.pitch = 0.0;
	u.yaw = get_yaw_from_odom();
	if (idling_lasting_time < param.idling.landing_timeout)
	{
		u.thrust = param.mass * param.gra / param.full_thrust * param.idling.landing_thrust_percent;
	}
	else
	{
		u.thrust = param.idling.lowest_thrust;
	}
	u.mode = Controller_Output_t::VERT_THRU;
}


void N3CtrlFSM::process_hover_control(Controller_Output_t& u)
{
//	Desired_State_t des;
	des.p = hover_pose.head<3>();
	des.v = Vector3d::Zero();
	des.yaw = hover_pose(3);
	des.a = Vector3d::Zero();

	controller.update(des, odom_data, u);

	publish_desire(des);
}

void N3CtrlFSM::process_break_control(Controller_Output_t& u)
{
//	Desired_State_t des;
	des.p = odom_data.p;
	des.v = Vector3d::Zero();
	des.yaw = get_yaw_from_odom();
	des.a = Vector3d::Zero();

	controller.update(des, odom_data, u);

	publish_desire(des);
}

void N3CtrlFSM::process_cmd_control(Controller_Output_t& u)
{
//	Desired_State_t des;
	des.p = cmd_data.p;
	des.v = cmd_data.v;
	des.yaw = cmd_data.yaw;
	des.a = cmd_data.a;

	controller.update(des, odom_data, u);

	publish_desire(des);	
}

void N3CtrlFSM::process_js_control(Controller_Output_t& u)
{
//	Desired_State_t des;
//	Vector3d des_v;
//	double des_dyaw;
//	
	get_des_from_js(des_v, des_dyaw);
  ROS_INFO("des_v(x),des_v(y),des_v(z):%lf,%lf,%lf",des_v(0),des_v(1),des_v(2));
	des.a = Vector3d::Zero();

	int axis_id;
	for(axis_id=0; axis_id<3; ++axis_id)
	{
		switch(axis_states[axis_id]) // xy axis
		{
			case FIX:
				des.p(axis_id) = hover_pose(axis_id);
				des.v(axis_id) = 0.0;
				break;
			case MOVE:
				des.p(axis_id) = odom_data.p(axis_id);
				des.v(axis_id) = des_v(axis_id);
				break;
			case BREAK:
				des.p(axis_id) = odom_data.p(axis_id);
				des.v(axis_id) = 0.0;
				break;
			default:
				ROS_ASSERT(false);
		}
	}
//	ROS_INFO("z-state:%lf",axis_states[2]);
	axis_id = 3;
	switch(axis_states[axis_id]) // xy axis
	{
		case FIX:
			des.yaw = hover_pose(axis_id);
			break;
		case MOVE:
			des.yaw = yaw_add(get_yaw_from_odom(), des_dyaw);
			break;
		case BREAK:
			des.yaw = get_yaw_from_odom();        //!TODO 
			break;
		default:
			ROS_ASSERT(false);
	}

  //! ROS_WARN("axis_state (z-y-z-yaw): %d %d %d %d", axis_states[0], axis_states[1], axis_states[2], axis_states[3]);
  //! ROS_INFO("des_p: %lf %lf %lf des_v: %lf %lf %lf des_yaw: %lf", des.p(0), des.p(1), des.p(2), des.v(0), des.v(1), des.v(2), des.yaw);
  //! ROS_INFO("odom_p: %lf %lf %lf odom_v: %lf %lf %lf odom_yaw: %lf", odom_data.p(0), odom_data.p(1), odom_data.p(2), odom_data.v(0),
  //!          odom_data.v(1), odom_data.v(2), get_yaw_from_odom());
	
//	des.p.x() = 0;
//	des.p.y() = 0;
//	des.p.z() = 0.8;
	controller.update(des, odom_data, u); 

	publish_desire(des);
}
