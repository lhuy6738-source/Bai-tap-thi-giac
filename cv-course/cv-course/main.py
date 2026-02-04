import matplotlib.pyplot as plt
import numpy as np
import cv2
import math

# --- CẤU HÌNH ---
width = 1024
height = 768

# 1. Tạo bức hình kích thước 1024x768 với giá trị pixel ngẫu nhiên
# np.random.randint(low, high, size, dtype)
# Tạo ảnh màu (3 kênh) để vẽ đường màu đỏ
img_random = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# 2. Vẽ một đường chéo, tô màu đỏ
# Điểm bắt đầu (0, 0) -> Điểm kết thúc (width, height)
# Màu đỏ trong OpenCV là (B, G, R) -> (0, 0, 255)
thickness = 5
cv2.line(img_random, (0, 0), (width, height), (0, 0, 255), thickness)

# 3. Vẽ các chữ số La Mã I đến XII như trên mặt đồng hồ
center_x = width // 2
center_y = height // 2
radius = 300  # Bán kính của vòng tròn số
numerals = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]

# Cài đặt font chữ
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 5
font_color = (255, 255, 255) # Màu trắng cho dễ nhìn trên nền nhiễu

for i in range(12):
    # Mỗi số cách nhau 30 độ (360 / 12)
    # XII nằm ở vị trí 0 độ (trên cùng), I là 30 độ, v.v...
    # Công thức lượng giác (lưu ý OpenCV trục Y hướng xuống dưới):
    # x = center_x + r * sin(angle)
    # y = center_y - r * cos(angle)
    
    angle_deg = i * 30
    angle_rad = math.radians(angle_deg)
    
    # Tính tọa độ
    x = int(center_x + radius * math.sin(angle_rad))
    y = int(center_y - radius * math.cos(angle_rad))
    
    # Lấy kích thước chữ để căn giữa chính xác tại điểm (x, y)
    text = numerals[i]
    (text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    
    # Điều chỉnh tọa độ để tâm của chữ trùng với điểm (x, y)
    text_x = x - text_w // 2
    text_y = y + text_h // 2
    
    # Vẽ chữ
    cv2.putText(img_random, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

# Hiển thị kết quả
cv2.imshow('Random Noise with Clock & Line', img_random)
cv2.waitKey(0)
cv2.destroyAllWindows()