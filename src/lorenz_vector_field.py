"""
Example from the book Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control.
Chapter 7. Data-Driven Dynamical Systems.
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Constants
sigma = 10
beta = 8/3
rho = 28
x0 = (0, 1, 20)
dt = 0.001
t = np.arange(0, 50+dt, dt)

# System of Differential Equations (Lorenz System)
def lorenz(x_y_z, t0, sigma=sigma, beta=beta, rho=rho):
    x, y, z = x_y_z

    return [sigma*(y-x), x*(rho-z)-y, x*y-beta*z]

# Integration
x_t = integrate.odeint(lorenz, x0, t, rtol=10**(-12), atol=10**(-12)*np.ones_like(x0))

# Plot
x, y, z = x_t.T

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=1)
plt.show()


