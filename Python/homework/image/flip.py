# cv2_rotate.py

import cv2
import numpy as np

img = cv2.imread("homework/image/test2.png")
print("初始: {img.shape}")
img = cv2.flip(img, 0)
print("更改: {img.shape}")
cv2.imwrite("homework/image/rotate_logo.png", img)
