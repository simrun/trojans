from lagrange import *

import matplotlib.pyplot as plt

import scipy.stats

# masses to simulate
mps = np.linspace(0.0005, 0.02, 10)

wanders = []
for mp in mps:
  ##########################################################
  # from lagrange.py; need to redefine in this loop
  rs = R * mp/(ms+mp)
  rp = R * ms/(ms+mp)
  w = 2*math.pi/T

  lx = rp-R/2
  ly = math.sqrt(3)*R/2
  ##########################################################

  y0 = (lx,ly,0,0)
  # TODO: parallelise this loop
  wanders.append(wander(orbit(y0, 500)))

fit = np.poly1d(np.polyfit(mps,wanders,2)) # quadratic
print(fit)

plt.rc('font',**{'family':'serif','serif':['mathpazo']})
plt.rc('text', usetex=True)

plt.plot(mps, wanders, 'k+', markersize=8)
plt.plot(mps, fit(mps), 'k-')

plt.xlabel('Planet/sun mass ratio')
plt.ylabel('Range of wander / au')

plt.tight_layout()
plt.savefig('../figures/mass.pdf')
