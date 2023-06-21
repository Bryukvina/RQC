import matplotlib.pyplot as plt
import numpy as np

import math


K = 4
b = 0.5
phi_0 = 3.1415/3
y = np.array([i / 10 for i in range(-50, 50, 1)])

def x(y, K, b, phi_0):
    x = [0] * len(y)
    for i in range(len(y)):
        phi = phi_0 + 0.001 * y[i]
        x[i] = y[i] + (K * (2 * y[i] * math.cos(phi) + (1 + b**2 - y[i]**2)*math.sin(phi)))/(1 * (1 + b**2 - y[i]**2) ** 2 + 4 * y[i] ** 2)
    return x

x = x(y, K, b, phi_0)

fig = plt.figure()
plt.scatter(x, y, color='blue', s=5, alpha=1)
plt.show()
