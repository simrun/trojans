# Calculates and plots the trajectory of an asteroid given its initial state
######################################################

from lagrange import *

import matplotlib.pyplot as plt
from matplotlib import rc

rx0 = lx
ry0 = ly
orbits = 5000

###############################

y0 = (rx0, ry0, 0, 0)
y = orbit(y0, orbits)

print(wander(y))


# latex font rendering
plt.rc('font',**{'family':'serif','serif':['mathpazo']})
plt.rc('text', usetex=True)

plt.plot(y[0], y[1], 'b-')

plt.text(lx+0.1, ly+0.1, r'L$_4$')
plt.plot(lx, ly, 'k+')

plt.text(-rs+0.4, 0.3, 'Sun')
plt.plot(-rs, 0, 'yo', markersize=50)
plt.text(rp-0.6, 0.15, 'Jupiter')
plt.plot(rp, 0, 'ro', markersize=10)

plt.xlabel('x / au')
plt.ylabel('y / au')

plt.tight_layout()
plt.show()
