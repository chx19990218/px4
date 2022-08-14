import matplotlib.pyplot as plt
import os
import numpy as np
import Tkinter as tk
import math


des_p_x = []
odom_p_x = []
des_p_y = []
odom_p_y = []
des_p_z = []
odom_p_z = []
des_v_x = []
odom_v_x = []
des_v_y = []
odom_v_y = []
des_v_z = []
odom_v_z = []
des_yaw = []
odom_yaw = []
rc_roll = []
u_roll = []
rc_pitch = []
u_pitch = []
rc_yaw = []
u_yaw = []
rc_thr = []
u_thr = []
hov = []
t = []
imu_w = []
imu_x = []
imu_y = []
imu_z = []
odom_w = []
odom_x = []
odom_y = []
odom_z = []
imu_a_x = []
imu_a_y = []
imu_a_z = []
target_p_x = []
target_v_x = []
target_p_y = []
target_v_y = []
eso_p_x = []
eso_v_x = []
eso_d_x = []
eso_p_y = []
eso_v_y = []
eso_d_y = []

def px_callback():
	global plot_index 
	plot_index = 0
	message.set('********We will plot des.p.x/odom.p.x/eso.p.x********')
def py_callback():
	global plot_index 
	plot_index = 1
	message.set('********We will plot des.p.y/odom.p.y/eso.p.y********')
def pz_callback():
	global plot_index 
	plot_index = 2
	message.set('********We will plot des.p.z/odom.p.z********')
def vx_callback():
	global plot_index 
	plot_index = 3
	message.set('********We will plot des.v.x/odom.v.x/eso.v.x********')
def vy_callback():
	global plot_index 
	plot_index = 4
	message.set('********We will plot des.v.y/odom.v.y/eso.v.y********')
def vz_callback():
	global plot_index 
	plot_index = 5
	message.set('********We will plot des.v.z/odom.v.z********')
def rc_u_roll_callback():
	global plot_index 
	plot_index = 6
	message.set('********We will plot rc_data.roll/u.roll/imu_roll/odom_roll********')
def rc_u_pitch_callback():
	global plot_index 
	plot_index = 7
	message.set('********We will plot rc_data.pitch/u.pitch/imu_pitch/odom_pitch********')
def rc_u_yaw_callback():
	global plot_index 
	plot_index = 8
	message.set('********We will plot rc_data.yaw/u.yaw/imu_yaw/odom_yaw********')
def rc_u_thr_callback():
	global plot_index 
	plot_index = 9
	message.set('********We will plot rc_data.thr/u.thr********')
def hovper_callback():
	global plot_index
	plot_index = 10
	message.set('********We will plot hov_percent********')
def acc_callback():
	global plot_index
	plot_index = 11
	message.set('********We will plot acc********')
def traj_callback():
	global plot_index
	plot_index = 12
	message.set('********We will plot trajectory********')



def plot_callback():
	fileName = textinput.get()
	logPath = os.path.abspath('.')
	
	try:
		integrated_log_Path = logPath + '/' + fileName + '.txt'
		print(integrated_log_Path)
		log = open(integrated_log_Path,"r")
	except:
		integrated_log_Path = logPath + '/' + fileName
		log = open(integrated_log_Path,"r")
	else:
		print('No data wanted!')

 	
	count = 0
	lines = log.readlines()
	for line in lines:
#		for param
		if count<2:
			count = count + 1
			continue
		index1 = line.find('/')
		des_p_x.append(float(line[0:index1]))
		
		index2 = line.find('/', index1+1, len(line))
		odom_p_x.append(float(line[index1+1:index2]))
		
		index3 = line.find('/', index2+1, len(line))
		des_p_y.append(float(line[index2+1:index3]))
		
		index4 = line.find('/', index3+1, len(line))
		odom_p_y.append(float(line[index3+1:index4]))
		
		index5 = line.find('/', index4+1, len(line))
		des_p_z.append(float(line[index4+1:index5]))
		
		index6 = line.find('/', index5+1, len(line))
		odom_p_z.append(float(line[index5+1:index6]))
		
		index7 = line.find('/', index6+1, len(line))
		des_v_x.append(float(line[index6+1:index7]))
		
		index8 = line.find('/', index7+1, len(line))
		odom_v_x.append(float(line[index7+1:index8]))
		
		index9 = line.find('/', index8+1, len(line))
		des_v_y.append(float(line[index8+1:index9]))
		
		index10 = line.find('/', index9+1, len(line))
		odom_v_y.append(float(line[index9+1:index10]))
		
		index11 = line.find('/', index10+1, len(line))
		des_v_z.append(float(line[index10+1:index11]))
		
		index12 = line.find('/', index11+1, len(line))
		odom_v_z.append(float(line[index11+1:index12]))
		
		index13 = line.find('/', index12+1, len(line))
		des_yaw.append(float(line[index12+1:index13]))
		
		index14 = line.find('/', index13+1, len(line))
#		odom_yaw.append(float(line[index13+1:index14]))
		
		index15 = line.find('/', index14+1, len(line))
		rc_roll.append(float(line[index14+1:index15]))
		
		index16 = line.find('/', index15+1, len(line))
		u_roll.append(float(line[index15+1:index16]))
		
		index17 = line.find('/', index16+1, len(line))
		rc_pitch.append(float(line[index16+1:index17]))
		
		index18 = line.find('/', index17+1, len(line))
		u_pitch.append(float(line[index17+1:index18]))
		
		index19 = line.find('/', index18+1, len(line))
		rc_yaw.append(float(line[index18+1:index19]))
		
		index20 = line.find('/', index19+1, len(line))
		u_yaw.append(float(line[index19+1:index20]))
		
		index21 = line.find('/', index20+1, len(line))
		rc_thr.append(float(line[index20+1:index21]))
		
		index22 = line.find('/', index21+1, len(line))
		u_thr.append(float(line[index21+1:index22]))
		
		index23 = line.find('/', index22+1, len(line))
		hov.append(float(line[index22+1:index23]))
		
		index24 = line.find('/', index23+1, len(line))
		t.append(float(line[index23+1:index24]))
		
		index25 = line.find('/', index24+1, len(line))
		imu_w.append(float(line[index24+1:index25]))
		
		index26 = line.find('/', index25+1, len(line))
		imu_x.append(float(line[index25+1:index26]))
		
		index27 = line.find('/', index26+1, len(line))
		imu_y.append(float(line[index26+1:index27]))
		
		index28 = line.find('/', index27+1, len(line))
		imu_z.append(float(line[index27+1:index28]))
		
		index29 = line.find('/', index28+1, len(line))
		odom_w.append(float(line[index28+1:index29]))
		
		index30 = line.find('/', index29+1, len(line))
		odom_x.append(float(line[index29+1:index30]))
		
		index31 = line.find('/', index30+1, len(line))
		odom_y.append(float(line[index30+1:index31]))
		
		index32 = line.find('/', index31+1, len(line))
		odom_z.append(float(line[index31+1:index32]))
		
		index33 = line.find('/', index32+1, len(line))
		imu_a_x.append(float(line[index32+1:index33]))
		
		index34 = line.find('/', index33+1, len(line))
		imu_a_y.append(float(line[index33+1:index34]))
		
		index35 = line.find('/', index34+1, len(line))
		imu_a_z.append(float(line[index34+1:index35]))
		
		index36 = line.find('/', index35+1, len(line))
		target_p_x.append(float(line[index35+1:index36]))
		
		index37 = line.find('/', index36+1, len(line))
		target_v_x.append(float(line[index36+1:index37]))
		
		index38 = line.find('/', index37+1, len(line))
		target_p_y.append(float(line[index37+1:index38]))
		
		index39 = line.find('/', index38+1, len(line))
		target_v_y.append(float(line[index38+1:index39]))
		
		index40 = line.find('/', index39+1, len(line))
		eso_p_x.append(float(line[index39+1:index40]))
		
		index41 = line.find('/', index40+1, len(line))
		eso_v_x.append(float(line[index40+1:index41]))
		
		index42 = line.find('/', index41+1, len(line))
		eso_d_x.append(float(line[index41+1:index42]))
		
		index43 = line.find('/', index42+1, len(line))
		eso_p_y.append(float(line[index42+1:index43]))
		
		index44 = line.find('/', index43+1, len(line))
		eso_v_y.append(float(line[index43+1:index44]))
		
		index45 = line.find('/', index44+1, len(line))
		eso_d_y.append(float(line[index44+1:index45]))
		
		
	if plot_index == 0:
		plt.figure()
		plt.xlabel("t/s")
		plt.ylabel("p_x/m")
		plt.grid()
		
		plt.plot(t, des_p_x, 'r')
		plt.plot(t, odom_p_x, 'b')
		plt.plot(t, eso_p_x, 'g')
		
		plt.legend(["des_p_x", "real_p_x", "eso_p_x"])
	
	if plot_index == 1:
		plt.figure()
		plt.xlabel("t/s")
		plt.ylabel("p_y/m")
		plt.grid()
		
		plt.plot(t, des_p_y, 'r')
		plt.plot(t, odom_p_y, 'b')
		plt.plot(t, eso_p_y, 'g')
		
		plt.legend(["des_p_y", "real_p_y", "eso_p_y"])
		
	if plot_index == 2:
		plt.figure()
		plt.xlabel("t/s")
		plt.ylabel("p_z/m")
		plt.grid()
		
		plt.plot(t, des_p_z, 'r')
		plt.plot(t, odom_p_z, 'b')
		
		plt.legend(["des_p_z", "real_p_z"])
		
	if plot_index == 3:
		plt.figure()
		plt.xlabel("t/s")
		plt.ylabel("v_x / m/s")
		plt.grid()
		
		plt.plot(t, des_v_x, 'r')
		plt.plot(t, odom_v_x, 'b')
		plt.plot(t, eso_v_x, 'g')
		
		plt.legend(["des_v_x", "real_v_x", "eso_v_x"])
	
	if plot_index == 4:
		plt.figure()
		plt.xlabel("t/s")
		plt.ylabel("v_y / m/s")
		plt.grid()
		
		plt.plot(t, des_v_y, 'r')
		plt.plot(t, odom_v_y, 'b')
		plt.plot(t, eso_v_y, 'g')
		
		plt.legend(["des_v_y", "real_v_y", "eso_v_y"])
		
	if plot_index == 5:
		plt.figure()
		plt.xlabel("t/s")
		plt.ylabel("v_z / m/s")
		plt.grid()
		
		plt.plot(t, des_v_z, 'r')
		plt.plot(t, odom_v_z, 'b')
		
		plt.legend(["des_v_z", "real_v_z"])
		
	

	if plot_index == 6 or plot_index == 7 or plot_index == 8:
		imu_roll = []
		imu_pitch = []
		imu_yaw = []
		
		odom_roll = []
		odom_pitch = []
		odom_yaw = []
		
		for i in range(len(t)):
			imu_roll.append(math.atan2(2 * (imu_w[i] * imu_x[i] + imu_y[i] * imu_z[i]), 1 - 2 * (imu_x[i] * imu_x[i] + imu_y[i] * imu_y[i]))/3.14*180.0)
			imu_pitch.append(math.asin(2 * (imu_w[i] * imu_y[i] - imu_z[i] * imu_x[i]))/3.14*180)
			imu_yaw.append(math.atan2(2 * (imu_w[i]* imu_z[i] + imu_x[i] * imu_y[i]), 1 - 2 * (imu_y[i] * imu_y[i] + imu_z[i] * imu_z[i]))/3.14*180)
			
			odom_roll.append(math.atan2(2 * (odom_w[i] * odom_x[i] + odom_y[i] * odom_z[i]), 1 - 2 * (odom_x[i] * odom_x[i] + odom_y[i] * odom_y[i]))/3.14*180.0)
			odom_pitch.append(math.asin(2 * (odom_w[i] * odom_y[i] - odom_z[i] * odom_x[i]))/3.14*180)
			odom_yaw.append(math.atan2(2 * (odom_w[i]* odom_z[i] + odom_x[i] * odom_y[i]), 1 - 2 * (odom_y[i] * odom_y[i] + odom_z[i] * odom_z[i]))/3.14*180)
		if plot_index == 6:
			plt.figure()
			plt.xlabel("t/s")
			plt.ylabel("roll/deg")
			plt.grid()
			plt.plot(t, u_roll, 'r')
			plt.plot(t, imu_roll, 'b')
			plt.plot(t, odom_roll, 'g')
			plt.plot(t, rc_roll, 'y')
		
			plt.legend(["des_roll", "imu_yaw", "odom_roll", "rc_roll"])
			
		if plot_index == 7:
			plt.figure()
			plt.xlabel("t/s")
			plt.ylabel("pitch/deg")
			plt.grid()
			plt.plot(t, u_pitch, 'r')
			plt.plot(t, imu_pitch, 'b')
			plt.plot(t, odom_pitch, 'g')
			plt.plot(t, rc_pitch, 'y')
		
			plt.legend(["des_pitch", "imu_pitch", "odom_pitch", "rc_pitch"])
			
		if plot_index == 8:
			plt.figure()
			plt.xlabel("t/s")
			plt.ylabel("yaw/deg")
			plt.grid()
			plt.plot(t, u_yaw, 'r')
			plt.plot(t, imu_yaw, 'b')
			plt.plot(t, odom_yaw, 'g')
			plt.plot(t, rc_yaw, 'y')
		
			plt.legend(["des_yaw", "imu_yaw", "odom_yaw", "rc_yaw"])
		
	if plot_index == 9:
		plt.figure()
		plt.xlabel("t/s")
		plt.ylabel("thr/per")
		plt.grid()
		plt.plot(t, u_thr, 'r')
		plt.plot(t, rc_thr, 'y')
	
		plt.legend(["u_thr", "rc_pitch"])
	
	if plot_index == 10:
		plt.figure()
		plt.xlabel("t/s")
		plt.ylabel("hov/per")
		plt.grid()
		plt.plot(t, hov, 'r')
	
		plt.legend(["hover_percent"])
		
	if plot_index == 11:
		plt.figure()
		plt.xlabel("t/s")
		plt.ylabel("acc / m/s^2")
		
		plt.subplot(311)
		plt.plot(t, imu_a_x, 'r')
		plt.grid()
		plt.legend(['acc_x'])
		
		plt.subplot(312)
		plt.plot(t, imu_a_y, 'r')
		plt.grid()
		plt.legend(['acc_y'])
		
		plt.subplot(313)
		plt.plot(t, imu_a_z, 'r')
		plt.grid()
		plt.legend(['acc_z'])
	
	if plot_index == 12:
		plt.figure()
		plt.xlabel("x/m")
		plt.ylabel("y/m")
		plt.plot(odom_p_x, odom_p_y, 'r')
		plt.plot(target_p_x, target_p_y, 'r')
		plt.grid()
	
		plt.legend(["real", "target"])
	
	plt.show()
	


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


mass = 1.5
g = np.array([[9.81]])
hover_per = 0.1
max_force = mass*g/hover_per
xx = np.array([[hover_per],[0.0]])
P = 1*np.array([[0.01**2,0.0],[0.0,0.01**2]])
Q = 1.0*np.array([[0.000065**2,0.0],[0.0,0.001**2]])
F = np.array([[1.0,0.0],[-1.0*max_force/mass,0.0]])
B = np.array([[0.0],[max_force/mass]])
H = np.transpose(np.array([[0.0],[1.0]]))
R = 0.1*np.array([[0.8*0.8]])
	
def kalman_hovper():
	global xx,P
	startime = float(startime_input.get())
	folderName = textinput.get()
	logPath = os.path.abspath('.')
	folderPath = logPath + '/' + folderName;

	#kalman
	record_hovper = []
	for index in range(len(t)):
		a = imu_a_z[index]
		u = u_thr[index]
		if t[index]>startime:
			update(a)
			process(u)
		record_hovper.append(xx[0])

	plt.figure()
	plt.plot(t, record_hovper,'r')
	plt.xlabel('t/s')
	plt.ylabel('hover_per')
	plt.grid()
	plt.show()


def plot_lmpc():
	print("no function")






frame = tk.Tk()
frame.title('Visulization')
frame.geometry('500x200+1000+400')

bigmenu = tk.Menu(frame)
datamenu = tk.Menu(bigmenu,tearoff = 0)
datamenu.add_command(label='des.p.x/odom.p.x/eso.p.x', command=px_callback)
datamenu.add_command(label='des.p.y/odom.p.y/eso.p.y', command=py_callback)
datamenu.add_command(label='des.p.z/odom.p.z', command=pz_callback)
datamenu.add_separator()
datamenu.add_command(label='des.v.x/odom.v.x/eso.v.x', command=vx_callback)
datamenu.add_command(label='des.v.y/odom.v.y/eso.v.x', command=vy_callback)
datamenu.add_command(label='des.v.z/odom.v.z', command=vz_callback)
datamenu.add_separator()
datamenu.add_command(label='u.roll/imu_roll/odom_roll/rc_data.roll', command=rc_u_roll_callback)
datamenu.add_command(label='u.pitch/imu_pitch/odom_pitch/rc_data.pitch', command=rc_u_pitch_callback)
datamenu.add_command(label='u.yaw/imu_yaw/odom_yaw/rc_data.yaw', command=rc_u_yaw_callback)
datamenu.add_command(label='rc_data.thr/u.thrust', command=rc_u_thr_callback)
datamenu.add_separator()
datamenu.add_command(label='hovper', command=hovper_callback)
datamenu.add_separator()
datamenu.add_command(label='acc', command=acc_callback)
datamenu.add_separator()
datamenu.add_command(label='trajectory', command=traj_callback)

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
