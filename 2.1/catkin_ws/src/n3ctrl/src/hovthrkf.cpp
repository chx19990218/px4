#include "hovthrkf.h"
#include <iostream>
#include <uav_utils/utils.h>


HovThrKF::HovThrKF(Parameter_t& param_) : param(param_) {
}

void HovThrKF::init() {
    double mass = param.mass;
    double max_force = param.full_thrust;

    // to ensure init this after param is inited.
    ROS_ASSERT_MSG(mass > 0.1 && max_force > 9.8, "mass=%f max_force=%f", mass, max_force);

    x = Vector2d(0.0, 0.0);
    P = Matrix<double, 2, 2>();
    P << 0.01 * 0.01, 0, 0, 0.01 * 0.01;
    Q = Matrix<double, 2, 2>();
    Q << 0.001 * 0.001, 0, 0, 0.05 * 0.05;
    F = Matrix<double, 2, 2>();
    F << 1, 0, -max_force / mass, 0;
    B = Matrix<double, 2, 1>();
    B << 0, max_force / mass;
    H = Matrix<double, 1, 2>();
    H << 0, 1;
    R = Matrix<double, 1, 1>();
    R << 0.8 * 0.8;
}

void HovThrKF::process(double u) {
    // printf("u = %f\n", u);
    // printf("pro: x- = %10.3f %10.3f\n",x(0), x(1));
    x = F * x + B * u;
    P = F * P * F.transpose() + Q;
    // printf("pro: x+ = %10.3f %10.3f\n",x(0), x(1));
    // limit_range(x(0), 0.5, 0.9);
}

void HovThrKF::update(double a) {
    // printf("******\na = %f\n", a);
    Matrix<double, 1, 1> z;
    z << a - 9.8;
    MatrixXd y = z - H * x;
    Vector2d k = P * H.transpose() * (H * P * H.transpose() + R).inverse();
    // printf("upd: x- = %10.3f %10.3f\n",x(0), x(1));
    x = x + k * y;
    // printf("upd: x+ = %10.3f %10.3f\n",x(0), x(1));
    P = (Matrix2d::Identity() - k * H) * P;
    // std::cout << "k=" << k.transpose() << endl;
    // printf("hov = %.3f a = %.3f P =[ %5e, %5e;  %5e, %5e]\n---------------------\n",
    // x(0),x(1),P(0,0),P(0,1),P(1,0),P(1,1));
    
    
    uav_utils::limit_range(x(0), param.hover.percent_lower_limit, param.hover.percent_higher_limit);
		param.hov_per = x(0);
		
    if (x(0) == param.hover.percent_lower_limit) {
        ROS_WARN("[n3ctrl.hover] Reach percent_lower_limit %f", x(0));
    }
    if (x(0) == param.hover.percent_higher_limit) {
        ROS_WARN("[n3ctrl.hover] Reach percent_higher_limit %f", x(0));
    }
}

double HovThrKF::get_hov_thr() {
    return x(0);
}

void HovThrKF::set_hov_thr(double hov) {
    x(0) = hov;
}

void HovThrKF::simple_update(Eigen::Quaterniond q, double u, Eigen::Vector3d acc) {

		Matrix3d wRb = q.toRotationMatrix();
		Matrix3d bRw = wRb.transpose();
		
		double weight = 0.98;
		x(0) = x(0)*weight + (1.0-weight)*u*param.gra/acc(2);

//    Vector3d acc_body = acc - bRw * Vector3d(0, 0, param.gra);
//    Vector3d acc_des =
//        Vector3d(0, 0, u * param.full_thrust / param.mass) - bRw * Vector3d(0, 0, param.gra);
//		ROS_INFO("acc_des(2) - acc_body(2):%lf",acc_des(2) - acc_body(2));
//		double compensate;
//		if (std::fabs(acc_des(2) - acc_body(2))<0.1)
//		{
//    	compensate = (acc_des(2) - acc_body(2)) * 0.0001;
//		}
//		else
//		{
//			compensate = (acc_des(2) - acc_body(2)) * 0.0001;
//		}
//    x(0) = x(0) + compensate;



    uav_utils::limit_range(x(0), param.hover.percent_lower_limit, param.hover.percent_higher_limit);
    
    if (x(0) == param.hover.percent_lower_limit) {
        ROS_WARN("[n3ctrl.hover] Reach percent_lower_limit %f", x(0));
    }
    if (x(0) == param.hover.percent_higher_limit) {
        ROS_WARN("[n3ctrl.hover] Reach percent_higher_limit %f", x(0));
    }
}

void HovThrKF::update_hor_k(Eigen::Matrix3d cRw, Eigen::Vector3d des_v, Eigen::Vector3d odom_v) {

		Vector3d error_v = cRw * (des_v - odom_v);
		Vector3d delta_error_v = error_v - last_error_v;
		
		Vector3d odom_v_c = cRw * odom_v;
		if(odom_v_c.x()>=0)
		{
			param.hor_x_k += error_v.x() * param.hover.hor_kp + delta_error_v.x() * param.hover.hor_kd * param.ctrl_rate;
		}else
		{
			param.hor_x_k -= error_v.x() * param.hover.hor_kp + delta_error_v.x() * param.hover.hor_kd * param.ctrl_rate;
		}
		if(odom_v_c.y()>=0)
		{
			param.hor_y_k += error_v.y() * param.hover.hor_kp + delta_error_v.y() * param.hover.hor_kd * param.ctrl_rate;
		}else
		{
			param.hor_y_k -= error_v.y() * param.hover.hor_kp + delta_error_v.y() * param.hover.hor_kd * param.ctrl_rate;
		}
		if(odom_v_c.z()>=0)
		{
			param.hor_z_k += error_v.z() * param.hover.hor_kp + delta_error_v.z() * param.hover.hor_kd * param.ctrl_rate;
		}else
		{
			param.hor_z_k -= error_v.z() * param.hover.hor_kp + delta_error_v.z() * param.hover.hor_kd * param.ctrl_rate;
		}

		
		last_error_v = error_v;
		
		uav_utils::limit_range(param.hor_x_k, param.hover.hor_lower_limit, param.hover.hor_higher_limit);
		uav_utils::limit_range(param.hor_y_k, param.hover.hor_lower_limit, param.hover.hor_higher_limit);
		uav_utils::limit_range(param.hor_z_k, param.hover.hor_lower_limit, param.hover.hor_higher_limit);
		
//    if (param.hor_x_k == param.hover.hor_lower_limit) {
//        ROS_WARN("[n3ctrl.hor] Reach hor_x_lower_limit %f", param.hor_x_k);
//    }
//    if (param.hor_x_k == param.hover.hor_higher_limit) {
//        ROS_WARN("[n3ctrl.hor] Reach hor_x_higher_limit %f", param.hor_x_k);
//    }
//    
//    if (param.hor_y_k == param.hover.hor_lower_limit) {
//        ROS_WARN("[n3ctrl.hor] Reach hor_y_lower_limit %f", param.hor_y_k);
//    }
//    if (param.hor_y_k == param.hover.hor_higher_limit) {
//        ROS_WARN("[n3ctrl.hor] Reach hor_y_higher_limit %f", param.hor_y_k);
//    }
}

void HovThrKF::publish_thr() {
    std_msgs::Float64 msg;
    msg.data = get_hov_thr();
    hov_thr_pub.publish(msg);
}
