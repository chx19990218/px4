import matplotlib.pyplot as plt
import os
import numpy as np
import Tkinter as tk
import math


folderName = '1210night4'
logPath = os.path.abspath('.')
folderPath = logPath + '/' + folderName;

log_t_Path = folderPath + '/' + 'log_t.txt'
log_p_x_Path = folderPath + '/' + 'log_p_x.txt'
log_p_y_Path = folderPath + '/' + 'log_p_y.txt'
log_v_x_Path = folderPath + '/' + 'log_v_x.txt'
log_v_y_Path = folderPath + '/' + 'log_v_y.txt'
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
log_p_x = open(log_p_x_Path,"r")
log_p_y = open(log_p_y_Path,"r")
log_v_x = open(log_v_x_Path,"r")
log_v_y = open(log_v_y_Path,"r")




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


uav_des_x = []
uav_des_y = []
uav_des_vx = []
uav_des_vy = []

uav_x = []
uav_y = []
uav_vx = []
uav_vy = []

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


d = []

w0 = 5
inter = 0.01
b0 = 1.0
A = np.array([[-3*w0, 1.0, 0.0], [-3*w0*w0, 0.0, 1.0], [-w0*w0*w0, 0, 0]])
B = np.array([[0, 3*w0], [b0, 3*w0*w0], [0, w0*w0*w0]])
#A = np.array([[-4*w0, 1.0, 0.0, 0.0], [-6*w0*w0, 0.0, 1.0, 0.0], [-4*w0*w0*w0, 0, 0, 1.0], [-w0*w0*w0*w0, 0.0, 0.0, 0.0]])
#B = np.array([[0, 4*w0], [0.0, 6*w0*w0], [b0, 4*w0*w0*w0], [0, w0*w0*w0*w0]])
I = np.identity(3)
Ak = A * inter + I
Bk = B * inter

obv_p = []
obv_v = []
obv_d = []


startime = 10
Z = np.array([0, 0 ,0])

for index in range(len(t)):
	if t[index]>startime:
		acc = 1.0 * (uav_des_vx[index] - uav_vx[index])
		u_y = np.array([acc, uav_x[index]])
		Z = Ak.dot(Z) + Bk.dot(u_y)
		obv_p.append(Z[0])
		obv_v.append(Z[1])
		obv_d.append(Z[2])
	else:
		obv_p.append(0.0)
		obv_v.append(0.0)
		obv_d.append(0.0)
		
plt.subplot(311)
plt.plot(t, obv_p,'b')
plt.plot(t, uav_y,'r')
plt.grid()

plt.subplot(312)
plt.plot(t, obv_v,'b')
plt.plot(t, uav_vx, 'r')
plt.plot(t, uav_des_vx, 'y')
plt.grid()

plt.subplot(313)
plt.plot(t, obv_d,'b')
plt.grid()


plt.show()












