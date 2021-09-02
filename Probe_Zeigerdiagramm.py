from matplotlib import scale
import numpy as np
import math as mt
import matplotlib.pyplot as plt
from colorama import init
from numpy.polynomial.polynomial import Polynomial

Up_Strang= 109.43
U_R1 = 8.03
U_xd = 85.49
Strom = 155

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
# soa = np.array([[0,0,0,Up_Strang], [0,Up_Strang,0,U_R1], [0,(U_R1+Up_Strang),-U_xd,0], [,0,-U_xd,0]])
# X, Y, U, V = zip(*soa)
# plt.figure()
# ax = plt.gca()
# ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color=['red', 'green', 'yellow'])
# ax.set_xlim([-200, 10])
# ax.set_ylim([-1, 200])
# plt.draw()
# plt.grid()
# plt.show()
Up = np.arry([0,0,0,Up_Strang])
UR = np.array([0,Up_Strang,0,U_R1])