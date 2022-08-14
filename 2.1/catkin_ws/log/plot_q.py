import matplotlib.pyplot as plt
import os
import numpy as np
import math

folderName = '2021.4.20--21:7:56'
logPath = os.path.abspath('.')
folderPath = logPath + '/' + folderName; 

log_q_path = folderPath + '/' + 'log_q.txt'
log_odom_q_path = folderPath + '/' + 'log_odom_q.txt'
log_t_path = folderPath + '/' + 'log_t.txt'
log_acc_z_path = folderPath + '/' + 'log_acc_z.txt'
log_u_thr_path = folderPath + '/' + 'log_u_thr.txt'
log_v_z_path = folderPath + '/' + 'log_v_z.txt'
log_u_pitch_path = folderPath + '/' + 'log_u_pitch.txt'
log_u_roll_path = folderPath + '/' + 'log_u_roll.txt'

log_q = open(log_q_path,"r") 
log_odom_q = open(log_odom_q_path,"r") 
log_t = open(log_t_path,"r")
log_acc_z = open(log_acc_z_path,"r")
log_u_thr = open(log_u_thr_path,"r")
log_v_z = open(log_v_z_path,"r")
log_u_pitch = open(log_u_pitch_path,"r")
log_u_roll = open(log_u_roll_path,"r")

#t
t=[]
lines = log_t.readlines()
for line in lines:
	index = line.find('/')
	t.append(float(line[0:index]))

#u
u = []
lines = log_u_thr.readlines()
for line in lines:  
	index = line.find('/')
	u.append(float(line[index+1:-1])*3.1415926/180)


#v_z
v_z = []
lines = log_v_z.readlines()
for line in lines:  
	index = line.find('/')
	v_z.append(float(line[index+1:-1]))

#a_z
odom_a_z = []
a_horizon = 50
record_a_z = []
for index in range(len(v_z)):
	if index==0:
		odom_a_z.append(0)
		record_a_z.append(0)
	else:
		if index<a_horizon:
			record_a_z.append((v_z[index]-v_z[index-1])/(t[index]-t[index-1]))
		else:
			del(record_a_z[1])
			record_a_z.append((v_z[index]-v_z[index-1])/(t[index]-t[index-1]))
		odom_a_z.append(np.sum(record_a_z)/len(record_a_z))


#u_pitch
u_pitch = []
lines = log_u_pitch.readlines()
for line in lines:  
	index = line.find('/')
	u_pitch.append(float(line[index+1:-1]))

#u_pitch
u_roll = []
lines = log_u_roll.readlines()
for line in lines:  
	index = line.find('/')
	u_roll.append(float(line[index+1:-1]))


#plt.figure(1)
#plt.plot(t,odom_a_z)
#plt.xlabel('t/s')
#plt.ylabel('a_z')
#plt.grid()
##plt.show()

#imu_a_z
horizon = 10
acc_z = []
acc_h = []
lines = log_acc_z.readlines()
for line in lines:  
	acc_z.append(float(line))



imu_a_z =[]
for index in range(len(acc_z)):
	if index<horizon:
		acc_h.append(acc_z[index])
	else:
		del(acc_h[1])
		acc_h.append(acc_z[index])
	imu_a_z.append(np.sum(acc_h)/len(acc_h))

#plt.figure(1)
#plt.plot(t,imu_a_z)
#plt.xlabel('t/s')
#plt.ylabel('imu_a_z')
#plt.grid()
#plt.show()

#imu
w1 = []
x1 = []
y1 = []
z1 = []
roll1 = []
pitch1 =[]
yaw1 =[]


lines = log_q.readlines()
for line in lines:  
#	print(line)
	index = line.find('/')
	w1.append(float(line[0:index]))
	index1 = line.find('/', index+1, len(line))
	x1.append(float(line[index+1:index1]))
	index2 = line.find('/', index1+1, len(line))
	y1.append(float(line[index1+1:index2]))
	z1.append(float(line[index2+1:len(line)]))

	roll1.append(math.atan2(2 * (w1[-1] * x1[-1] + y1[-1] * z1[-1]), 1 - 2 * (x1[-1] * x1[-1] + y1[-1] * y1[-1]))/3.14*180.0)
	pitch1.append(math.asin(2 * (w1[-1] * y1[-1] - z1[-1] * x1[-1]))/3.14*180)
	yaw1.append(math.atan2(2 * (w1[-1]* z1[-1] + x1[-1] * y1[-1]), 1 - 2 * (y1[-1] * y1[-1] + z1[-1] * z1[-1]))/3.14*180)

#plt.figure()

#plt.subplot(311)
#plt.plot(t, roll1)
#plt.plot(t, u_roll)
#plt.xlabel('t/s')
#plt.ylabel('roll')
#plt.grid()

#plt.subplot(312)
#plt.plot(t, pitch1)
#plt.plot(t, u_pitch)
#plt.xlabel('t/s')
#plt.ylabel('pitch')
#plt.grid()

##plt.subplot(313)
##plt.plot(t, yaw1)
##plt.plot(t, u_yaw)
##plt.xlabel('t/s')
##plt.ylabel('yaw')
##plt.grid()
#plt.show()




##odom
#w = []
#x = []
#y = []
#z = []
#roll = []
#pitch =[]
#yaw =[]


#lines = log_odom_q.readlines()
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
#	yaw.append(math.atan2(2 * (w[-1]* z[-1] + x[-1] * y[-1]), 1 - 2 * (y[-1] * y[-1] + z[-1] * z[-1]))/3.14*180)

#plt.figure()
#plt.subplot(211)
#plt.plot(t, roll1,'b')
#plt.plot(t, roll,'r')
#plt.plot(t, u_roll,'y')
#plt.xlabel('t/s')
#plt.ylabel('roll')
#plt.grid()

#plt.subplot(212)
#plt.plot(t, pitch,'r')
#plt.plot(t, pitch1,'b')
#plt.plot(t, u_pitch,'y')
#plt.xlabel('t/s')
#plt.ylabel('pitch')
#plt.grid()

#plt.subplot(311)
#plt.plot(t, roll1,'b')
#plt.plot(t, roll,'r')
#plt.xlabel('t/s')
#plt.ylabel('roll')
#plt.grid()

#plt.subplot(312)
#plt.plot(t, pitch,'r')
#plt.plot(t, pitch1,'b')
#plt.xlabel('t/s')
#plt.ylabel('pitch')
#plt.grid()

#plt.subplot(313)
#plt.plot(t, yaw,'r')
#plt.plot(t, yaw1,'b')
#plt.xlabel('t/s')
#plt.ylabel('yaw')
#plt.grid()

#plt.show()

#plt.figure()
#plt.plot(t,desire, ls="-.")
#plt.grid()
#plt.xlabel("t/s")
#plt.ylabel(data_array[plot_index])
	
#wRb = np.ones(3,3)
#wRb[0][0] = 1-2*y*y-2*z*z
#wRb[0][1] = 2*x*y+2*w*z
#wRb[0][2] = 2*x*z-2*w*y
#wRb[1][0] = 2*x*y-2*w*z
#wRb[1][1] = 1-2*x*x-2*z*z
#wRb[1][2] = 2*y*z+2*w*x
#wRb[2][0] = 2*x*z+2*w*y
#wRb[2][1] = 2*y*z-2*w*x
#wRb[2][2] = 1-2*x*x-2*y*y

#bRw = np.linalg.inv(wRb)

##np.dot(bRw,)



#record_hovper = []
#hov_percent = 0.32
#mass = 0.96
#full_thrust = 29.8
#for index in range(len(t)):
#	if t[index]>17:
#		acc_body = acc_z[index]
#		acc_des = u[index]*full_thrust/mass
#		if math.fabs(acc_des-acc_body)<0.1:
#			compensate = (acc_des - acc_body) * 0.0001;
#		else:
#			compensate = (acc_des - acc_body) * 0.001;
##		compensate = (acc_des-acc_body)*0.001
#		hov_percent = hov_percent+compensate
#		if hov_percent<0.05:
#			hov_percent = 0.05
#		elif hov_percent>0.45:
#			hov_percent = 0.45
#		full_thrust = mass*9.81/hov_percent
#		record_hovper.append(hov_percent)
#	else:
#		record_hovper.append(0.32)

#plt.figure(1)
#plt.plot(t,record_hovper)
#plt.xlabel('t/s')
#plt.ylabel('hov_percent')
#plt.grid()


##u
#horizon1 = 10
##acc
#horizon2 = 50
#u_h = []
#acc_h = []
#index1 = 0

#record_hovper = []
#hov_percent = 0.5
#mass = 1.5
#full_thrust = 29.8
#for index in range(len(t)):
#	if t[index]>15:
#		acc_body = acc_z[index]
##		acc_body = odom_a_z[index]+9.81
#		acc_des = u[index]*full_thrust/mass
#		compensate = (acc_des - acc_body) * 0.00001;
##		if math.fabs(acc_des-acc_body)<0.1:
##			compensate = (acc_des - acc_body) * 0.001;
##		else:
##			compensate = (acc_des - acc_body) * 0.001;
##		compensate = (acc_des-acc_body)*0.001
#		hov_percent = hov_percent+compensate
##		if hov_percent<0.05:
##			hov_percent = 0.05
##		elif hov_percent>0.45:
##			hov_percent = 0.45
#		full_thrust = mass*9.81/hov_percent
#		record_hovper.append(hov_percent)
#	else:
#		record_hovper.append(hov_percent)
#		index1 = index

#plt.figure(1)
#plt.plot(t,record_hovper)
#plt.xlabel('t/s')
#plt.ylabel('hov_percent')
#plt.grid()
#plt.show()

#plt.figure(3)
#plt.plot(t,odom_a_z)
#plt.xlabel('t/s')
#plt.ylabel('odom_a_z')
#plt.grid()
##plt.show()
##plt.show()

#record_hovper1 = []
#hov_percent = 0.32
#mass = 0.96
#full_thrust = 29.8
#for index in range(len(t)):
#	if t[index]>17:
##		acc_body = odom_a_z[index]
#		acc_body = odom_a_z[index]+9.81
#		acc_des = u[index]*full_thrust/mass
#		if math.fabs(acc_des-acc_body)<0.1:
#			compensate = (acc_des - acc_body) * 0.0001;
#		else:
#			compensate = (acc_des - acc_body) * 0.0001;
##		compensate = (acc_des-acc_body)*0.001
#		hov_percent = hov_percent+compensate
#		if hov_percent<0.05:
#			hov_percent = 0.05
#		elif hov_percent>0.45:
#			hov_percent = 0.45
#		full_thrust = mass*9.81/hov_percent
#		record_hovper1.append(hov_percent)
#	else:
#		record_hovper1.append(0.32)
#		index1 = index

#plt.figure(4)
#plt.plot(t,record_hovper1)
#plt.xlabel('t/s')
#plt.ylabel('record_hovper1')
#plt.grid()
##plt.show()
#plt.show()
#####u
####horizon1 = 10
#####acc
####horizon2 = 5
####u_h = []
####acc_h = []
####index1 = 0

####record_hovper = []
####hov_percent = 0.32
####mass = 0.96
####full_thrust = 29.8
####for index in range(len(t)):
####	if t[index]>17:
####		if (index-index1)<horizon1:
####			u_h.append(u[index])
####		else:
####			del(u_h[1])
####			u_h.append(u[index])
####		if (index-index1)<horizon2:
####			acc_h.append(a_z[index])
####		else:
####			del(acc_h[1])
####			acc_h.append(a_z[index])
####		avg_u = np.sum(u_h)/len(u_h)
####		acc_body = np.sum(acc_h)/len(acc_h)
####		acc_des = avg_u*full_thrust/mass
####		if math.fabs(acc_des-acc_body)<0.1:
####			compensate = (acc_des - acc_body) * 0.0001;
####		else:
####			compensate = (acc_des - acc_body) * 0.001;
#####		compensate = (acc_des-acc_body)*0.001
####		hov_percent = hov_percent+compensate
####		if hov_percent<0.05:
####			hov_percent = 0.05
####		elif hov_percent>0.45:
####			hov_percent = 0.45
####		full_thrust = mass*9.81/hov_percent
####		record_hovper.append(hov_percent)
####	else:
####		record_hovper.append(0.32)
####		index1 = index

####plt.figure(1)
####plt.plot(t,record_hovper)
####plt.xlabel('t/s')
####plt.ylabel('hov_percent')
####plt.grid()
####plt.show()




#horizon1 = 100
#horizon2 = 50
#u_h = []
#acc_h = []

#record_hovper = []
#hov_percent = 0.3
#mass = 1
#full_thrust = mass*9.81/hov_percent
#for index in range(len(t)):

#	acc_body = acc_z[index]
#	if index<horizon1:
#		u_h.append(u[index])
#	else:
#		del(u_h[1])
#		u_h.append(u[index])
#	if index<horizon2:
#		acc_h.append(acc_z[index])
#	else:
#		del(acc_h[1])
#		acc_h.append(acc_z[index])
#	avg_u = np.sum(u_h)/len(u_h)
#	acc_body = np.sum(acc_h)/len(acc_h)
#	acc_des = avg_u*full_thrust/mass
#	compensate = (acc_des-acc_body)*0.001
#	hov_percent = hov_percent+compensate
#	if hov_percent<0.05:
#		hov_percent = 0.05
#	elif hov_percent>0.8:
#		hov_percent = 0.8
#	full_thrust = mass*9.81/hov_percent
#	record_hovper.append(hov_percent)

#plt.figure(2)
#plt.plot(t,record_hovper)
#plt.xlabel('t/s')
#plt.ylabel('hov_percent')
#plt.grid()
#plt.show()
