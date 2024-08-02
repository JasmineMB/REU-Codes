# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:34:07 2024

@author: MIRIA
"""

import matplotlib.pyplot as plt
import numpy as np

fpath = "D:\\PythonFiles\\REU\\RepositoryData - standard units.txt"

name_list = []
egw_list = []
freq_list = []
eff50_list = []
eff10_list = []
rotate_list = []
vel_list = []
mass_list = []
dur_list = []

with open(fpath) as fp:
    for i, line in enumerate(fp):
        line_split = line.split()
        if i > 0:
            name_list.append(str(line_split[1]))
            egw_list.append(float(line_split[2]))
            freq_list.append(int(line_split[3]))
            eff50_list.append(float(line_split[4]))
            eff10_list.append(float(line_split[5]))
            rotate_list.append(bool(float(line_split[6])))
            vel_list.append(float(line_split[6]))
            mass_list.append(float(line_split[7]))
            dur_list.append(float(line_split[8]))
            
            
arr_name = np.array(name_list)
arr_egw = np.array(egw_list)
arr_freq = np.array(freq_list)
arr_eff50 = np.array(eff50_list)
arr_eff10 = np.array(eff10_list)
arr_mass = np.array(mass_list)
arr_dur = np.array(dur_list)
arr_vel = np.array(vel_list)

'''
###############################################################################
Normalization using log
###############################################################################
'''

log_vel = []

for x in arr_vel:
    if x == 0:
        log_vel.append(x)
    else:
        log_vel.append(np.log(x))

log_egw = np.log(arr_egw)
log_freq = np.log(arr_freq)
log_dur = np.log(arr_dur)
log_mass = np.log(arr_mass)

m_egw = np.mean(log_egw)
m_freq = np.mean(log_freq)
m_dur = np.mean(log_dur)
m_mass = np.mean(log_mass)
m_vel = np.mean(log_vel)

std_egw = np.std(log_egw)
std_freq = np.std(log_freq)
std_dur = np.std(log_dur)
std_mass = np.std(log_mass)
std_vel = np.std(log_vel)

norm_egw = (log_egw - m_egw) / std_egw
norm_freq = (log_freq - m_freq) / std_freq
norm_dur = (log_dur - m_dur) / std_dur
norm_mass = (log_mass - m_mass) / std_mass
norm_vel = (log_vel - m_vel) / std_vel

metrics4 = np.sqrt(np.square(norm_egw) + np.square(norm_freq) + np.square(norm_dur) + np.square(norm_mass))
metrics5 = np.sqrt(np.square(norm_egw) + np.square(norm_freq) + np.square(norm_dur) + np.square(norm_mass) + np.square(norm_vel))


'''
###############################################################################
Normalization using division
###############################################################################
'''

min_egw = min(arr_egw)
min_freq = min(arr_freq)
min_eff50 = min(arr_eff50)
min_eff10 = min(arr_eff10)
min_mass = min(arr_mass)
min_dur = min(arr_dur)
min_vel = min(arr_vel)

r_egw = max(arr_egw) - min(arr_egw)
r_freq = max(arr_freq) - min(arr_freq)
r_eff50 = max(arr_eff50) - min(arr_eff50)
r_eff10 = max(arr_eff10) - min(arr_eff10)
r_mass = max(arr_mass) - min(arr_mass)
r_dur = max(arr_dur) - min(arr_dur)
r_vel = max(arr_vel) - min(arr_vel)


normd_egw = (arr_egw - min_egw) / r_egw
normd_freq = (arr_freq - min_freq) / r_freq
normd_dur = (arr_dur - min_dur) / r_dur
normd_mass = (arr_mass - min_mass) / r_mass
normd_vel = (arr_vel - min_vel) / r_vel

metrics4d = np.sqrt(np.square(normd_egw) + np.square(normd_freq) 
                    + np.square(normd_dur) + np.square(normd_mass))

metrics5d = np.sqrt(np.square(normd_egw) + np.square(normd_freq)
                    + np.square(normd_dur) + np.square(normd_mass)
                    + np.square(normd_vel))

'''
###############################################################################
Rotating vs. Nonrotating points
###############################################################################
'''

metrics4d_y = []
metrics5d_y = []
ang_vel = []
eff10_y = []
eff50_y = []
egw_y = []

metrics4d_n = []
metrics5d_n = []
vel_0 = []
eff10_n = []
eff50_n = []
egw_n = []

for x in enumerate(rotate_list):
    i = x[0]
    if rotate_list[i] == True:
        metrics4d_y.append(metrics4d[i])
        metrics5d_y.append(metrics5d[i])
        ang_vel.append(arr_vel[i])
        eff10_y.append(arr_eff10[i])
        eff50_y.append(arr_eff50[i])
        egw_y.append(arr_egw[i])
        
    else:
        metrics4d_n.append(metrics4d[i])
        metrics5d_n.append(metrics5d[i])
        vel_0.append(arr_vel[i])
        eff10_n.append(arr_eff10[i])
        eff50_n.append(arr_eff50[i])
        egw_n.append(arr_egw[i])


'''
###############################################################################
Other Plots
###############################################################################
'''

print('other plots')
# Energy vs Distance standard units
plt.figure()
plt.plot(eff10_y, egw_y, 'r*', label = '10% & rotating')
plt.plot(eff10_n, egw_n, 'ro', label = '10% & nonrotating')
plt.plot(eff50_y, egw_y, 'b*', label = '50% & rotating')
plt.plot(eff50_n, egw_n, 'bo', label = '50% & nonrotating')
plt.legend()
plt.title('Energy vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Energy of GW (M\u2609c^2)')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.axvline(4)
plt.show()

# Angular Velocity vs Distance 50%
plt.figure()
plt.plot(eff50_y, ang_vel, 'bo', label = '50% efficiency')
plt.legend()
plt.title('Angular Velocity vs. Distance (50%)')
plt.xlabel('Distance (kpc)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid(True)
plt.xscale('log')
plt.show()

# Angular Velocity vs Distance 10%
plt.figure()
plt.plot(eff10_y, ang_vel, 'ro', label = '10% efficiency')
plt.legend()
plt.title('Angular Velocity vs. Distance (10%)')
plt.xlabel('Distance (kpc)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid(True)
plt.xscale('log')
plt.show()

# 3D plot Distance, Angular Velocity and GW Energy
plt.figure(figsize = (8, 4.5))
ax = plt.axes(projection ="3d")
ax.scatter3D(eff50_y, egw_y, ang_vel, color = "green")
plt.title('Distance, Angular Velocity, and EGW (50%)')
plt.xlabel('Distance (kpc)')
plt.show()

plt.figure()
plt.plot(egw_n, vel_0, 'ro', label = 'nonrotating')
plt.plot(egw_y, ang_vel, 'bo', label = 'rotating')
plt.legend()
plt.title('Angular Velocity vs. Energy')
plt.xlabel('Energy (J)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid(True)
plt.xscale('log')
plt.show()

plt.figure()
plt.plot(eff50_y, ang_vel, 'bo', label = 'rotating')
plt.plot(eff50_n, vel_0, 'ro', label = 'nonrotating')
plt.title('Angular Velocity vs Distance (50%)')
plt.xlabel('Distance (kpc)')
plt.ylabel('Angular Velocity (rad/s)')
plt.xscale('log')
plt.grid(True)
plt.legend()
plt.show()
