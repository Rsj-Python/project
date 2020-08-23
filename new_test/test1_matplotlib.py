import numpy as np
import matplotlib.pyplot as pl
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False


x = np.arange(0.1,10,0.01)

y = np.log(1 + 2*x) / x
pl.plot(x,y)
pl.show()
