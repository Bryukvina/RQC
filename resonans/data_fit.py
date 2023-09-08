import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import cmath


#function, that takes parametrs and delta_frequensy list and return list of transmitted wave power points

def theor(x, do, dc, g):
    y = []
    for i in range(len(x)):
        y.append(abs((complex(do, -x[i]) ** 2 - dc ** 2 + g ** 2)/(complex(do + dc, -x[i]) ** 2 + g ** 2)) ** 2)
    y = np.array(y)
    return y

#reading real data

file = open("C:\Job\RQC\experiment_data\modified_data.txt", "r")
s = file.readline()
channel1 = []
channel2 = []
channel3 = []
times = []

#data from file with processing

s = file.readline()
while s != "":
    t, c1, c2, c3 = map(float, s.split(", "))
    times.append(t)
    channel1.append(c1)
    channel2.append(c2)
    channel3.append(c3)
    s = file.readline()
times = np.array(times)
channel3 = np.array(channel3)

#transfering time list to frequency list, using interferometer's data
count = 0
for i in range(1, len(channel2) - 1):
    if channel2[i - 1] < channel2[i] and channel2[i + 1] < channel2[i]:
        count += 1
        
dw = 102000000
dt = (max(times) - min(times)) / count
speed = dw / dt
freq = times * speed

#parameters
do = 2.5 * 10000000000
dc = 7.1 * 10000000000
g = 4.9 * 10000000000

#draw grafix with fitting data. parameters were had already piked up (part of data with resonanse)

theor_list = theor(freq, d0, dc, g)
freq_prac = freq + 0.85 * 10 ** (11)
prac_norm = (channel3 - min(channel3)) /(8.4099E-01 - min(channel3))

plt.figure(figsize=(6, 3))
plt.plot(freq[len(freq) // 3:len(freq) // 2], theor_list[len(freq) // 3:len(freq) //2],  label="theoretical_data")
plt.plot(freq_prac[len(freq) // 3:len(freq)  // 2], prac_norm[len(freq) // 3:len(freq) // 2], label="experiment_data")
plt.legend()
plt.show()

plt.figure(figsize=(6, 3))
plt.plot(freq, theor_list, label="theoretical_data")
plt.plot(freq_prac, prac_norm, label="experiment_data")
plt.legend()
plt.show()
