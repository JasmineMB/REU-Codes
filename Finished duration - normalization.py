# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 06:04:05 2025

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
dur_yn = []

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
            dur_yn.append(bool(int(line_split[9])))
            
            
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
                    + np.square(normd_mass))

metrics5d = np.sqrt(np.square(normd_egw) + np.square(normd_freq)
                    + np.square(normd_mass) + np.square(normd_vel))

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

for x, y in zip(enumerate(dur_yn), enumerate(rotate_list)):
    i = x[0]
    j = y[0]
    if dur_yn[i] == True and rotate_list[j] == True:
        metrics4d_y.append(metrics4d[j])
        metrics5d_y.append(metrics5d[j])
        ang_vel.append(arr_vel[j])
        eff10_y.append(arr_eff10[j])
        eff50_y.append(arr_eff50[j])
        egw_y.append(arr_egw[j])
        
    elif dur_yn[i] == True and rotate_list[j] == False:
        metrics4d_n.append(metrics4d[j])
        metrics5d_n.append(metrics5d[j])
        vel_0.append(arr_vel[j])
        eff10_n.append(arr_eff10[j])
        eff50_n.append(arr_eff50[j])
        egw_n.append(arr_egw[j])


'''
###############################################################################
Plots using 4 parameters division
###############################################################################
'''
print('4 parameter normalization using division with no duration')
# Normalized Hyperparameter Coordinates of Energy, Frequency, Duration, and Mass vs. Distance
plt.figure()
plt.plot(eff10_y, metrics4d_y, 'r*', label = '10% & rotating')
plt.plot(eff10_n, metrics4d_n, 'ro', label = '10% & nonrotating')
plt.plot(eff50_y, metrics4d_y, 'b*', label = '50% & rotating')
plt.plot(eff50_n, metrics4d_n, 'bo', label = '50% & nonrotating')
plt.legend()
plt.title('Normalized 4 parameter Space vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Normalized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(4)
plt.show()

# Normalized Hyperparameter Coordinates of Energy, Frequency, Duration, and Mass vs. Distance at 10% efficiency
plt.figure()
plt.plot(eff10_y, metrics4d_y, 'ro', label = 'rotating')
plt.plot(eff10_n, metrics4d_n, 'bo', label = 'nonrotating')
plt.legend()
plt.title('Normalized 4 parameter Space vs. Distance (10% efficiency)')
plt.xlabel('Distance (kpc)')
plt.ylabel('Normalized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(4)
plt.show()

# Normalized Hyperparameter Coordinates of Energy, Frequency, Duration, and Mass vs. Distance at 50% efficiency
plt.figure()
plt.plot(eff50_y, metrics4d_y, 'ro', label = 'rotating')
plt.plot(eff50_n, metrics4d_n, 'bo', label = 'nonrotating')
plt.legend()
plt.title('Normalized 4 parameter Space vs. Distance (50% efficiency)')
plt.xlabel('Distance (kpc)')
plt.ylabel('Normalized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(4)
plt.show()

# Normalized Hyperparameter Coordinates of Energy, Frequency, Duration, and Mass vs. Distance only rotating
plt.figure()
plt.plot(eff10_y, metrics4d_y, 'ro', label = '10%')
plt.plot(eff50_y, metrics4d_y, 'bo', label = '50%')
plt.legend()
plt.title('Normalized 4 parameter Space (rotating) vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Normalized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(4)
plt.show()

# Normalized Hyperparameter Coordinates only non rotating
plt.figure()
plt.plot(eff10_n, metrics4d_n, 'ro', label = '10%')
plt.plot(eff50_n, metrics4d_n, 'bo', label = '50%')
plt.legend()
plt.title('Normalized 4 parameter Space (nonrotating) vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Normalized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(4)
plt.show()

'''
###############################################################################
Plots using 5 parameters division
###############################################################################
'''
print('5 parameter normalization using division with no duration')
# Normalized Hyperparameter Coordinates of Energy, Frequency, Duration, Mass, and Angular Velocity vs. Distance
plt.figure()
plt.plot(eff10_y, metrics5d_y, 'r*', label = '10% & rotating')
plt.plot(eff10_n, metrics5d_n, 'ro', label = '10% & nonrotating')
plt.plot(eff50_y, metrics5d_y, 'b*', label = '50% & rotating')
plt.plot(eff50_n, metrics5d_n, 'bo', label = '50% & nonrotating')
plt.legend()
plt.title('Normalized 5 parameter Space vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Normalized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(4)
plt.show()

# Normalized Hyperparameter Coordinates of Energy, Frequency, Duration, Mass, and Angular Velocity vs. Distance at 10% efficiency
plt.figure()
plt.plot(eff10_y, metrics5d_y, 'ro', label = 'rotating')
plt.plot(eff10_n, metrics5d_n, 'bo', label = 'nonrotating')
plt.legend()
plt.title('Normalized 5 parameter Space vs. Distance (10% efficiency)')
plt.xlabel('Distance (kpc)')
plt.ylabel('Normalized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(4)
plt.show()

# Normalized Hyperparameter Coordinates of Energy, Frequency, Duration, Mass, and Angular Velocity vs. Distance at 50% efficiency
plt.figure()
plt.plot(eff50_y, metrics5d_y, 'ro', label = 'rotating')
plt.plot(eff50_n, metrics5d_n, 'bo', label = 'nonrotating')
plt.legend()
plt.title('Normalized 5 parameter Space vs. Distance (50% efficiency)')
plt.xlabel('Distance (kpc)')
plt.ylabel('Normalized Hyperparameter Coordinates')
plt.grid(True)
plt.axvline(10)
plt.show()

# Normalized Hyperparameter Coordinates of Energy, Frequency, Duration, Mass, and Angular Velocity vs. Distance only rotating
plt.figure()

plt.scatter(eff10_y, metrics5d_y, color = 'r', label = '10%')
plt.scatter(eff50_y, metrics5d_y, color = 'b', label = '50%')

m10, b10 = np.polyfit(eff10_y, metrics5d_y, 1)
plt.plot(eff10_y, m10*np.array(eff10_y) + b10, color='magenta')

m50, b50 = np.polyfit(eff50_y, metrics5d_y, 1)
plt.plot(eff50_y, m50*np.array(eff50_y) + b50, color='cyan')

plt.legend()
plt.title('Normalized  5 parameter Space (rotating) vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Normalized Hyperparameter Coordinates')
plt.grid(True)
#plt.xscale('log')
plt.axvline(10)
plt.show()