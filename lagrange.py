import math

import numpy as np
import scipy.integrate

import matplotlib.pyplot as plt

######################################################
# user defined quantities

G = 4*math.pi**2 # gravitational constant
ms = 1 # solar mass
mp = 0.001
R = 5.2 # astronomical units
T = R**1.5 # jupiter -> 11.8618 years

precision = 100 # evaluation points per orbit

######################################################
# derived quantities

rs = R * mp/(ms+mp) # distance from origin to sun
rp = R * ms/(ms+mp)
w = 2*math.pi/T # angular velocity of frame

# co-ordinates of lagrange point
lx = rp-R/2
ly = math.sqrt(3)*R/2

######################################################

# equations of motion
def derivs (y, t):
  rx, ry, vx, vy = y

  # for convenience
  dp3 = ((rp-rx)**2 + ry**2)**1.5
  ds3 = ((rs+rx)**2 + ry**2)**1.5
   
  return (vx,
          vy,
          -G * (ms*(rx+rs)/ds3 + mp*(rx-rp)/dp3) + 2*w*vy + rx*w**2,
          -G * (ms*ry/ds3 + mp*ry/dp3) - 2*w*vx + ry*w**2)

# calculate a trajectory starting from y0
def orbit (y0, orbits):
  t = np.linspace(0, orbits*T, orbits*precision)
  y = scipy.integrate.odeint(derivs, y0, t)
  return np.transpose(y)

# find furthest distance travelled from lagrange point
def wander(y):
  return max([math.sqrt((rx-lx)**2+(ry-ly)**2) for (rx,ry) in zip(y[0],y[1])])
