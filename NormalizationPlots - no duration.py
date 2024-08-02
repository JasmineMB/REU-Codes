# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:20:14 2024

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
Normalization using division
###############################################################################
'''

min_egw = min(arr_egw)
min_freq = min(arr_freq)
min_eff50 = min(arr_eff50)
min_eff10 = min(arr_eff10)
min_mass = min(arr_mass)
min_vel = min(arr_vel)

r_egw = max(arr_egw) - min(arr_egw)
r_freq = max(arr_freq) - min(arr_freq)
r_eff50 = max(arr_eff50) - min(arr_eff50)
r_eff10 = max(arr_eff10) - min(arr_eff10)
r_mass = max(arr_mass) - min(arr_mass)
r_vel = max(arr_vel) - min(arr_vel)


normd_egw = (arr_egw - min_egw) / r_egw
normd_freq = (arr_freq - min_freq) / r_freq
normd_mass = (arr_mass - min_mass) / r_mass
normd_vel = (arr_vel - min_vel) / r_vel

metrics4d = np.sqrt(np.square(normd_egw) + np.square(normd_freq) 
                    + np.square(normd_mass) + np.square(normd_vel))

'''
###############################################################################
Rotating vs. Nonrotating points
###############################################################################
'''

metrics4d_y = []
ang_vel = []
eff10_y = []
eff50_y = []
egw_y = []

metrics4d_n = []
vel_0 = []
eff10_n = []
eff50_n = []
egw_n = []

for x in enumerate(rotate_list):
    i = x[0]
    if rotate_list[i] == True:
        metrics4d_y.append(metrics4d[i])
        ang_vel.append(arr_vel[i])
        eff10_y.append(arr_eff10[i])
        eff50_y.append(arr_eff50[i])
        egw_y.append(arr_egw[i])
        
    else:
        metrics4d_n.append(metrics4d[i])
        vel_0.append(arr_vel[i])
        eff10_n.append(arr_eff10[i])
        eff50_n.append(arr_eff50[i])
        egw_n.append(arr_egw[i])

'''
###############################################################################
Plots using 4 parameters division
###############################################################################
'''
print('4 parameter normalization using division')
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

