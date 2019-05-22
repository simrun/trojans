# Concurrently evaluates wander for a grid of starting points and saves result to disk
######################################################

from lagrange import *

import multiprocessing

# our grid of sample starting points has size deltax * deltax, centred
# on the lagrange point
deltax = 0.08
x = np.linspace(-deltax/2, deltax/2, 16)
xx, yy = np.meshgrid(x, x)


if __name__ == "__main__":
  # nested list comprehension; the outermost one we run in parallel
  # note: unfortunately pool.map() cannot take lambda functions
  # equivalent to:
  #  ww = [[wander(orbit((lx+x[0],ly+y[0],0,0))) for x in xx.T] for y in yy]
  def y(y):
    return [wander(orbit((lx+x[0],ly+y[0],0,0), 500)) for x in xx.T]
  pool = multiprocessing.Pool(processes=4) # 4 cores on my laptop
  ww = pool.map(y, yy)

  np.save("ww.npy", ww)
