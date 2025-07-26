# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 12:44:27 2025

@author: alexo
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LinearRegression
from sklearn.utils import check_random_state

height, width = 180, 240
np.random.seed(0)
X = np.arange(width)
Y = np.arange(height)

image = np.zeros((height, width))
for i in range(height):
    image[i,:] = 50 * np.log1p(X) + np.random.randint(-30, 30, size = width)

ir = IsotonicRegression(out_of_bounds="clip")
image_ir = np.zeros_like(image)
for i in range(height):
    image_ir[i,:] = ir.fit_transform(X, image[i,:])
for i in range(width):
    image_ir[:,i] = ir.fit_transform(Y, image[:,i])

#lr = LinearRegression()

#segments = [[[i, y[i]], [i, y1[i]]] for i in range(n)]
#lc = LineCollection(segments, zorder=0)
#lc.set_array(np.ones(len(y)))
#lc.set_linewidths(np.full(n, 0.5))

#fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(12, 6))

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.title("Imagine originală cu zgomot")
plt.imshow(image, aspect='auto', cmap='viridis')
plt.colorbar()

plt.subplot(1,2,2)
plt.title("Imagine după regresie isotonică (pe linii)")
plt.imshow(image_ir, aspect='auto', cmap='viridis')
plt.colorbar()
plt.tight_layout()
plt.show()

plt.show()