import numpy as np

def convolve2d(image, kernel):

    m, n = image.shape
    k = kernel.shape[0]
    pad = k // 2
    padded_img = np.pad(image, ((pad, pad), (pad, pad)), mode='constant', constant_values=0)

    output = np.zeros_like(image, dtype=float)

    for i in range(m):
        for j in range(n):
            window       = padded_img[i:i + k, j:j + k]
            output[i, j] = np.sum(window * kernel)
    return output