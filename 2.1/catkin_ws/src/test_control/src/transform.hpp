#ifndef __TRANSFORM_H
#define __TRANSFORM_H

//姿态变换所需函数
//原本为嵌入式开发环境编写，兼容C编译器，也可应用于C++程序中
//这是一套针对初学者和嵌入式应用的姿态计算库，其设计原则为：简洁易懂、高效、跨平台、无依赖、可轻松定制及跨语言移植。
//欧拉角、四元数、旋转矩阵、轴角等表示方式都可以用于表示物体在空间中的姿态，这几种表示方式各有利弊，一套程序中往往需要同时使用多种表达方式。
//然而，如何在不同表示方式之间切换一直是工程中的难点。就定义方面，坐标系分为左手和右手坐标系、欧拉角有12种转序和内外旋的区别、四元数也有Hamilton和JPL两种定义方式，
//而大多数书籍、教程中并未提及这些区别，导致不同书籍、教程间的转换公式难以结合使用，
//而又鲜有单一的书籍、教程能够涉及所有的转换关系，这无疑为初学者提高了学习的门槛。
//各类算法库（如Eigen、Matlab、Google Ceres Solver、Mathematica等）均提供了转换算法，但高度的封装和广泛的依赖项无形中增加了新手学习和移植定制化开发的成本，因而编写该库函数。
//若需要实现更高端的功能，可使用Eigen、Matlab、Google Ceres Solver、Mathematica等。
//程序缺点：调用困难，不优雅
//程序优点：简洁高效、高兼容
//请按照需求选择是否使用本套库函数
//坐标系统一使用右手直角坐标系
//欧拉角统一使用右手内旋
//四元数可选择使用Hamilton定义或JPL定义，通过是否注释宏定义"#define _QUATERNION_HAMILTION"切换
	//注：EIGEN库只能使用Hamilton定义，与惯导等应用场合下的JPL定义方式不同，不可混用
//函数包括：
//1.四元数规范化
//2.旋转矩阵规范化
//3.旋转矩阵转置（求逆）
//4.四元数乘法
//5.旋转矩阵乘法
//6.四元数、欧拉角、旋转矩阵相互转换
#include <math.h>
//#define _USE_EIGEN//启用ENGNE库
#define _QUATERNION_HAMILTION//四元数使用Hamilton定义，否则使用JPL定义



#ifdef _USE_EIGEN
#include <eigen3/Eigen/Core>
#include <eigen3/Eigen/Geometry>
#endif

namespace HITCHC_transform
{

struct Quaternion//四元数
{
	float q[4];//q[0]+iq[1]+jq[2]+kq[3]
};
struct Euler//欧拉角
{
	float e[3];//e[0]=X(roll),e[1]=Y(pitch),e[2]=Z(yaw)
};
struct Matrix3x3//旋转矩阵
{
	float m[3][3];//[rows][cols]
};
struct Matrix4x4//齐次变换矩阵
{
	float m[4][4];//[rows][cols]
};
/**
 * @brief	四元数规范化
 * @param	q 需要规范化的四元数
 */
void quaternionNormalize(Quaternion *q)
{
	float normR = 1.0f / sqrt(q->q[0] * q->q[0] + q->q[1] * q->q[1] + q->q[2] * q->q[2] + q->q[3] * q->q[3]);
	q->q[0] = q->q[0] * normR;
	q->q[1] = q->q[1] * normR;
	q->q[2] = q->q[2] * normR;
	q->q[3] = q->q[3] * normR;
}
/**
 * @brief	旋转矩阵规范化
 * @param	m 需要规范化的旋转矩阵
 */
void matrix3x3Normalize(Matrix3x3 *m)//TODO：未完成
{
	for(int i = 0; i < 3; i++)
	{
		for(int j = 0; j < 3; j++)
		{
			m->m[0][0];
		}
	}
	
}
#ifdef _USE_EIGEN
void matrix3x3Normalize_Eigen(Matrix3x3 *m)//TODO：未完成
{
	Eigen::Matrix3f rotation_matrix3;
	rotation_matrix3 << m->m[0][0], m->m[0][1], m->m[0][2], m->m[1][0], m->m[1][1], m->m[1][2], m->m[2][0], m->m[2][1], m->m[2][2];
	//rotation_matrix3.
}
#endif

/**
 * @brief	旋转矩阵转置（求逆）
 * @param	m 需要转置的旋转矩阵
 */
void matrix3x3Transpose(Matrix3x3 *m)
{
	float temp;
	temp = m->m[1][0];
	m->m[1][0] = m->m[0][1];
	m->m[0][1] = temp;
	temp = m->m[2][0];
	m->m[2][0] = m->m[0][2];
	m->m[0][2] = temp;
	temp = m->m[2][1];
	m->m[2][1] = m->m[1][2];
	m->m[1][2] = temp;
}
/**
 * @brief	四元数乘法
 * @param	qIn1 输入四元数1
 * @param	qIn2 输入四元数2
 * @param	qOut 输出四元数
 * @note	qOut=qIn1*qIn2
 */
void quaternionMultiply(Quaternion *qIn1, Quaternion *qIn2, Quaternion *qOut)
{
	float q0 = qIn1->q[0] * qIn2->q[0] - qIn1->q[1] * qIn2->q[1] - qIn1->q[2] * qIn2->q[2] - qIn1->q[3] * qIn2->q[3];
	float q1 = qIn1->q[1] * qIn2->q[0] + qIn1->q[0] * qIn2->q[1] + qIn1->q[3] * qIn2->q[2] - qIn1->q[2] * qIn2->q[3];
	float q2 = qIn1->q[2] * qIn2->q[0] + qIn1->q[0] * qIn2->q[2] + qIn1->q[1] * qIn2->q[3] - qIn1->q[3] * qIn2->q[1];
	float q3 = qIn1->q[3] * qIn2->q[0] + qIn1->q[0] * qIn2->q[3] + qIn1->q[2] * qIn2->q[1] - qIn1->q[1] * qIn2->q[2];
	qOut->q[0] = q0;
	qOut->q[1] = q1;
	qOut->q[2] = q2;
	qOut->q[3] = q3;
}
#ifdef _USE_EIGEN
void quaternionMultiply_Eigen(Quaternion *qIn1, Quaternion *qIn2, Quaternion *qOut)
{
	Eigen::Quaternionf q1(qIn1->q[0],qIn1->q[1],qIn1->q[2],qIn1->q[3]);
	Eigen::Quaternionf q2(qIn2->q[0],qIn2->q[1],qIn2->q[2],qIn2->q[3]);
	Eigen::Quaternionf q3 = q1 * q2;
	qOut->q[0] = q3.coeffs()[3];//real
	qOut->q[1] = q3.coeffs()[0];//i
	qOut->q[2] = q3.coeffs()[1];//j
	qOut->q[3] = q3.coeffs()[2];//k
}
#endif

/**
 * @brief	旋转矩阵乘法
 * @param	mIn1 输入旋转矩阵1
 * @param	mIn2 输入旋转矩阵2
 * @param	mOut 输出旋转矩阵
 * @note	mOut=mIn1*mIn2
 */
void matrix3x3Multiply(Matrix3x3 *mIn1, Matrix3x3 *mIn2, Matrix3x3 *mOut)
{
	int i,j,k;
	float matrixTemp[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
	for(i = 0; i < 3; i++)
		for(j = 0; j < 3; j++)
			for(k = 0; k < 3; k++)
				matrixTemp[i][j] += mIn1->m[i][k] * mIn2->m[k][j];
	for(i = 0; i < 3; i++)
		for(j = 0; j < 3; j++)
			mOut->m[i][j] = matrixTemp[i][j];
}
//===========================================================坐标变换相关===========================================================

//==========================================================四元数转欧拉角==========================================================
/**
 * @brief	四元数转欧拉角
 * @param	qIn 输入四元数
 * @param	eOut 输出欧拉角
 * @note	欧拉角使用XYZ内旋转序(先绕自身X轴旋转，再绕自身Y轴旋转，最后绕自身Z轴旋转)
 */
void quaternionToEulerXYZ(Quaternion *qIn, Euler *eOut)
{
	float w = qIn->q[0];
	float x = qIn->q[1];
	float y = qIn->q[2];
	float z = qIn->q[3];
	#ifdef _QUATERNION_HAMILTION
	eOut->e[0] = atan2(-2*(y*z-w*x),1-2*(x*x+y*y));
	eOut->e[1] = asin(2*(x*z+w*y));
	eOut->e[2] = atan2(-2*(x*y-w*z),1-2*(y*y+z*z));
	#else//TODO：公式有误
	eOut->e[0] = atan2(-2*(w*x+y*z),1-2*(x*x+y*y));
	eOut->e[1] = asin(-2*(w*y-z*x));
	eOut->e[2] = atan2(-2*(w*z+x*y),1-2*(y*y+z*z));
	#endif
}
#ifdef _USE_EIGEN
void quaternionToEulerXYZ_Eigen(Quaternion *qIn, Euler *eOut)
{
	Eigen::Quaternionf q(qIn->q[0],qIn->q[1],qIn->q[2],qIn->q[3]);
	Eigen::Vector3f eulerAngle = q.matrix().eulerAngles(0,1,2);
	eOut->e[0] = eulerAngle.coeff(0);
	eOut->e[1] = eulerAngle.coeff(1);
	eOut->e[2] = eulerAngle.coeff(2);
}
#endif

/**
 * @brief	四元数转欧拉角
 * @param	qIn 输入四元数
 * @param	eOut 输出欧拉角
 * @note	欧拉角使用ZYX内旋转序(先绕自身Z轴旋转，再绕自身Y轴旋转，最后绕自身X轴旋转)
 */
void quaternionToEulerZYX(Quaternion *qIn, Euler *eOut)//TODO：未完成
{
}
#ifdef _USE_EIGEN
void quaternionToEulerZYX_Eigen(Quaternion *qIn, Euler *eOut)//TODO：未测试
{
	Eigen::Quaternionf q(qIn->q[0],qIn->q[1],qIn->q[2],qIn->q[3]);
	Eigen::Vector3f eulerAngle = q.matrix().eulerAngles(2,1,0);
	eOut->e[0] = eulerAngle.coeff(0);
	eOut->e[1] = eulerAngle.coeff(1);
	eOut->e[2] = eulerAngle.coeff(2);
}
#endif

//==========================================================欧拉角转四元数==========================================================
/**
 * @brief	欧拉角转四元数
 * @param	eIn 输入欧拉角rpy
 * @param	qOut 输出四元数xyzw
 * @note	欧拉角使用XYZ内旋转序(先绕自身X轴旋转，再绕自身Y轴旋转，最后绕自身Z轴旋转)
 */
void eulerXYZToQuaternion(Euler *eIn, Quaternion *qOut)
{
	float halfYaw = eIn->e[2] * 0.5f;
	float halfPitch = eIn->e[1] * 0.5f;
	float halfRoll = eIn->e[0] * 0.5f;
	float cosYaw = cos(halfYaw);
	float sinYaw = sin(halfYaw);
	float cosPitch = cos(halfPitch);
	float sinPitch = sin(halfPitch);
	float cosRoll = cos(halfRoll);
	float sinRoll = sin(halfRoll);
	#ifdef _QUATERNION_HAMILTION
	qOut->q[0] = cosRoll * cosPitch * cosYaw - sinRoll * sinPitch * sinYaw;
	qOut->q[1] = sinRoll * cosPitch * cosYaw + cosRoll * sinPitch * sinYaw;
	qOut->q[2] = cosRoll * sinPitch * cosYaw - sinRoll * cosPitch * sinYaw;
	qOut->q[3] = cosRoll * cosPitch * sinYaw + sinRoll * sinPitch * cosYaw;
	#else//TODO：公式有误
	qOut->q[0] = cosRoll * cosPitch * cosYaw - sinRoll * sinPitch * sinYaw;
	qOut->q[1] = -cosRoll * sinPitch * sinYaw - sinRoll * cosPitch * cosYaw;
	qOut->q[2] = sinRoll * cosPitch * sinYaw - cosRoll * sinPitch * cosYaw;
	qOut->q[3] = -cosRoll * cosPitch * sinYaw - sinRoll * sinPitch * cosYaw;
	#endif
}
#ifdef _USE_EIGEN
void eulerXYZToQuaternion_Eigen(Euler *eIn, Quaternion *qOut)
{
	Eigen::Quaternionf quaternion = Eigen::AngleAxisf(eIn->e[0], ::Eigen::Vector3f::UnitX()) *
	Eigen::AngleAxisf(eIn->e[1], ::Eigen::Vector3f::UnitY()) *
	Eigen::AngleAxisf(eIn->e[2], ::Eigen::Vector3f::UnitZ());
	qOut->q[0] = quaternion.coeffs()[3];//real
	qOut->q[1] = quaternion.coeffs()[0];//i
	qOut->q[2] = quaternion.coeffs()[1];//j
	qOut->q[3] = quaternion.coeffs()[2];//k
}
#endif

//=========================================================四元数转旋转矩阵=========================================================
/**
 * @brief	四元数转旋转矩阵
 * @param	qIn 输入四元数
 * @param	mOut 输出旋转矩阵
 */
void quaternionToMatrix3x3(Quaternion *qIn, Matrix3x3 *mOut)
{
	#ifdef _QUATERNION_HAMILTION
	float tx = 2*qIn->q[1];
	float ty = 2*qIn->q[2];
	float tz = 2*qIn->q[3];
	float twx = tx*qIn->q[0];
	float twy = ty*qIn->q[0];
	float twz = tz*qIn->q[0];
	float txx = tx*qIn->q[1];
	float txy = ty*qIn->q[1];
	float txz = tz*qIn->q[1];
	float tyy = ty*qIn->q[2];
	float tyz = tz*qIn->q[2];
	float tzz = tz*qIn->q[3];
	mOut->m[0][0] = 1-(tyy+tzz);
	mOut->m[0][1] = txy-twz;
	mOut->m[0][2] = txz+twy;
	mOut->m[1][0] = txy+twz;
	mOut->m[1][1] = 1-(txx+tzz);
	mOut->m[1][2] = tyz-twx;
	mOut->m[2][0] = txz-twy;
	mOut->m[2][1] = tyz+twx;
	mOut->m[2][2] = 1-(txx+tyy);
	#else
	float tx = 2*qIn->q[1];
	float ty = 2*qIn->q[2];
	float tz = 2*qIn->q[3];
	float twx = tx*qIn->q[0];
	float twy = ty*qIn->q[0];
	float twz = tz*qIn->q[0];
	float txx = tx*qIn->q[1];
	float txy = ty*qIn->q[1];
	float txz = tz*qIn->q[1];
	float tyy = ty*qIn->q[2];
	float tyz = tz*qIn->q[2];
	float tzz = tz*qIn->q[3];
	mOut->m[0][0] = 1-(tyy+tzz);
	mOut->m[0][1] = txy+twz;
	mOut->m[0][2] = txz-twy;
	mOut->m[1][0] = txy-twz;
	mOut->m[1][1] = 1-(txx+tzz);
	mOut->m[1][2] = tyz+twx;
	mOut->m[2][0] = txz+twy;
	mOut->m[2][1] = tyz-twx;
	mOut->m[2][2] = 1-(txx+tyy);
	#endif
}
#ifdef _USE_EIGEN
void quaternionToMatrix3x3_Eigen(Quaternion *qIn, Matrix3x3 *mOut)
{
	Eigen::Quaternionf quaternion(qIn->q[0],qIn->q[1],qIn->q[2],qIn->q[3]);
	Eigen::Matrix3f rotation_matrix3 = quaternion.matrix();
	for(int i = 0; i < 3; i++)
		for(int j = 0; j < 3; j++)
			mOut->m[i][j] = rotation_matrix3.coeff(i,j);//(row,col)
}
#endif

//=========================================================旋转矩阵转四元数=========================================================
/**
 * @brief	旋转矩阵转四元数
 * @param	mIn 输入旋转矩阵
 * @param	qOut 输出四元数
 */
void matrix3x3ToQuaternion(Matrix3x3 *mIn, Quaternion *qOut)
{
	float t = mIn->m[0][0] + mIn->m[1][1] + mIn->m[2][2];
	if(t >= 0)//得到四元数的实部最大
	{
		#ifdef _QUATERNION_HAMILTION
		t = sqrt(t + 1);
		qOut->q[0] = t * 0.5f;
		t = 0.5f / t;
		qOut->q[1] = (mIn->m[2][1] - mIn->m[1][2]) * t;
		qOut->q[2] = (mIn->m[0][2] - mIn->m[2][0]) * t;
		qOut->q[3] = (mIn->m[1][0] - mIn->m[0][1]) * t;
		#else
		t = sqrt(t + 1);
		qOut->q[0] = t * 0.5f;
		t = 0.5f / t;
		qOut->q[1] = (mIn->m[1][2] - mIn->m[2][1]) * t;
		qOut->q[2] = (mIn->m[2][0] - mIn->m[0][2]) * t;
		qOut->q[3] = (mIn->m[0][1] - mIn->m[1][0]) * t;
		#endif
	}
	else//得到的四元数某个虚部最大
	{
		int i = 0;
		if(mIn->m[1][1] > mIn->m[0][0]) i = 1;
		if(mIn->m[2][2] > mIn->m[i][i]) i = 2;
		int j = (i + 1) % 3;
		int k = (j + 1) % 3;
		t = sqrt(mIn->m[i][i] - mIn->m[j][j] - mIn->m[k][k] + 1.0f);
		qOut->q[i+1] = 0.5f * t;
		t = 0.5f / t;
		#ifdef _QUATERNION_HAMILTION
		qOut->q[0] = (mIn->m[k][j]-mIn->m[j][k]) * t;
		qOut->q[j+1] = (mIn->m[j][i]+mIn->m[i][j]) * t;
		qOut->q[k+1] = (mIn->m[k][i]+mIn->m[i][k]) * t;
		#else
		qOut->q[0] = (mIn->m[j][k]-mIn->m[k][j]) * t;
		qOut->q[j+1] = (mIn->m[i][j]-mIn->m[j][i]) * t;
		qOut->q[k+1] = (mIn->m[i][k]-mIn->m[k][i]) * t;
		#endif
	}
}
#ifdef _USE_EIGEN
void matrix3x3ToQuaternion_Eigen(Matrix3x3 *mIn, Quaternion *qOut)
{
	Eigen::Matrix3f rotation_matrix3;
	rotation_matrix3 << mIn->m[0][0],mIn->m[0][1],mIn->m[0][2],mIn->m[1][0],mIn->m[1][1],mIn->m[1][2],mIn->m[2][0],mIn->m[2][1],mIn->m[2][2];
	Eigen::Quaternionf quaternion;
	quaternion = rotation_matrix3;
	qOut->q[0] = quaternion.coeffs()[3];//real
	qOut->q[1] = quaternion.coeffs()[0];//i
	qOut->q[2] = quaternion.coeffs()[1];//j
	qOut->q[3] = quaternion.coeffs()[2];//k
}
#endif

//=========================================================欧拉角转旋转矩阵=========================================================
/**
 * @brief	欧拉角转旋转矩阵
 * @param	eIn 输入欧拉角
 * @param	mOut 输出旋转矩阵
 * @note	欧拉角使用XYZ内旋转序(先绕自身X轴旋转，再绕自身Y轴旋转，最后绕自身Z轴旋转)
 */
void eulerXYZToMatrix3x3(Euler *eIn, Matrix3x3 *mOut)
{
	float sx = sin(eIn->e[0]);//sin(roll)
	float cx = cos(eIn->e[0]);//cos(roll)
	float sy = sin(eIn->e[1]);//sin(pitch)
	float cy = cos(eIn->e[1]);//cos(pitch)
	float sz = sin(eIn->e[2]);//sin(yaw)
	float cz = cos(eIn->e[2]);//cos(yaw)
	mOut->m[0][0] = cy*cz;
	mOut->m[0][1] = -cy*sz;
	mOut->m[0][2] = sy;
	mOut->m[1][0] = cx*sz+sx*sy*cz;
	mOut->m[1][1] = cx*cz-sx*sy*sz;
	mOut->m[1][2] = -sx*cy;
	mOut->m[2][0] = sx*sz-cx*sy*cz;
	mOut->m[2][1] = sx*cz+cx*sy*sz;
	mOut->m[2][2] = cx*cy;
}
#ifdef _USE_EIGEN
void eulerXYZToMatrix3x3_Eigen(Euler *eIn, Matrix3x3 *mOut)
{
	Eigen::Matrix3f rotation_matrix3;
	rotation_matrix3 = Eigen::AngleAxisf(eIn->e[0], Eigen::Vector3f::UnitX()) * 
						Eigen::AngleAxisf(eIn->e[1], Eigen::Vector3f::UnitY()) * 
						Eigen::AngleAxisf(eIn->e[2], Eigen::Vector3f::UnitZ());
	for(int i = 0; i < 3; i++)
		for(int j = 0; j < 3; j++)
			mOut->m[i][j] = rotation_matrix3.coeff(i,j);//(row,col)
}
#endif

/**
 * @brief	欧拉角转旋转矩阵
 * @param	eIn 输入欧拉角
 * @param	mOut 输出旋转矩阵
 * @note	欧拉角使用ZYX内旋转序(先绕自身Z轴旋转，再绕自身Y轴旋转，最后绕自身X轴旋转)
 */
void eulerZYXToMatrix3x3(Euler *eIn, Matrix3x3 *mOut)//TODO：未完成
{
}
#ifdef _USE_EIGEN
void eulerZYXToMatrix3x3_Eigen(Euler *eIn, Matrix3x3 *mOut)//TODO：未测试
{
	Eigen::Matrix3f rotation_matrix3;
	rotation_matrix3 = Eigen::AngleAxisf(eIn->e[0], Eigen::Vector3f::UnitZ()) * 
						Eigen::AngleAxisf(eIn->e[1], Eigen::Vector3f::UnitY()) * 
						Eigen::AngleAxisf(eIn->e[2], Eigen::Vector3f::UnitX());
	for(int i = 0; i < 3; i++)
		for(int j = 0; j < 3; j++)
			mOut->m[i][j] = rotation_matrix3.coeff(i,j);//(row,col)
}
#endif

/**
 * @brief	欧拉角转旋转矩阵
 * @param	eIn 输入欧拉角
 * @param	mOut 输出旋转矩阵
 * @note	欧拉角使用YZX内旋转序(先绕自身Y轴旋转，再绕自身Z轴旋转，最后绕自身X轴旋转)
 */
void eulerYZXToMatrix3x3(Euler *eIn, Matrix3x3 *mOut)//TODO：未完成
{
}
#ifdef _USE_EIGEN
void eulerYZXToMatrix3x3_Eigen(Euler *eIn, Matrix3x3 *mOut)//TODO：未测试
{
	Eigen::Matrix3f rotation_matrix3;
	rotation_matrix3 = Eigen::AngleAxisf(eIn->e[0], Eigen::Vector3f::UnitY()) * 
						Eigen::AngleAxisf(eIn->e[1], Eigen::Vector3f::UnitZ()) * 
						Eigen::AngleAxisf(eIn->e[2], Eigen::Vector3f::UnitX());
	for(int i = 0; i < 3; i++)
		for(int j = 0; j < 3; j++)
			mOut->m[i][j] = rotation_matrix3.coeff(i,j);//(row,col)
}
#endif

//=========================================================旋转矩阵转欧拉角=========================================================
/**
 * @brief	旋转矩阵转欧拉角
 * @param	mIn 输入旋转矩阵
 * @param	eOut 输出欧拉角
 * @note	欧拉角使用XYZ内旋转序(先绕自身X轴旋转，再绕自身Y轴旋转，最后绕自身Z轴旋转)
 */
void matrix3x3ToEulerXYZ(Matrix3x3 *mIn, Euler *eOut)
{
	eOut->e[0] = atan2(-mIn->m[1][2],mIn->m[2][2]);
	eOut->e[1] = asin(mIn->m[0][2]);
	eOut->e[2] = atan2(-mIn->m[0][1],mIn->m[0][0]);
}
#ifdef _USE_EIGEN
void matrix3x3ToEulerXYZ_Eigen(Matrix3x3 *mIn, Euler *eOut)
{
	Eigen::Matrix3f rotation_matrix3;
	rotation_matrix3 << mIn->m[0][0],mIn->m[0][1],mIn->m[0][2],mIn->m[1][0],mIn->m[1][1],mIn->m[1][2],mIn->m[2][0],mIn->m[2][1],mIn->m[2][2];
	Eigen::Vector3f eulerAngle = rotation_matrix3.eulerAngles(0,1,2);
	eOut->e[0] = eulerAngle.coeff(0);
	eOut->e[1] = eulerAngle.coeff(1);
	eOut->e[2] = eulerAngle.coeff(2);
}
#endif

/**
 * @brief	旋转矩阵转欧拉角
 * @param	mIn 输入旋转矩阵
 * @param	eOut 输出欧拉角
 * @note	欧拉角使用ZYX内旋转序(先绕自身Z轴旋转，再绕自身Y轴旋转，最后绕自身X轴旋转)
 */
void matrix3x3ToEulerZYX(Matrix3x3 *mIn, Euler *eOut)//TODO：未完成
{
}
#ifdef _USE_EIGEN
void matrix3x3ToEulerZYX_Eigen(Matrix3x3 *mIn, Euler *eOut)//TODO：未测试
{
	Eigen::Matrix3f rotation_matrix3;
	rotation_matrix3 << mIn->m[0][0],mIn->m[0][1],mIn->m[0][2],mIn->m[1][0],mIn->m[1][1],mIn->m[1][2],mIn->m[2][0],mIn->m[2][1],mIn->m[2][2];
	Eigen::Vector3f eulerAngle = rotation_matrix3.eulerAngles(2,1,0);
	eOut->e[0] = eulerAngle.coeff(0);
	eOut->e[1] = eulerAngle.coeff(1);
	eOut->e[2] = eulerAngle.coeff(2);
}
#endif

/**
 * @brief	旋转矩阵转欧拉角
 * @param	mIn 输入旋转矩阵
 * @param	eOut 输出欧拉角
 * @note	欧拉角使用YZX内旋转序(先绕自身Y轴旋转，再绕自身Z轴旋转，最后绕自身X轴旋转)
 */
void matrix3x3ToEulerYZX(Matrix3x3 *mIn, Euler *eOut)//TODO：未完成
{
}
#ifdef _USE_EIGEN
void matrix3x3ToEulerYZX_Eigen(Matrix3x3 *mIn, Euler *eOut)//TODO：未测试
{
	Eigen::Matrix3f rotation_matrix3;
	rotation_matrix3 << mIn->m[0][0],mIn->m[0][1],mIn->m[0][2],mIn->m[1][0],mIn->m[1][1],mIn->m[1][2],mIn->m[2][0],mIn->m[2][1],mIn->m[2][2];
	Eigen::Vector3f eulerAngle = rotation_matrix3.eulerAngles(1,2,0);
	eOut->e[0] = eulerAngle.coeff(0);
	eOut->e[1] = eulerAngle.coeff(1);
	eOut->e[2] = eulerAngle.coeff(2);
}
#endif

}


#endif
