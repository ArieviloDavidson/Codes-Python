import matplotlib.pyplot as plt
import pandas as pd 
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

betas = [12884326.827237627, 80.55607498768511, 36.443960153661074]

plothiper = plt.figure()
grafico = plothiper.gca(projection='3d')

x1g = np.linspace(-10000,10000,20)
x2g = np.linspace(-10000,10000,20)

XG, YG = np.meshgrid(x1g, x2g)
Z = betas[0] + XG*betas[1] + YG*betas[2]

# grafico = plt.axes(projection='3d')

grafico.plot_wireframe(XG,YG,Z)
plt.show()

# 12884326.827237627	80.55607498768511	36.443960153661074