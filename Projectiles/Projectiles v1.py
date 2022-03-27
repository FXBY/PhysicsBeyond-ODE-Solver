# -*- coding: utf-8 -*-
"""Projectiles v1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OdzbJqHvxX2FVzflSXtAkeIQ_Fpq8zOS

# Simulating Projectile motion (version 1)

- The aim of the first version is to have a working implementation of the _Euler method_ for the motion of a projectile.
- the _input parameters_ are set in the code and the _output_ yields the final position and velocity of the projectile
- In the _evaluation_ we simply print out the error of the values obtained by the _Euler method_ when compared to the ones obtained using _SUVAT_
---
"""

# Importing packages
import numpy as np


# Input

# initial position and velocity of the point particle
pos_init = np.array([0, 0])
vel_init = np.array([10, 20])

# Set g
g = np.array([0, -9.81])

# Set the number N of time steps 
N = 10000
# Set a final time 
t_final = 4

dt = t_final/N


# Main

# Implementing the Euler method
# Set the intial values for position and velocity
pos = pos_init
vel = vel_init

# Calculate the new position and velocity for each time step
for i in range(N):
    pos = pos + vel*dt
    vel = vel + g*dt


# Output
print("position ", pos)
print("velocity ", vel)

# Compare the final velocities calculated with Euler vs SUVAT
print("velocity (SUVAT): ", vel_init + g*t_final)
print("Difference: ", vel_init + g*t_final - vel)

# Compare the final positions calculated with Euler vs SUVAT
print("Position (SUVAT): ", pos_init + vel_init * t_final + 1/2 * g * t_final**2)
print("Difference: ", pos_init + vel_init * t_final + 1/2 * g * t_final**2 - pos)
