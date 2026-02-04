import cv2 as cv
import numpy as np
import math

cap = cv.VideoCapture("cv-course/bang_chuyen.mp4")
if not cap.isOpened():
    print("Không mở được video")
    exit()

# ====== TÌM VẠCH ĐỎ ======
ret, first_frame = cap.read()
hsv = cv.cvtColor(first_frame, cv.COLOR_BGR2HSV)
lower_red1 = np.array([0,120,70]); upper_red1 = np.array([10,255,255])
lower_red2 = np.array([170,120,70]); upper_red2 = np.array([180,255,255])
mask = cv.inRange(hsv, lower_red1, upper_red1) + cv.inRange(hsv, lower_red2, upper_red2)
contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

line_X = None
for c in contours:
    if cv.contourArea(c) > 500:
        x, y, w, h = cv.boundingRect(c)
        line_X = x + w//2
        break

if line_X is None:
    print("Không tìm thấy vạch đỏ")
    exit()

cap.set(cv.CAP_PROP_POS_FRAMES, 1)

next_id = 0
objects = {}
counted_ids = set()
count = 0
MAX_UNSEEN_FRAMES = 5

while True:
    ret, frame = cap.read()
    if not ret: break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (9, 9), 2)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp=1.2, minDist=50,
                              param1=100, param2=35, minRadius=20, maxRadius=80)

    current_centers = []
    if circles is not None:
        circles = np.uint16(np.round(circles))
        for c in circles[0, :]:
            current_centers.append((int(c[0]), int(c[1]), int(c[2])))

    new_objects = {}
    used_centers = set()

    # 1. Cập nhật các đối tượng hiện có
    for obj_id, (px, py, unseen) in objects.items():
        best_match = None
        min_dist = 50

        for i, (cx, cy, cr) in enumerate(current_centers):
            if i in used_centers: continue
            dist = math.hypot(cx - px, cy - py)
            if dist < min_dist:
                min_dist = dist
                best_match = i

        if best_match is not None:
            cx, cy, cr = current_centers[best_match]
            
            # KIỂM TRA ĐẾM QUA VẠCH (Khi tâm đi qua line_X)
            if obj_id not in counted_ids:
                if px <= line_X and cx > line_X:
                    count += 1
                    counted_ids.add(obj_id)
            
            new_objects[obj_id] = (cx, cy, 0)
            used_centers.add(best_match)
            
            # Vẽ visualization
            cv.circle(frame, (cx, cy), cr, (0, 255, 0), 2)
            cv.putText(frame, f"ID {obj_id}", (cx-10, cy-10), 2, 0.5, (0,255,0), 1)
        else:
            # Nếu không tìm thấy, tăng số frame bị mất dấu
            if unseen < MAX_UNSEEN_FRAMES:
                new_objects[obj_id] = (px, py, unseen + 1)

    # 2. Đăng ký đối tượng mới cho các center chưa được dùng
    for i, (cx, cy, cr) in enumerate(current_centers):
        if i not in used_centers:
            new_objects[next_id] = (cx, cy, 0)
            next_id += 1

    objects = new_objects

    # Vẽ vạch đếm và kết quả
    cv.line(frame, (line_X, 0), (line_X, frame.shape[0]), (0, 255, 255), 2)
    cv.putText(frame, f"Total Count: {count}", (20, 50), 
               cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv.imshow("Tracking Count", frame)
    if cv.waitKey(30) & 0xFF == ord('q'): break

cap.release()
cv.destroyAllWindows()