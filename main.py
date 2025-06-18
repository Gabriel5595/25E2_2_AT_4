from components.core.image_matrix import get_image
from components.core.mean_filter import mean_kernel
from components.core.filter_design import convolve2d

img = get_image()
kernel = mean_kernel(3)
smoothed = convolve2d(img, kernel)

print(img)
print(smoothed.round().astype(int))