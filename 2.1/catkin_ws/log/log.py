import matplotlib.pyplot as plt
import os
import numpy as np
import Tkinter as tk
import math


mass = 1.5
g = np.array([[9.81]])
hover_per = 0.1
max_force = mass*g/hover_per
xx = np.array([[hover_per],[0.0]])
#P = np.array([[0.5*0.5,0.0],[0.0,1.0*1.0]])
P = 1*np.array([[0.01**2,0.0],[0.0,0.01**2]])
Q = 1.0*np.array([[0.000065**2,0.0],[0.0,1.0**2]])
F = np.array([[1.0,0.0],[-1.0*max_force/mass,0.0]])
B = np.array([[0.0],[max_force/mass]])
H = np.transpose(np.array([[0.0],[1.0]]))
R = 1.0*np.array([[0.08*0.08]])


def px_callback():
	global plot_index 
	plot_index = 0
	message.set('********We will plot des.p.x/odom.p.x********')
def py_callback():
	global plot_index 
	plot_index = 1
	message.set('********We will plot des.p.y/odom.p.y********')
def pz_callback():
	global plot_index 
	plot_index = 2
	message.set('********We will plot des.p.z/odom.p.z********')
def vx_callback():
	global plot_index 
	plot_index = 3
	message.set('********We will plot des.v.x/odom.v.x********')
def vy_callback():
	global plot_index 
	plot_index = 4
	message.set('********We will plot des.v.y/odom.v.y********')
def vz_callback():
	global plot_index 
	plot_index = 5
	message.set('********We will plot des.v.z/odom.v.z********')
def yaw_callback():
	global plot_index 
	plot_index = 6
	message.set('********We will plot des.yaw/odom.yaw********')
def rc_u_roll_callback():
	global plot_index 
	plot_index = 7
	message.set('********We will plot rc_data.roll/u.roll********')
def rc_u_pitch_callback():
	global plot_index 
	plot_index = 8
	message.set('********We will plot rc_data.pitch/u.pitch********')
def rc_u_yaw_callback():
	global plot_index 
	plot_index = 9
	message.set('********We will plot rc_data.yaw/u.yaw********')
def rc_u_thr_callback():
	global plot_index 
	plot_index = 10
	message.set('********We will plot rc_data.thr/u.thr********')
def hovper_callback():
	global plot_index
	plot_index = 11 
	message.set('********We will plot hov_percent********')
def acc_x_callback():
	global plot_index
	plot_index = 12 
	message.set('********We will plot acc_x********')
def acc_y_callback():
	global plot_index
	plot_index = 13
	message.set('********We will plot acc_y********')
def acc_z_callback():
	global plot_index
	plot_index = 14 
	message.set('********We will plot acc_z********')


def plot_callback():
	folderName = textinput.get()
	logPath = os.path.abspath('.')
	folderPath = logPath + '/' + folderName

	log_p_x_Path = folderPath + '/' + 'log_p_x.txt'
	log_p_y_Path = folderPath + '/' + 'log_p_y.txt'
	log_p_z_Path = folderPath + '/' + 'log_p_z.txt'
	log_v_x_Path = folderPath + '/' + 'log_v_x.txt'
	log_v_y_Path = folderPath + '/' + 'log_v_y.txt'
	log_v_z_Path = folderPath + '/' + 'log_v_z.txt'
	log_yaw_Path = folderPath + '/' + 'log_yaw.txt'
	log_u_roll_Path = folderPath + '/' + 'log_u_roll.txt'
	log_u_pitch_Path = folderPath + '/' + 'log_u_pitch.txt'
	log_u_yaw_Path = folderPath + '/' + 'log_u_yaw.txt'
	log_u_thr_Path = folderPath + '/' + 'log_u_thr.txt'
	log_hovper_Path = folderPath + '/' + 'log_hovper.txt'
	log_t_Path = folderPath + '/' + 'log_t.txt'
	log_acc_x_Path = folderPath + '/' + 'log_acc_x.txt'
	log_acc_y_Path = folderPath + '/' + 'log_acc_y.txt'
	log_acc_z_Path = folderPath + '/' + 'log_acc_z.txt'
	log_q_Path = folderPath + '/' + 'log_q.txt'
	log_odom_q_Path = folderPath + '/' + 'log_odom_q.txt'


	log_p_x = open(log_p_x_Path,"r") 
	log_p_y = open(log_p_y_Path,"r")
	log_p_z = open(log_p_z_Path,"r") 
	log_v_x = open(log_v_x_Path,"r") 
	log_v_y = open(log_v_y_Path,"r") 
	log_v_z = open(log_v_z_Path,"r") 
	log_yaw = open(log_yaw_Path,"r") 
	log_u_roll = open(log_u_roll_Path,"r") 
	log_u_pitch = open(log_u_pitch_Path,"r") 
	log_u_yaw = open(log_u_yaw_Path,"r") 
	log_u_thr = open(log_u_thr_Path,"r") 
	log_hovper = open(log_hovper_Path,"r")
	log_t = open(log_t_Path,"r")
	log_acc_x = open(log_acc_x_Path,"r")
	log_acc_y = open(log_acc_y_Path,"r")
	log_acc_z = open(log_acc_z_Path,"r")	
	log_q = open(log_q_Path,"r") 
	log_odom_q = open(log_odom_q_Path,"r")



	#t
	t=[]
	lines = log_t.readlines()
	for line in lines:  
		index = line.find('/')
		t.append(float(line[0:index]))

	#imu attitude
	imu_w = []
	imu_x = []
	imu_y = []
	imu_z = []
	imu_roll = []
	imu_pitch =[]
	imu_yaw =[]

	lines = log_q.readlines()
	for line in lines:  
		index = line.find('/')
		imu_w.append(float(line[0:index]))
		index1 = line.find('/', index+1, len(line))
		imu_x.append(float(line[index+1:index1]))
		index2 = line.find('/', index1+1, len(line))
		imu_y.append(float(line[index1+1:index2]))
		imu_z.append(float(line[index2+1:len(line)]))

		imu_roll.append(math.atan2(2 * (imu_w[-1] * imu_x[-1] + imu_y[-1] * imu_z[-1]), 1 - 2 * (imu_x[-1] * imu_x[-1] + imu_y[-1] * imu_y[-1]))/3.14*180.0)
		imu_pitch.append(math.asin(2 * (imu_w[-1] * imu_y[-1] - imu_z[-1] * imu_x[-1]))/3.14*180)
		imu_yaw.append(math.atan2(2 * (imu_w[-1]* imu_z[-1] + imu_x[-1] * imu_y[-1]), 1 - 2 * (imu_y[-1] * imu_y[-1] + imu_z[-1] * imu_z[-1]))/3.14*180)

	#odom attitude
	odom_w = []
	odom_x = []
	odom_y = []
	odom_z = []
	odom_roll = []
	odom_pitch =[]
	odom_yaw =[]

	lines = log_odom_q.readlines()
	for line in lines:  
		index = line.find('/')
		odom_w.append(float(line[0:index]))
		index1 = line.find('/', index+1, len(line))
		odom_x.append(float(line[index+1:index1]))
		index2 = line.find('/', index1+1, len(line))
		odom_y.append(float(line[index1+1:index2]))
		odom_z.append(float(line[index2+1:len(line)]))

		odom_roll.append(math.atan2(2 * (odom_w[-1] * odom_x[-1] + odom_y[-1] * odom_z[-1]), 1 - 2 * (odom_x[-1] * odom_x[-1] + odom_y[-1] * odom_y[-1]))/3.14*180.0)
		odom_pitch.append(math.asin(2 * (odom_w[-1] * odom_y[-1] - odom_z[-1] * odom_x[-1]))/3.14*180)
		odom_yaw.append(math.atan2(2 * (odom_w[-1]* odom_z[-1] + odom_x[-1] * odom_y[-1]), 1 - 2 * (odom_y[-1] * odom_y[-1] + odom_z[-1] * odom_z[-1]))/3.14*180)


	desire = []
	real = []
	lines = eval(data_array[plot_index]).readlines()
	print(data_array[plot_index])
	if plot_index<11:
		for line in lines:  
			index = line.find('/')
			desire.append(float(line[0:index]))
			real.append(float(line[index+1:-1]))
		if len(t)==len(real) & len(t)==len(desire):
			plt.figure()
			plt.plot(t,desire,'r--')
			plt.plot(t,real,'b')
			if plot_index<=6:
				plt.legend(["des","odom"])
			elif plot_index==7:
				plt.plot(t,imu_roll,'g--')
				plt.plot(t,odom_roll,'y')
				plt.legend(["input","output"])
			elif plot_index==8:
				plt.plot(t,imu_pitch,'g--')
				plt.plot(t,odom_pitch,'y')
				plt.legend(["input","output"])
			elif plot_index==9:
				plt.plot(t,imu_yaw,'g')
				plt.plot(t,odom_yaw,'y')
				plt.legend(["input","output"])
			else:
				plt.legend(["input","output"])
			plt.grid()
			plt.xlabel("t/s")
			plt.ylabel(data_array[plot_index])
			plt.show()
		else:
			message.set('Loading Data Failed')	
	elif plot_index==11:
		hov_per = []
		hor_x_k = []
		hor_y_k = []
		hor_z_k = []
		for line in lines:
			index = line.find('/')
			hov_per.append(float(line[0:index]))
			index1 = line.find('/', index+1, len(line))
			hor_x_k.append(float(line[index+1:index1]))
			index2 = line.find('/', index1+1, len(line))
			hor_y_k.append(float(line[index1+1:index2]))
			hor_z_k.append(float(line[index2+1:len(line)]))
		
		plt.figure()
		plt.plot(t, hov_per, "r")
#		plt.plot(t, hor_x_k, "y")
#		plt.plot(t, hor_y_k, "b")
#		plt.plot(t, hor_y_k, "g")
		plt.grid()
		plt.xlabel("t/s")
		plt.ylabel(data_array[plot_index])
		plt.legend(["hov_per"])
		plt.show()
	else:
		for line in lines:  
			index = line.find('/')
			real.append(float(line[0:index]))
		print(len(real))
		print(len(t))
		if len(t)==len(real):
			plt.figure()
			plt.plot(t,real, ls="--")
			plt.grid()
			plt.xlabel("t/s")
			plt.ylabel(data_array[plot_index])
			plt.show()
		else:
			message.set('Loading Data Failed')	
		

def process(u):
	global xx,P,Q,F,B
	xx = np.dot(F, xx)+B*u
	P = np.dot(np.dot(F, P), np.transpose(F)) + Q

def update(a):
	global xx,P,Q,F,B
	z1 = a - g
	y = z1 - np.dot(H, xx)
	k = np.dot(P, np.transpose(H)) * np.linalg.inv((np.dot(np.dot(H, P), np.transpose(H)) + R))
	xx = xx + k*y
	P = np.dot((np.identity(2)-np.dot(k, H)), P) 
#	if xx[0]<0.05:
#		xx[0] = 0.05
#	if xx[0]>0.45:
#		xx[0] = 0.45


#def simple_hovper():
	
def kalman_hovper():
	global xx,P
	startime = float(startime_input.get())
	folderName = textinput.get()
	logPath = os.path.abspath('.')
	folderPath = logPath + '/' + folderName;

	log_t_Path = folderPath + '/' + 'log_t.txt'
	log_u_thr_Path = folderPath + '/' + 'log_u_thr.txt'
	log_acc_x_Path = folderPath + '/' + 'log_acc_x.txt'
	log_acc_y_Path = folderPath + '/' + 'log_acc_y.txt'
	log_acc_z_Path = folderPath + '/' + 'log_acc_z.txt'
	log_hovper_Path = folderPath + '/' + 'log_hovper.txt'
	log_q_Path = folderPath + '/' + 'log_q.txt'


	log_t = open(log_t_Path,"r")
	log_u_thr = open(log_u_thr_Path,"r") 
	log_acc_x = open(log_acc_x_Path,"r")
	log_acc_y = open(log_acc_y_Path,"r")
	log_acc_z = open(log_acc_z_Path,"r")	
	log_hovper = open(log_hovper_Path,"r")
	log_q = open(log_q_Path,"r") 


	#t
	t=[]
	lines = log_t.readlines()
	for line in lines:
		index = line.find('/')
		t.append(float(line[0:index]))
	#imu
	w = []
	x = []
	y = []
	z = []
	roll = []
	pitch = []
	yaw = []

	lines = log_q.readlines()
	for line in lines:  
	#	print(line)
		index = line.find('/')
		w.append(float(line[0:index]))
		index1 = line.find('/', index+1, len(line))
		x.append(float(line[index+1:index1]))
		index2 = line.find('/', index1+1, len(line))
		y.append(float(line[index1+1:index2]))
		z.append(float(line[index2+1:len(line)]))

		roll.append(math.atan2(2 * (w[-1] * x[-1] + y[-1] * z[-1]), 1 - 2 * (x[-1] * x[-1] + y[-1] * y[-1]))/3.14*180.0)
		pitch.append(math.asin(2 * (w[-1] * y[-1] - z[-1] * x[-1]))/3.14*180)
		yaw.append(math.atan2(2 * (w[-1]* z[-1] + x[-1] * y[-1]), 1 - 2 * (y[-1] * y[-1] + z[-1] * z[-1]))/3.14*180.0)

	#u
	u = []
	z_u = []
	lines = log_u_thr.readlines()
	for line in lines:  
		index = line.find('/')
		u.append(float(line[index+1:-1]))
		wRb = np.ones((3,3))
		wRb[0][0] = 1-2*y[index]*y[index]-2*z[index]*z[index]
		wRb[0][1] = 2*x[index]*y[index]+2*w[index]*z[index]
		wRb[0][2] = 2*x[index]*z[index]-2*w[index]*y[index]
		wRb[1][0] = 2*x[index]*y[index]-2*w[index]*z[index]
		wRb[1][1] = 1-2*x[index]*x[index]-2*z[index]*z[index]
		wRb[1][2] = 2*y[index]*z[index]+2*w[index]*x[index]
		wRb[2][0] = 2*x[index]*z[index]+2*w[index]*y[index]
		wRb[2][1] = 2*y[index]*z[index]-2*w[index]*x[index]
		wRb[2][2] = 1-2*x[index]*x[index]-2*y[index]*y[index]
		z_u.append(float(line[index+1:-1])*wRb[2][2])

	#acc_z
	acc_z = []
	lines = log_acc_z.readlines()
	for line in lines:  
		acc_z.append(float(line))
	#acc_x
	acc_x = []
	lines = log_acc_x.readlines()
	for line in lines:  
		acc_x.append(float(line))
	#acc_y
	acc_y = []
	lines = log_acc_y.readlines()
	for line in lines:  
		acc_y.append(float(line))


	#kalman
	acc_world = []
	record_hovper_w = []
	for index in range(len(t)):
		wRb = np.ones([3,3])
		wRb[0][0] = 1-2*y[index]*y[index]-2*z[index]*z[index]
		wRb[0][1] = 2*x[index]*y[index]-2*w[index]*z[index]
		wRb[0][2] = 2*x[index]*z[index]+2*w[index]*y[index]
		wRb[1][0] = 2*x[index]*y[index]+2*w[index]*z[index]
		wRb[1][1] = 1-2*x[index]*x[index]-2*z[index]*z[index]
		wRb[1][2] = 2*y[index]*z[index]-2*w[index]*x[index]
		wRb[2][0] = 2*x[index]*z[index]-2*w[index]*y[index]
		wRb[2][1] = 2*y[index]*z[index]+2*w[index]*x[index]
		wRb[2][2] = 1-2*x[index]*x[index]-2*y[index]*y[index]
		
		acc = np.zeros([3,1])
		acc[0][0] = acc_x[index]
		acc[1][0] = acc_y[index]
		acc[2][0] = acc_z[index]
		a = np.zeros([1,1])
		acc = np.dot(wRb, acc)
		acc_world.append(acc[2])
		a[0][0] = acc[2]
		u0 = np.zeros([1,1])
		u0[0][0] = z_u[index]
		if t[index]>startime:
			update(a)
			process(u0)
			record_hovper_w.append(xx[0])
		else:
			record_hovper_w.append(hover_per)

	
#	xx = np.array([[hover_per],[0.0]])
#	P = np.array([[10*10,0.0],[0.0,10*10]])
#	record_hovper_b = []
#	for index in range(len(t)):
#		if t[index]>startime:
#			a = np.zeros([1,1])
#			acc = np.dot(wRb, acc)
#			a[0][0] = acc_z[index]
#			u0 = np.zeros([1,1])
#			u0[0,0] = u[index]
#			update(a)
#			process(u0)
#			record_hovper_b.append(xx[0])
#		else:
#			record_hovper_b.append(hover_per)



	plt.figure()
#	plt.subplot(311)
#	plt.plot(t, record_hovper_b,'b')
	plt.plot(t, record_hovper_w,'r')
	plt.xlabel('t/s')
	plt.ylabel('hover_per')
	plt.grid()
	plt.legend(['body','world'])

#	plt.subplot(312)
#	plt.plot(t, acc_world,'b')
#	plt.plot(t, acc_z,'r')
#	plt.xlabel('t/s')
#	plt.ylabel('acc')
#	plt.grid()
#	plt.legend(['world','body'])

#	plt.subplot(313)
#	plt.plot(t, z_u,'r')
#	plt.plot(t, u,'b')
#	plt.xlabel('t/s')
#	plt.ylabel('u')
#	plt.grid()
#	plt.legend(['world','body'])

	plt.show()


def plot_lmpc():
	folderName = textinput.get()
	logPath = os.path.abspath('.')
	folderPath = logPath + '/' + folderName;

	log_t_Path = folderPath + '/' + 'log_t.txt'
	log_target_Path = folderPath + '/' + 'log_target.txt'
	log_p_x_Path = folderPath + '/' + 'log_p_x.txt'
	log_p_y_Path = folderPath + '/' + 'log_p_y.txt'
	log_v_x_Path = folderPath + '/' + 'log_v_x.txt'
	log_v_y_Path = folderPath + '/' + 'log_v_y.txt'
	log_eso_x_Path = folderPath + '/' + 'log_eso_x.txt'
	log_eso_y_Path = folderPath + '/' + 'log_eso_y.txt'
	log_t = open(log_t_Path,"r")
	log_target = open(log_target_Path,"r")
	log_p_x = open(log_p_x_Path,"r")
	log_p_y = open(log_p_y_Path,"r")
	log_v_x = open(log_v_x_Path,"r")
	log_v_y = open(log_v_y_Path,"r")
	log_eso_x = open(log_eso_x_Path,"r")
	log_eso_y = open(log_eso_y_Path,"r")
	
	#t
	t=[]
	lines = log_t.readlines()
	for line in lines:
		index = line.find('/')
		t.append(float(line[0:index]))
	
	#target
	target_x = []
	target_y = []
	target_vx = []
	target_vy = []
	lines = log_target.readlines()
	for line in lines:  
		index = line.find('/')
		target_x.append(float(line[0:index]))
		index1 = line.find('/', index+1, len(line))
		target_vx.append(float(line[index+1:index1]))
		index2 = line.find('/', index1+1, len(line))
		target_y.append(float(line[index1+1:index2]))
		target_vy.append(float(line[index2+1:len(line)]))
		
	#x,y,vx,vy
	uav_des_x = []
	uav_des_y = []
	uav_des_vx = []
	uav_des_vy = []
	
	uav_x = []
	uav_y = []
	uav_vx = []
	uav_vy = []
	
	eso_px = []
	eso_vx = []
	eso_dx = []
	
	eso_py = []
	eso_vy = []
	eso_dy = []
	
	lines = log_p_x.readlines()
	for line in lines:  
		index = line.find('/')
		uav_des_x.append(float(line[0:index]))
		uav_x.append(float(line[index+1:-1]))
		
	lines = log_p_y.readlines()
	for line in lines:  
		index = line.find('/')
		uav_des_y.append(float(line[0:index]))
		uav_y.append(float(line[index+1:-1]))
		
	lines = log_v_x.readlines()
	for line in lines:  
		index = line.find('/')
		uav_des_vx.append(float(line[0:index]))
		uav_vx.append(float(line[index+1:-1]))
		
	lines = log_v_y.readlines()
	for line in lines:  
		index = line.find('/')
		uav_des_vy.append(float(line[0:index]))
		uav_vy.append(float(line[index+1:-1]))
		
	lines = log_eso_x.readlines()
	for line in lines:  
		index = line.find('/')
		eso_px.append(float(line[0:index]))
		index1 = line.find('/', index+1, len(line))
		eso_vx.append(float(line[index+1:index1]))
		eso_dx.append(float(line[index1+1:len(line)]))
		
	lines = log_eso_y.readlines()
	for line in lines:  
		index = line.find('/')
		eso_py.append(float(line[0:index]))
		index1 = line.find('/', index+1, len(line))
		eso_vy.append(float(line[index+1:index1]))
		eso_dy.append(float(line[index1+1:len(line)]))
		
	
	plt.figure()
	plt.subplot(311)
	plt.plot(t, uav_x, 'r')
	plt.plot(t, uav_des_x, 'b')
	plt.plot(t, eso_px, 'g')
	plt.grid()
	plt.legend(['real', 'des', 'eso'])
	
	plt.subplot(312)
	plt.plot(t, uav_vx, 'r')
	plt.plot(t, uav_des_vx, 'b')
	plt.plot(t, eso_vx, 'g')
	plt.grid()
	plt.legend(['real', 'des', 'eso'])
	
	plt.subplot(313)
	plt.plot(t, eso_dx, 'g')
	plt.grid()
	
	plt.figure()
	plt.subplot(311)
	plt.plot(t, uav_y, 'r')
	plt.plot(t, uav_des_y, 'b')
	plt.plot(t, eso_py, 'g')
	plt.grid()
	plt.legend(['real', 'des', 'eso'])
	
	plt.subplot(312)
	plt.plot(t, uav_vy, 'r')
	plt.plot(t, uav_des_vy, 'b')
	plt.plot(t, eso_vy, 'g')
	plt.grid()
	plt.legend(['real', 'des', 'eso'])
	
	plt.subplot(313)
	plt.plot(t, eso_dy, 'g')
	plt.grid()
	plt.legend(['real', 'des', 'eso'])
	
#	plt.figure()
#	plt.plot(target_x, target_y)
##	plt.plot(uav_des_x, uav_des_y, 'y')
#	plt.plot(uav_x, uav_y, '--')
#	
#	plt.xlabel('x/m')
#	plt.ylabel('y/m')
#	plt.grid()
#	plt.legend(['target', 'uav'])
#	
#	
#	plt.figure()
#	plt.plot(t, target_x, '--')
#	plt.plot(t, uav_x,)
#	
#	plt.xlabel('t/s')
#	plt.ylabel('x/m')
#	plt.grid()
#	plt.legend(['target_x', 'uav_x'])
#	
#	plt.figure()
#	plt.plot(t, target_y, '--')
#	plt.plot(t, uav_y,)
#	
#	plt.xlabel('t/s')
#	plt.ylabel('y/m')
#	plt.grid()
#	plt.legend(['target_y', 'uav_y'])
	
	plt.show()

		
	
	

#2021.4.16--19:12:50
data_array = ['log_p_x','log_p_y','log_p_z',
							'log_v_x','log_v_y','log_v_z',
							'log_yaw',
							'log_u_roll','log_u_pitch','log_u_yaw','log_u_thr',
							'log_hovper',
							'log_acc_x','log_acc_y','log_acc_z']





frame = tk.Tk()
frame.title('Visulization')
frame.geometry('500x200+1000+400')

bigmenu = tk.Menu(frame)
datamenu = tk.Menu(bigmenu,tearoff = 0)
datamenu.add_command(label='des.p.x/odom.p.x', command=px_callback)
datamenu.add_command(label='des.p.y/odom.p.y', command=py_callback)
datamenu.add_command(label='des.p.z/odom.p.z', command=pz_callback)
datamenu.add_separator()
datamenu.add_command(label='des.v.x/odom.v.x', command=vx_callback)
datamenu.add_command(label='des.v.y/odom.v.y', command=vy_callback)
datamenu.add_command(label='des.v.z/odom.v.z', command=vz_callback)
datamenu.add_separator()
datamenu.add_command(label='des.yaw/odom.yaw', command=yaw_callback)
datamenu.add_separator()
datamenu.add_command(label='rc_data.roll/u.roll', command=rc_u_roll_callback)
datamenu.add_command(label='rc_data.pitch/u.pitch', command=rc_u_pitch_callback)
datamenu.add_command(label='rc_data.yaw/u.yaw', command=rc_u_yaw_callback)
datamenu.add_command(label='rc_data.thr/u.thrust', command=rc_u_thr_callback)
datamenu.add_separator()
datamenu.add_command(label='hovper', command=hovper_callback)
datamenu.add_separator()
datamenu.add_command(label='acc_x', command=acc_x_callback)
datamenu.add_command(label='acc_y', command=acc_y_callback)
datamenu.add_command(label='acc_z', command=acc_z_callback)
bigmenu.add_cascade(label = 'data',menu = datamenu)
frame.config(menu = bigmenu)

textinput = tk.Entry(frame,width=25,show=None)
textinput.place(x=150,y=15)

startime_input = tk.Entry(frame,width=25,show=None)
startime_input.place(x=150,y=60)


message = tk.StringVar()
message.set('*********** Welcome  to  DataPloter ***********')
label = tk.Label(frame, textvariable=message).place(x=40,y=100)
label1 = tk.Label(frame, text="foldername:").place(x=40,y=15)
label2 = tk.Label(frame, text="startime:").place(x=40,y=60)

plot_index = 0
tk.Button(frame, text="plot",width=7,height=2, command=plot_callback).place(x=400,y=20)
tk.Button(frame, text="hovper",width=7,height=2, command=kalman_hovper).place(x=400,y=80)
tk.Button(frame, text="lmpc",width=60,height=2, command=plot_lmpc).place(x=30,y=140)

frame.mainloop()




#flightlog.log_p_x << des.p.x() << "/" << odom_data.p.x() << endl;
#	flightlog.log_p_y << des.p.y() << "/" << odom_data.p.y() << endl;
#	flightlog.log_p_z << des.p.z() << "/" << odom_data.p.z() << endl;
#	flightlog.log_v_x << des.v.x() << "/" << odom_data.v.x() << endl;
#	flightlog.log_v_y << des.v.y() << "/" << odom_data.v.y() << endl;
#	flightlog.log_v_z << des.v.z() << "/" << odom_data.v.z() << endl;
#	flightlog.log_yaw << des.yaw << "/" << 2*std::atan2(odom_data.q.z(), odom_data.q.w()) / M_PI * 180.0 << endl;
#	flightlog.log_u_roll << rc_data.roll << "/" << toDeg(u.roll) << endl;
#	flightlog.log_u_pitch << rc_data.pitch << "/" << toDeg(u.pitch) << endl;
#	flightlog.log_u_yaw << rc_data.yaw << "/" << toDeg(u.yaw) << endl;
#	flightlog.log_u_thr << rc_data.thr << "/" << toDeg(u.thrust) << endl;
#	flightlog.log_hovper << hovper << endl;
#	flightlog.log_t << now_time.toSec() << endl;




#startime = 0
#folderName = '1205night5'
#logPath = os.path.abspath('.')
#folderPath = logPath + '/' + folderName;

#log_t_Path = folderPath + '/' + 'log_t.txt'
#log_u_thr_Path = folderPath + '/' + 'log_u_thr.txt'
#log_acc_x_Path = folderPath + '/' + 'log_acc_x.txt'
#log_acc_y_Path = folderPath + '/' + 'log_acc_y.txt'
#log_acc_z_Path = folderPath + '/' + 'log_acc_z.txt'
#log_hovper_Path = folderPath + '/' + 'log_hovper.txt'
#log_q_Path = folderPath + '/' + 'log_q.txt'


#log_t = open(log_t_Path,"r")
#log_u_thr = open(log_u_thr_Path,"r") 
#log_acc_x = open(log_acc_x_Path,"r")
#log_acc_y = open(log_acc_y_Path,"r")
#log_acc_z = open(log_acc_z_Path,"r")	
#log_hovper = open(log_hovper_Path,"r")
#log_q = open(log_q_Path,"r") 


##t
#t=[]
#lines = log_t.readlines()
#for line in lines:
#	index = line.find('/')
#	t.append(float(line[0:index]))
##imu
#w = []
#x = []
#y = []
#z = []
#roll = []
#pitch = []
#yaw = []

#lines = log_q.readlines()
#for line in lines:  
##	print(line)
#	index = line.find('/')
#	w.append(float(line[0:index]))
#	index1 = line.find('/', index+1, len(line))
#	x.append(float(line[index+1:index1]))
#	index2 = line.find('/', index1+1, len(line))
#	y.append(float(line[index1+1:index2]))
#	z.append(float(line[index2+1:len(line)]))

#	roll.append(math.atan2(2 * (w[-1] * x[-1] + y[-1] * z[-1]), 1 - 2 * (x[-1] * x[-1] + y[-1] * y[-1]))/3.14*180.0)
#	pitch.append(math.asin(2 * (w[-1] * y[-1] - z[-1] * x[-1]))/3.14*180)
#	yaw.append(math.atan2(2 * (w[-1]* z[-1] + x[-1] * y[-1]), 1 - 2 * (y[-1] * y[-1] + z[-1] * z[-1]))/3.14*180.0)

##u
#u = []
#z_u = []
#lines = log_u_thr.readlines()
#for line in lines:  
#	index = line.find('/')
#	u.append(float(line[index+1:-1]))
#	wRb = np.ones((3,3))
#	wRb[0][0] = 1-2*y[index]*y[index]-2*z[index]*z[index]
#	wRb[0][1] = 2*x[index]*y[index]+2*w[index]*z[index]
#	wRb[0][2] = 2*x[index]*z[index]-2*w[index]*y[index]
#	wRb[1][0] = 2*x[index]*y[index]-2*w[index]*z[index]
#	wRb[1][1] = 1-2*x[index]*x[index]-2*z[index]*z[index]
#	wRb[1][2] = 2*y[index]*z[index]+2*w[index]*x[index]
#	wRb[2][0] = 2*x[index]*z[index]+2*w[index]*y[index]
#	wRb[2][1] = 2*y[index]*z[index]-2*w[index]*x[index]
#	wRb[2][2] = 1-2*x[index]*x[index]-2*y[index]*y[index]
#	z_u.append(float(line[index+1:-1])*wRb[2][2])

##acc_z
#acc_z = []
#lines = log_acc_z.readlines()
#for line in lines:  
#	acc_z.append(float(line))
##acc_x
#acc_x = []
#lines = log_acc_x.readlines()
#for line in lines:  
#	acc_x.append(float(line))
##acc_y
#acc_y = []
#lines = log_acc_y.readlines()
#for line in lines:  
#	acc_y.append(float(line))


##kalman
#acc_world = []
#record_hovper_w = []
#for index in range(len(t)):
#	wRb = np.ones([3,3])
#	wRb[0][0] = 1-2*y[index]*y[index]-2*z[index]*z[index]
#	wRb[0][1] = 2*x[index]*y[index]-2*w[index]*z[index]
#	wRb[0][2] = 2*x[index]*z[index]+2*w[index]*y[index]
#	wRb[1][0] = 2*x[index]*y[index]+2*w[index]*z[index]
#	wRb[1][1] = 1-2*x[index]*x[index]-2*z[index]*z[index]
#	wRb[1][2] = 2*y[index]*z[index]-2*w[index]*x[index]
#	wRb[2][0] = 2*x[index]*z[index]-2*w[index]*y[index]
#	wRb[2][1] = 2*y[index]*z[index]+2*w[index]*x[index]
#	wRb[2][2] = 1-2*x[index]*x[index]-2*y[index]*y[index]
#	
#	acc = np.zeros([3,1])
#	acc[0][0] = acc_x[index]
#	acc[1][0] = acc_y[index]
#	acc[2][0] = acc_z[index]
#	a = np.zeros([1,1])
#	acc = np.dot(wRb, acc)
#	acc_world.append(acc[2])
#	a[0][0] = acc[2]
#	u0 = np.zeros([1,1])
#	u0[0][0] = z_u[index]
#	if t[index]>startime:
#		if xx[0]>0.2:
#			Q = 1.0*np.array([[0.000065**2,0.0],[0.0,1**2]])
#		else:
#			Q = 1.0*np.array([[0.000065**2,0.0],[0.0,0.001**2]])
#		update(a)
#		process(u0)
#		record_hovper_w.append(xx[0])
#	else:
#		record_hovper_w.append(hover_per)


##	xx = np.array([[hover_per],[0.0]])
##	P = np.array([[10*10,0.0],[0.0,10*10]])
##	record_hovper_b = []
##	for index in range(len(t)):
##		if t[index]>startime:
##			a = np.zeros([1,1])
##			acc = np.dot(wRb, acc)
##			a[0][0] = acc_z[index]
##			u0 = np.zeros([1,1])
##			u0[0,0] = u[index]
##			update(a)
##			process(u0)
##			record_hovper_b.append(xx[0])
##		else:
##			record_hovper_b.append(hover_per)



#plt.figure()
##	plt.subplot(311)
##	plt.plot(t, record_hovper_b,'b')
#plt.plot(t, record_hovper_w,'r')
#plt.xlabel('t/s')
#plt.ylabel('hover_per')
#plt.grid()
#plt.legend(['body','world'])

##	plt.subplot(312)
##	plt.plot(t, acc_world,'b')
##	plt.plot(t, acc_z,'r')
##	plt.xlabel('t/s')
##	plt.ylabel('acc')
##	plt.grid()
##	plt.legend(['world','body'])

##	plt.subplot(313)
##	plt.plot(t, z_u,'r')
##	plt.plot(t, u,'b')
##	plt.xlabel('t/s')
##	plt.ylabel('u')
##	plt.grid()
##	plt.legend(['world','body'])

#plt.show()
