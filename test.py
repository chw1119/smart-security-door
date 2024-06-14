import cv2
import numpy as np

cap = cv2.VideoCapture(1) #외부 카메라 사용 1,내장 카메라 사용시에는 0으로

brown_lower = np.array([10, 100, 20], dtype="uint8")
brown_upper = np.array([20, 255, 200], dtype="uint8")
white_lower = np.array([0, 0, 200], dtype="uint8")
white_upper = np.array([180, 20, 255], dtype="uint8")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    brown_mask = cv2.inRange(hsv, brown_lower, brown_upper)
    white_mask = cv2.inRange(hsv, white_lower, white_upper)

    kernel = np.ones((2,2),np.uint8)
    brown_mask = cv2.morphologyEx(brown_mask, cv2.MORPH_OPEN, kernel)
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel)

    color_mask = cv2.bitwise_or(brown_mask, white_mask)
    result = cv2.bitwise_and(frame, frame, mask=color_mask)

    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 500: 
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Frame', frame)
    cv2.imshow('Detected Colors', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
