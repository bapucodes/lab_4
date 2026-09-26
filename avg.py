import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread("gray.jpg", 0)

kernel = np.ones((3,3)) * 1/9

k_s = 3

m = img1.shape[0]

x = img1.shape[1]

filtered_image = np.zeros((m,x))

for i in range(0, m-k_s+1):
    for j in range(0, x-k_s+1):
        filtered_image[i][j] = np.sum(kernel * img1[i:i+k_s, j:j+k_s])

plt.imshow(filtered_image, cmap='gray')

plt.show()
