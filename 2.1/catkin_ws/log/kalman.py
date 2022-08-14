import matplotlib.pyplot as plt
import os
import numpy as np
import math

mass = 1.5
g = np.array([[9.81]])
hover_per = 0.3
max_force = mass*g/hover_per
xx = np.array([[hover_per],[0.0]])
#P = np.array([[0.5*0.5,0.0],[0.0,1.0*1.0]])
P = np.array([[0.001*0.001,0.0],[0.0,0.001*0.001]])
Q = np.array([[0.1*0.1,0.0],[0.0,1.0*1.0]])
F = np.array([[1.0,0.0],[-1.0*max_force/mass,0.0]])
B = np.array([[0.0],[max_force/mass]])
H = np.transpose(np.array([[0.0],[1.0]]))
R = np.array([[1*1]])


#kalman_y = []
#kalman_k0 = []
#kalman_k1 = []
#kalman_p0 = []
#kalman_p1 = []
def process(u):
	global xx,P
	xx = np.dot(F, xx)+B*u
	P = np.dot(np.dot(F, P), np.transpose(F)) + Q*0.0
#	kalman_p0.append(P[0][0])
#	kalman_p1.append(P[1][1])
#	print(x)
	
def update(a):
	global xx,P
	z1 = a - g
#	print(x)
	y = z1 - np.dot(H, xx)
#	kalman_y.append(float(y))
#	print(y)
	k = np.dot(P, np.transpose(H)) * np.linalg.inv((np.dot(np.dot(H, P), np.transpose(H)) + R))
#	if k[0]>0.001:
#		k[0] = 0.001
#	elif k[0]<-0.001:
#		k[0] = -0.001
#	if k[1]>0.001:
#		k[1] = 0.001
#	elif k[1]<-0.001:
#		k[1] = -0.001
#	if y>1:
#		y = 0.1
#	elif y<-1:
#		y = -0.1
#	kalman_k0.append(float(k[0]))
#	kalman_k1.append(float(k[1]))
#	print(k.shape)
	xx = xx + k*y
	P = np.dot((np.identity(2)-np.dot(k, H)), P) 
#	print(k)

#	if xx[0]<0.05:
#		xx[0] = 0.05
#	if xx[0]>0.45:
#		xx[0] = 0.45

folderName = '422night7'
logPath = os.path.abspath('.')
folderPath = logPath + '/' + folderName; 


log_t_path = folderPath + '/' + 'log_t.txt'
log_acc_x_path = folderPath + '/' + 'log_acc_x.txt'
log_acc_y_path = folderPath + '/' + 'log_acc_y.txt'
log_acc_z_path = folderPath + '/' + 'log_acc_z.txt'
log_u_thr_path = folderPath + '/' + 'log_u_thr.txt'
log_v_z_path = folderPath + '/' + 'log_v_z.txt'
log_q_path = folderPath + '/' + 'log_q.txt'



log_t = open(log_t_path,"r")
log_q = open(log_q_path,"r") 
log_acc_x = open(log_acc_x_path,"r")
log_acc_y = open(log_acc_y_path,"r")
log_acc_z = open(log_acc_z_path,"r")
log_u_thr = open(log_u_thr_path,"r")
log_v_z = open(log_v_z_path,"r")



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
	yaw.append(math.atan2(2 * (w[-1]* z[-1] + x[-1] * y[-1]), 1 - 2 * (y[-1] * y[-1] + z[-1] * z[-1]))/3.14*180)

#t
t=[]
lines = log_t.readlines()
for line in lines:
	index = line.find('/')
	t.append(float(line[0:index]))


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
#	print(wRb[2][2])
	z_u.append(float(line[index+1:-1])*wRb[2][2])


#v_z
v_z = []
lines = log_v_z.readlines()
for line in lines:  
	index = line.find('/')
	v_z.append(float(line[index+1:-1]))

#odom_a_z
odom_a_z = []
a_horizon = 10
record_a_z = []
for index in range(len(v_z)):
	if index==0:
		odom_a_z.append(0)
		record_a_z.append(0)
	else:
		if index<a_horizon:
			record_a_z.append((v_z[index]-v_z[index-1])/(t[index]-t[index-1])+9.81)
		else:
			del(record_a_z[1])
			record_a_z.append((v_z[index]-v_z[index-1])/(t[index]-t[index-1])+9.81)
		odom_a_z.append(np.sum(record_a_z)/len(record_a_z))


#acc_z
horizon = 10
acc_z = []
acc_h = []
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


#imu_a_z
imu_a_z =[]
for index in range(len(acc_z)):
	if index<horizon:
		acc_h.append(acc_z[index])
	else:
		del(acc_h[1])
		acc_h.append(acc_z[index])
	imu_a_z.append(np.sum(acc_h)/len(acc_h))



#record_hovper = []
#for index in range(len(t)):
#	if t[index]>10:
#		a = np.zeros([1,1])
#		a[0][0] = odom_a_z[index]
##		print(a,a.shape)
#		u0 = np.zeros([1,1])
#		u0[0,0] = u[index]
#		update(a)
#		process(u0)
#		record_hovper.append(x[0])
#	else:
#		record_hovper.append(hover_per)
acc_world = []
record_hovper1 = []
for index in range(len(t)):
	wRb = np.ones([3,3])
#	wRb[0][0] = 1-2*y[index]*y[index]-2*z[index]*z[index]
#	wRb[0][1] = 2*x[index]*y[index]+2*w[index]*z[index]
#	wRb[0][2] = 2*x[index]*z[index]-2*w[index]*y[index]
#	wRb[1][0] = 2*x[index]*y[index]-2*w[index]*z[index]
#	wRb[1][1] = 1-2*x[index]*x[index]-2*z[index]*z[index]
#	wRb[1][2] = 2*y[index]*z[index]+2*w[index]*x[index]
#	wRb[2][0] = 2*x[index]*z[index]+2*w[index]*y[index]
#	wRb[2][1] = 2*y[index]*z[index]-2*w[index]*x[index]
#	wRb[2][2] = 1-2*x[index]*x[index]-2*y[index]*y[index]

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
	if t[index]>7.5:
		update(a)
		process(u0)
		record_hovper1.append(xx[0])
	else:
		record_hovper1.append(hover_per)

#	update(a)
#	process(u0)
#	record_hovper1.append(xx[0])
xx = np.array([[hover_per],[0.0]])
P = np.array([[0.5*0.5,0.0],[0.0,1.0*1.0]])
record_hovper = []
for index in range(len(t)):
	if t[index]>7.5:
		a = np.zeros([1,1])
		acc = np.dot(wRb, acc)
		a[0][0] = acc_z[index]
		u0 = np.zeros([1,1])
		u0[0,0] = u[index]
		update(a)
		process(u0)
		record_hovper.append(xx[0])
	else:
		record_hovper.append(hover_per)



plt.figure(1)
plt.subplot(311)
plt.plot(t, record_hovper,'b')
plt.plot(t, record_hovper1,'r')
plt.xlabel('t/s')
plt.ylabel('hover_per')
plt.grid()
plt.legend(['body','world'])

plt.subplot(312)
plt.plot(t, acc_world,'b')
plt.plot(t, acc_z,'r')
plt.xlabel('t/s')
plt.ylabel('acc')
plt.grid()

plt.subplot(313)
plt.plot(t, z_u,'r')
plt.plot(t, u,'b')
plt.xlabel('t/s')
plt.ylabel('u')
plt.grid()

plt.figure(2)
plt.plot(range(len(kalman_p0)),kalman_p0,'r')
plt.plot(range(len(kalman_p1)),kalman_p1,'b')
plt.show()
#plt.figure(2)
#plt.subplot(311)
#plt.plot(t, kalman_y,'r')
#plt.xlabel('t/s')
#plt.ylabel('y')
#plt.grid()

#plt.subplot(312)
#plt.plot(t, kalman_k0,'r')
#plt.xlabel('t/s')
#plt.ylabel('k0')
#plt.grid()

#plt.subplot(313)
#plt.plot(t, kalman_k1,'r')
#plt.xlabel('t/s')
#plt.ylabel('k1')
#plt.grid()

#plt.suptitle('imu')
#print(len(t),len(kalman_y))
plt.show()
#plt.subplot(412)
#plt.plot(t, pitch,'r')kalman_p0
#plt.plot(t, pitch1,'b')
#plt.plot(t, u_pitch,'y')
#plt.xlabel('t/s')
#plt.ylabel('pitch')
#plt.grid()

#plt.subplot(421)
#plt.plot(t, roll1,'b')
#plt.plot(t, roll,'r')
#plt.xlabel('t/s')
#plt.ylabel('roll')
#plt.grid()

#plt.subplot(422)
#plt.plot(t, pitch,'r')
#plt.plot(t, pitch1,'b')
#plt.xlabel('t/s')
#plt.ylabel('pitch')
#plt.grid()

#plt.show()
#w = 0.707
#x = 0.707
#y = 0
#z = 0
#wRb = np.ones([3,3])
#wRb[0][0] = 1-2*y*y-2*z*z
#wRb[0][1] = 2*x*y-2*w*z
#wRb[0][2] = 2*x*z+2*w*y
#wRb[1][0] = 2*x*y+2*w*z
#wRb[1][1] = 1-2*x*x-2*z*z
#wRb[1][2] = 2*y*z-2*w*x
#wRb[2][0] = 2*x*z-2*w*y
#wRb[2][1] = 2*y*z+2*w*x
#wRb[2][2] = 1-2*x*x-2*y*y
#print(wRb)
