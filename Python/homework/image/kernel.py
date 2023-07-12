# 卷积核
# ⎡⎣⎢1 0 −1
#   0 0 0
#   -1 0 1⎤⎦⎥

# 维度的大小减2
# 仅保留了边缘信息
import cv2
import numpy as np

img = cv2.imread("homework/image/test2.png")
print("初始: {img.shape}")


conv_img = np.zeros((int(img.shape[0]) - 2, int(img.shape[1]) - 2, int(img.shape[2])))
for i in range(int(img.shape[0]) - 2):
    for j in range(int(img.shape[1]) - 2):
        conv_img[i][j] = img[i][j] - img[i + 2][j] - img[i][j + 2] + img[i + 2][j + 2]

print("更改: {conv_img.shape}")
cv2.imwrite("image/conv.png", conv_img)
