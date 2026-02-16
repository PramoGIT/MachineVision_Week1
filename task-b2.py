import cv2
import numpy as np
# Create blank image (black background)
img = cv2.imread('CameraFrame-Snapshot.png')

# Draw line (image, start_point, end_point, color_BGR, thickness)
cv2.line(img, (139, 473), (578, 473), (0, 0, 255), 6)
# Draw rectangle (image, top_left, bottom_right, color, thickness)
cv2.rectangle(img, (321, 317), (371, 369), (0, 255, 0), 2)
# Draw circle (image, center, radius, color, thickness)
cv2.circle(img, (319, 241), 24, (255, 0, 0), 2) # -1 = filled
# Put text (image, text, position, font, scale, color, thickness)
cv2.putText(img, 'Pramoda Medis 16.02.2026', (142, 454),
cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

cv2.putText(img, 'Disc 1', (337, 283),
cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

cv2.putText(img, 'Box 1', (379, 381),
cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('Drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()