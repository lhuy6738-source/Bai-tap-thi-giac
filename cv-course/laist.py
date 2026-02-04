import matplotlib.pyplot as plt
import numpy as np
import cv2 

#Black and white colormap

#mang pixel values to 0-255 range (8 bits)
M = 255 #1024x768
N = 255
K = 100
# ảnh có MxN pixels 
img = np.zeros((M,N), dtype=np.uint8)
for i in range(M):
    img[i,0:100] = i
# plt.imshow(img, cmap='gray')
# plt.show()
cv2.imshow('Gray Map', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Color colormap
img_color = np.zeros((M,N,3), dtype=np.uint8) #Red, Green, Blue

for i in range(M):
    img_color[i,0:64,0] = i  #Red channel
    img_color[i,100:150,1] = i  #Green channel
    img_color[i,200:250,2] = i  #Blue channel
# plt.imshow(img_color)
# plt.show()
# print(img_color)
cv2.imshow('Color Map', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Tạo một bức hình có kích thước 1024x768 với các giá trị pixel ngẫu nhiên
# Vẽ một đường chéo, tô màu đỏ cho đường chéo đó và hiển thị bức hình
# Vẽ lần lượt các chữ số La Mã I đến XII tương tự như trên một chiếc đồng hồ