import numpy as np

def mean_kernel(size=3):
    return np.ones((size, size)) / (size * size)
