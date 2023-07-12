import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import math
import cmath


I = 1400/3.1415
k1 = 75
k2 = 75
gN = 75
alf = complex(1, 2.5)
ksi0 = -8
v_m = 3.1415/2000
k3 = 75
T = 0.04
ex = cmath.exp(complex(0, 3 * 3.1415/4 + 0.6))
b = 0.05
nu = 0.5
w_m = 13000000000
km = 13

def func(t, y):
    y1 = I - k1 * y[0] - y[0] * gN * abs(y[1]) ** 2
    y2 = (alf * y[0] * gN - k2 + complex(0, ksi0 - v_m * t)) * y[1] - 2 * k3 * T * ex * y[3]
    y3 = -y[2] + complex(0, b) * y[3] - 2 * nu * (1 / T) * ex * y[1]
    y4 = -y[3] + complex(0, b) * y[2]
    return np.array([y1, y2, y3, y4])

sol = solve_ivp(func, [0, 5], [1.6 * 10 ** (-27), complex(1, 0), complex(1, 0), complex(1, 0)])



ampl = sol.y[1]
ampl1 = sol.y[2]
for i in range(len(ampl) - 1):
    ampl[i] = 2 * (cmath.phase(ampl[i] - ampl[i + 1])) / (sol.t[i + 1] - sol.t[i]) / 13#full amplitude = y axis
    ampl1[i] = 2 * (cmath.phase(ampl1[i] - ampl1[i + 1])) / (sol.t[i + 1] - sol.t[i]) / 13#front wave = x axis  
    
    
x = []
y = []
for i in range(len(ampl)):
    if -150 < ampl[i] < 0 and 65 < ampl1[i] < 300:
        y.append(ampl[i])
        x.append(ampl1[i])

fig = plt.figure()
plt.scatter(x, y, s=4, alpha=1)
plt.show()
