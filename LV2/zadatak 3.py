import numpy as np
import matplotlib.pyplot as plt

img = plt.imread(r"LV2\road.jpg")
print(img.dtype)
print(img.shape)
img = img[:,:,0] # we take only 1 channel for a grayscalepicture

h, w = img.shape[:2]
second_quarter = img[:, w//2:3*w//4]
second_quarter = second_quarter[:,::-1]
rotated90 = np.rot90(img, -1)
mirrored = img[:,::-1]

plt.subplot(2,2,1)
plt.imshow(img, cmap="gray", alpha=0.7)
plt.subplot(2,2,2)
plt.imshow(second_quarter, cmap="gray")
plt.subplot(2,2,3)
plt.imshow(rotated90, cmap="gray")
plt.subplot(2,2,4)
plt.imshow(mirrored, cmap="gray")
plt.show()