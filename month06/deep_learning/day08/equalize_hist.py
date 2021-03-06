"""
直方图均衡化示例
"""
import  numpy as np
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('../data/sunrise.jpg', 0) # 0表示读取灰度图像
cv2.imshow('im', im)

# 直方图均衡化
im_equ = cv2.equalizeHist(im)
cv2.imshow('im_equ', im_equ) # 显示均衡化处理后的图像

# 绘制灰度直方图
## 原始直方图
print(im.ravel())
plt.subplot(2, 1, 1)
plt.hist(im.ravel(), #ravel返回一个连续的扁平数组
         256, [0, 256], label="orig")
plt.legend()

## 均衡化处理后的直方图
plt.subplot(2, 1, 2)
plt.hist(im_equ.ravel(), 256, [0, 256], label="equalize")
plt.legend()

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()