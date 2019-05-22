# Plots data (in ww.npy) produced by offset.py
######################################################

from offset import *

import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import cm

ww = np.load("ww.npy")

fig = plt.figure()
ax = fig.add_subplot(111)
plt.rc('font',**{'family':'serif','serif':['mathpazo']})
plt.rc('text', usetex=True)

contours = ax.contourf(xx, yy, ww, cmap=cm.cool)
cbar = fig.colorbar(contours)
cbar.set_label('Wander / au')

# jupiter's (circular) orbit
cx = np.linspace(-deltax/2, deltax/2, 100)
cy = np.sqrt(rp**2-(cx+lx)**2)-ly
ax.plot(cx, cy, 'k--')

plt.xlabel('Initial x displacement from Lagrange point / au')
plt.ylabel('Initial y displacement from Lagrange point / au')

plt.tight_layout()
plt.savefig('../figures/offset_plot.pdf')
