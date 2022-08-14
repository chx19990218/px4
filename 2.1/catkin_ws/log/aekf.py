import matplotlib.pyplot as plt
import os
import numpy as np
import Tkinter as tk
import math

# kalman



#mass = 1.5
#g = np.array([[9.81]])
#hover_per = 0.1
#max_force = mass*g/hover_per
#xx = np.array([[hover_per],[0.0]])
##P = np.array([[0.5*0.5,0.0],[0.0,1.0*1.0]])
#P = 1*np.array([[0.01**2,0.0],[0.0,0.01**2]])
#Q = 1.0*np.array([[0.000065**2,0.0],[0.0,0.001**2]])
#F = np.array([[1.0,0.0],[-1.0*max_force/mass,0.0]])
#B = np.array([[0.0],[max_force/mass]])
#H = np.transpose(np.array([[0.0],[1.0]]))
#R = 0.1*np.array([[0.8*0.8]])




#def process(u):
#	global xx,P,Q,F,B
#	xx = np.dot(F, xx)+B*u
#	P = np.dot(np.dot(F, P), np.transpose(F)) + Q

#def update(a):
#	global xx,P,Q,F,B
#	z1 = a - g
#	y = z1 - np.dot(H, xx)
#	k = np.dot(P, np.transpose(H)) * np.linalg.inv((np.dot(np.dot(H, P), np.transpose(H)) + R))
#	xx = xx + k*y
#	P = np.dot((np.identity(2)-np.dot(k, H)), P) 








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
##plt.plot(t, record_hovper_w,'r')
##plt.xlabel('t/s')
##plt.ylabel('hover_per')
##plt.grid()
##plt.legend(['body','world'])

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




#AEKF


_hover_thr = 0.1
_gate_size = 3.0
_state_var = 0.01
_process_var = 12.5e-6
_acc_var = 5.0
_acc_var_scale = 1.0
_dt = 0.02
_innov = 0.0
_innov_var = 0.0
_innov_test_ratio = 0.0
_residual_lpf = 0.0
_signed_innov_test_ratio_lpf = 0.0
_noise_learning_time_constant = 2.0
_lpf_time_constant = 1.0
K = 0.0





def limit_range(x, a, b):
	if(x<=a):
		return a
	elif(x>=a and x<=b):
		return x
	else:
		return b

def sign(x):
	if x>=0: return 1.0
#	elif x==0: return 0.0
	else: return -1.0

def computeH(thrust):
	global _hover_thr
	return -9.8 * thrust / (_hover_thr * _hover_thr)
	
def computeInnovVar(H):
	global _acc_var, _acc_var_scale, _state_var
	R = _acc_var * _acc_var_scale
	P = _state_var
	return max(H * P * H + R, R)

def computePredictedAccZ(thrust):
	global _hover_thr
	return 9.8 * thrust / _hover_thr - 9.8

def computeInnov(acc_z, thrust):
	predicted_acc_z = computePredictedAccZ(thrust)
	return acc_z - predicted_acc_z
	
def computeKalmanGain(H, innov_var):
	global _state_var
	return _state_var * H / innov_var

def computeInnovTestRatio(innov, innov_var):
	global _gate_size
	return innov * innov / (_gate_size * _gate_size * innov_var)

def isTestRatioPassing(innov_test_ratio):
	return innov_test_ratio < 1.0;

def updateState(K, innov):
	global _hover_thr
	_hover_thr = _hover_thr + K * innov;
	_hover_thr = limit_range(_hover_thr, 0.1, 0.9)

def updateStateCovariance(K, H):
	global _state_var
	_state_var = (1.0 - K * H) * _state_var
	_state_var = limit_range(_state_var, 1e-10, 1.0)

def isLargeOffsetDetected():
	global _signed_innov_test_ratio_lpf
	return abs(_signed_innov_test_ratio_lpf) > 0.2

def bumpStateVariance():
	global _state_var, _process_var, _dt
	_state_var += 1e3 * _process_var * _dt * _dt

def updateLpf(residual, signed_innov_test_ratio):
	global _dt, _lpf_time_constant, _residual_lpf, _signed_innov_test_ratio_lpf
	alpha = _dt / (_lpf_time_constant + _dt)
	_residual_lpf = (1.0 - alpha) * _residual_lpf + alpha * residual
	signed_innov_test_ratio = limit_range(signed_innov_test_ratio, -1.0, 1.0)
	_signed_innov_test_ratio_lpf = (1.0 - alpha) * _signed_innov_test_ratio_lpf + alpha * signed_innov_test_ratio
	
def updateMeasurementNoise(residual, H):
	global _dt, _noise_learning_time_constant, _residual_lpf, _state_var, _acc_var, _process_var
	alpha = _dt / (_noise_learning_time_constant + _dt)
	res_no_bias = residual - _residual_lpf
	P = _state_var
	alpha = 0.9
	_acc_var = (1.0 - alpha) * _acc_var  + alpha * (res_no_bias * res_no_bias + H * P * H)
#	_process_var = (1.0 - alpha) * _process_var + alpha * (K * K * _innov * _innov)
	_acc_var = limit_range(_acc_var, 1.0, 400.0)

def predict(dt):
	global _state_var, _dt
	_state_var = _state_var + _process_var * dt * dt
	_dt = dt


def fuseAccZ(acc_z, thrust):
	global _innov_var, _innov, _innov_test_ratio, K
	H = computeH(thrust)
	innov_var = computeInnovVar(H)
	innov = computeInnov(acc_z, thrust)
	K = computeKalmanGain(H, innov_var)
	innov_test_ratio = computeInnovTestRatio(innov, innov_var)

	residual = innov
	
	updateState(K, innov)
	updateStateCovariance(K, H)
	residual = computeInnov(acc_z, thrust)

	if(isTestRatioPassing(innov_test_ratio)):
		updateState(K, innov)
		updateStateCovariance(K, H)
		residual = computeInnov(acc_z, thrust)
	elif (isLargeOffsetDetected()):
		bumpStateVariance()

#	signed_innov_test_ratio = sign(innov) * innov_test_ratio
#	updateLpf(residual, signed_innov_test_ratio)
#	updateMeasurementNoise(residual, H)

	_innov = innov
	_innov_var = innov_var
	_innov_test_ratio = innov_test_ratio


startime = 0
folderName = '1206night8'
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
	
#u
u = []
lines = log_u_thr.readlines()
for line in lines:
	index = line.find('/')
	u.append(float(line[index+1:-1]))
	
#acc_z
acc_z = []
lines = log_acc_z.readlines()
for line in lines:  
	acc_z.append(float(line))

record_hovper = []
q = []
r = []
for index in range(len(t)):
	if t[index]>startime:
		predict(0.02)
		fuseAccZ(acc_z[index], u[index])
		record_hovper.append(_hover_thr)
		q.append(_process_var)
		r.append(_acc_var)
		
plt.subplot(311)
plt.plot(t, record_hovper,'b')
plt.grid()

plt.subplot(312)
plt.plot(t, q,'r')
plt.grid()

plt.subplot(313)
plt.plot(t, r,'b')
plt.grid()


plt.show()












