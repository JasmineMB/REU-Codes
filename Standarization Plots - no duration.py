# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 07:08:01 2024

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
Standardization using log
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
log_mass = np.log(arr_mass)

m_egw = np.mean(log_egw)
m_freq = np.mean(log_freq)
m_mass = np.mean(log_mass)
m_vel = np.mean(log_vel)

std_egw = np.std(log_egw)
std_freq = np.std(log_freq)
std_mass = np.std(log_mass)
std_vel = np.std(log_vel)


stan_egw = (log_egw - m_egw) / std_egw
stan_freq = (log_freq - m_freq) / std_freq
stan_mass = (log_mass - m_mass) / std_mass
stan_vel = (log_vel - m_vel) / std_vel




'''
m_egw = np.mean(arr_egw)
m_freq = np.mean(arr_freq)
m_dur = np.mean(arr_dur)
m_mass = np.mean(arr_mass)
m_vel = np.mean(arr_vel)

std_egw = np.std(arr_egw)
std_freq = np.std(arr_freq)
std_dur = np.std(arr_dur)
std_mass = np.std(arr_mass)
std_vel = np.std(arr_vel)


stan_egw = (arr_egw - m_egw) / std_egw
stan_freq = (arr_freq - m_freq) / std_freq
stan_dur = (arr_dur - m_dur) / std_dur
stan_mass = (arr_mass - m_mass) / std_mass
stan_vel = (arr_vel - m_vel) / std_vel
'''

metrics4 = np.sqrt(np.square(stan_egw) + np.square(stan_freq) + np.square(stan_mass) + np.square(stan_vel))

'''
###############################################################################
Rotating vs. Nonrotating points
###############################################################################
'''

metrics4_y = []
eff10_y = []
eff50_y = []
egw_y = []

metrics4_n = []
eff10_n = []
eff50_n = []
egw_n = []

for x in enumerate(rotate_list):
    i = x[0]
    if rotate_list[i] == True:
        metrics4_y.append(metrics4[i])
        eff10_y.append(arr_eff10[i])
        eff50_y.append(arr_eff50[i])
        egw_y.append(arr_egw[i])
        
    else:
        metrics4_n.append(metrics4[i])
        eff10_n.append(arr_eff10[i])
        eff50_n.append(arr_eff50[i])
        egw_n.append(arr_egw[i])
        

'''
###############################################################################
Plots using 4 parameters log
###############################################################################
'''

print('4 parameter standardization using log')
# Standardized Hyperparameter Coordinates of Energy, Frequency, Duration, and Mass vs. Distance
plt.figure()
plt.plot(eff10_y, metrics4_y, 'r*', label = '10% & rotating')
plt.plot(eff10_n, metrics4_n, 'ro', label = '10% & nonrotating')
plt.plot(eff50_y, metrics4_y, 'b*', label = '50% & rotating')
plt.plot(eff50_n, metrics4_n, 'bo', label = '50% & nonrotating')
plt.legend()
plt.title('Standardized 4 parameter Space vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Standardized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(10)
plt.show()

# Standardized Hyperparameter Coordinates of Energy, Frequency, Duration, and Mass vs. Distance at 10% efficiency
plt.figure()
plt.plot(eff10_y, metrics4_y, 'ro', label = 'rotating')
plt.plot(eff10_n, metrics4_n, 'bo', label = 'nonrotating')
plt.legend()
plt.title('Standardized 4 parameter Space vs. Distance (10% efficiency)')
plt.xlabel('Distance (kpc)')
plt.ylabel('Standardized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(10)
plt.show()

# Standardized Hyperparameter Coordinates of Energy, Frequency, Duration, and Mass vs. Distance at 50% efficiency
plt.figure()
plt.plot(eff50_y, metrics4_y, 'ro', label = 'rotating')
plt.plot(eff50_n, metrics4_n, 'bo', label = 'nonrotating')
plt.legend()
plt.title('Standardized 4 parameter Space vs. Distance (50% efficiency)')
plt.xlabel('Distance (kpc)')
plt.ylabel('Standardized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(10)
plt.show()

# Standardized Hyperparameter Coordinates of Energy, Frequency, Duration, and Mass vs. Distance only rotating
plt.figure()
plt.plot(eff10_y, metrics4_y, 'ro', label = '10%')
plt.plot(eff50_y, metrics4_y, 'bo', label = '50%')
plt.legend()
plt.title('Standardized 4 parameter Space (rotating) vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Standardized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.show()

# Standardized Hyperparameter Coordinates only non rotating
plt.figure()
plt.plot(eff10_n, metrics4_n, 'ro', label = '10%')
plt.plot(eff50_n, metrics4_n, 'bo', label = '50%')
plt.legend()
plt.title('Standardized 4 parameter Space (nonrotating) vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Standardized Hyperparameter Coordinates')
plt.grid(True)
plt.xscale('log')
plt.axvline(10)
plt.show()

