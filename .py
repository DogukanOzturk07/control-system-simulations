import numpy as np
import matplotlib.pyplot as plt

# Simple first-order system: dx/dt = -a*x + b*u
a = 1.0
b = 1.0

dt = 0.01
t = np.arange(0, 10, dt)

x = 0
u = 1  # step input

x_values = []

for _ in t:
    dx = -a * x + b * u
    x = x + dx * dt
    x_values.append(x)

plt.plot(t, x_values)
plt.title("Simple Control System Response")
plt.xlabel("Time")
plt.ylabel("State x")
plt.grid()
plt.show()
