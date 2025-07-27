from components.core.image_matrix import get_image
from components.core.mean_filter import mean_kernel
from components.core.convolution import convolve2d

import numpy as np

img = get_image()
kernel = mean_kernel(3)
smoothed = convolve2d(img, kernel)

def edge_energy(M):
    # soma das diferenças absolutas horizontais e verticais
    dx = np.abs(np.diff(M, axis=1))
    dy = np.abs(np.diff(M, axis=0))
    return dx.mean() + dy.mean()

var_before = np.var(img)
var_after  = np.var(smoothed)

edge_before = edge_energy(img)
edge_after  = edge_energy(smoothed)

print(f"\nVariância global: antes={var_before:.2f}  depois={var_after:.2f}")
print(f"Energia de bordas (|∇| média): antes={edge_before:.2f}  depois={edge_after:.2f}\n")

print(img)
print(smoothed.round().astype(int))