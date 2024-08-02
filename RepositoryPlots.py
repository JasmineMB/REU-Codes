# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 07:46:08 2024

@author: MIRIA
"""

import matplotlib.pyplot as plt
import numpy as np

fpath = "D:\\PythonFiles\\REU\\RepositoryData.txt"

name_list = []
egw_list = []
freq_list = []
eff50_list = []
eff10_list = []
rotate_list = []
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
            rotate_list.append(bool(int(line_split[6])))
            mass_list.append(float(line_split[7]))
            dur_list.append(int(line_split[8]))
            
            
arr_name = np.array(name_list)
arr_egw = np.array(egw_list)
arr_freq = np.array(freq_list)
arr_eff50 = np.array(eff50_list)
arr_eff10 = np.array(eff10_list)
arr_mass = np.array(mass_list)
arr_dur = np.array(dur_list)

#Energy vs Frequency
plt.figure()
plt.scatter(arr_freq, arr_egw)
plt.title('Energy of GW vs. Peak Frequency')
plt.grid(True)
plt.xlabel('Peak Frequency (Hz)')
plt.ylabel('Energy of GW (M\u2609c^2)')
plt.yscale('log')
plt.show()

eff_avg = (arr_eff10 + arr_eff50) / 2
line = (arr_eff10 - arr_eff50) / 2

#Energy vs Distance
plt.figure()
plt.errorbar(eff_avg, arr_egw, xerr = line, fmt = '.', capsize = 3)
plt.title('Energy of GW vs. Distances at 10% and 50% Efficiency')
plt.grid(True)
plt.xlabel('Distance (kpc)')
plt.ylabel('Energy of GW (M\u2609c^2)')
plt.xscale('log')
plt.yscale('log')
plt.show()


egw_y = []
eff10_y = []
eff50_y = []
freq_y = []
mass_y = []
dur_y = []

egw_n = []
eff10_n = []
eff50_n = []
freq_n = []
mass_n = []
dur_n = []

for x in enumerate(rotate_list):
    i = x[0]
    if rotate_list[i] == True:
        egw_y.append(arr_egw[i])
        eff10_y.append(arr_eff10[i])
        eff50_y.append(arr_eff50[i])
        freq_y.append(arr_freq[i])
        mass_y.append(arr_mass[i])
        dur_y.append(arr_dur[i])
        
    else:
        egw_n.append(arr_egw[i])
        eff10_n.append(arr_eff10[i])
        eff50_n.append(arr_eff50[i])
        freq_n.append(arr_freq[i])
        mass_n.append(arr_mass[i])
        dur_n.append(arr_dur[i])
   
#Energy vs Frequency - rotating vs nonrotating
plt.figure()
plt.scatter(freq_y, egw_y, c = 'b', label = 'rotating')
plt.scatter(freq_n, egw_n, c = 'r', label = 'nonrotating')
plt.title('Energy of GW vs. Peak Frequency')
plt.grid(True)
plt.xlabel('Peak Frequency (Hz)')
plt.ylabel('Energy of GW (M\u2609c^2)')
plt.yscale('log')
plt.legend()
plt.show()

#Energy vs Distance - points
plt.figure()
plt.scatter(arr_eff50, arr_egw, c = 'b', label = '50% Efficiency')
plt.scatter(arr_eff10, arr_egw, c = 'r', label = '10% Efficiency')
plt.title('Energy of GW vs. Distances at 10% and 50% Efficiency')
plt.grid(True)
plt.xlabel('Distance (kpc)')
plt.ylabel('Energy of GW (M\u2609c^2)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

#Energy vs Distance - points 50%
plt.figure()
plt.scatter(arr_eff50, arr_egw, c = 'b', label = '50% Efficiency')
plt.title('Energy of GW vs. Distances at 50% Efficiency')
plt.grid(True)
plt.xlabel('Distance (kpc)')
plt.ylabel('Energy of GW (M\u2609c^2)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

#Energy vs Distance - points 10%
plt.figure()
plt.scatter(arr_eff10, arr_egw, c = 'r', label = '10% Efficiency')
plt.title('Energy of GW vs. Distances at 10% Efficiency')
plt.grid(True)
plt.xlabel('Distance (kpc)')
plt.ylabel('Energy of GW (M\u2609c^2)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

#Frequency vs Distance
plt.figure()
plt.scatter(arr_eff50, arr_freq, c = 'b', label = '50% Efficiency')
plt.scatter(arr_eff10, arr_freq, c = 'r', label = '10% Efficiency')
plt.title('Peak Frequency vs. Distances at 10% and 50% Efficiency')
plt.grid(True)
plt.xlabel('Distance (kpc)')
plt.ylabel('Peak Frequency (Hz)')
plt.xscale('log')
plt.legend()
plt.show()

#Mass vs Distance
plt.figure()
plt.scatter(arr_mass, arr_eff50, c = 'b', label = '50% Efficiency')
plt.scatter(arr_mass, arr_eff10,  c = 'r', label = '10% Efficiency')
plt.title('Distances at 10% and 50% Efficiency vs. Mass of Star')
plt.grid(True)
plt.ylabel('Distance (kpc)')
plt.xlabel('Mass (M\u2609)')
#plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

#Distance 10% vs Mass
plt.figure()
plt.scatter(mass_y, eff10_y, c = 'b', label = 'rotating')
plt.scatter(mass_n, eff10_n, c = 'r', label = 'nonrotating')
plt.title('Distance at 10% vs Mass of Star')
plt.grid(True)
plt.xlabel('Mass (M\u2609)')
plt.ylabel('Distance (kpc)')
plt.yscale('log')
plt.legend()
plt.show()

#Distance 50% vs Mass
plt.figure()
plt.scatter(mass_y, eff50_y, c = 'b', label = 'rotating')
plt.scatter(mass_n, eff50_n, c = 'r', label = 'nonrotating')
plt.title('Distance at 50% vs Mass of Star')
plt.grid(True)
plt.ylabel('Distance (kpc)')
plt.xlabel('Mass (M\u2609)')
plt.yscale('log')
plt.legend()
plt.show()

#Duration vs Distance
plt.figure()
plt.scatter(arr_eff50, arr_dur, c = 'b', label = '50% Efficiency')
plt.scatter(arr_eff10, arr_dur, c = 'r', label = '10% Efficiency')
plt.title('Duration of Signal vs. Distances at 10% and 50% Efficiency')
plt.grid(True)
plt.xlabel('Distance (kpc)')
plt.ylabel('Duration (ms)')
plt.xscale('log')
#plt.yscale('log')
plt.legend()
plt.show()

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
plt.show()

plt.figure()
plt.plot(eff10_y, freq_y, 'r*', label = '10% & rotating')
plt.plot(eff10_n, freq_n, 'ro', label = '10% & nonrotating')
plt.plot(eff50_y, freq_y, 'b*', label = '50% & rotating')
plt.plot(eff50_n, freq_n, 'bo', label = '50% & nonrotating')
plt.legend()
plt.title('Frequency vs. Distance')
plt.xlabel('Distance (kpc)')
plt.ylabel('Peak Frequency (Hz)')
plt.grid(True)
plt.xscale('log')
plt.show()

sorted_indexes = np.argsort(arr_egw)







