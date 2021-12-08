import cv2
import numpy as np

drawpoint = []

def find_pen(img):
    hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    lower = np.array([63, 97, 0])
    upper = np.array([86, 201, 255])

    mask = cv2.inRange(hsv , lower, upper)

    result = cv2.bitwise_and(img, img, mask = mask)
    penx, peny = find_contour(mask)
    cv2.circle(imgContour, (penx, peny), 10, (0,255,0), cv2.FILLED)
    cv2.imshow("result",result)
    if peny != -1:
        drawpoint.append([penx, peny])


def find_contour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >50:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri*0.02, True)
            x, y, w, h = cv2.boundingRect(vertices)
    return x+w//2, y

def draw(drawpoint):
    for point in drawpoint:
        cv2.circle(imgContour, (point[0], point[1]), 10, (0,255,0), cv2.FILLED)


cam = cv2.VideoCapture(0)

while True:
    ref, frame = cam.read()
    imgContour = frame.copy()
    if ref == True:
        cv2.imshow("cam", frame)
        find_pen(frame)
        draw(drawpoint)
        cv2.imshow("imgContour", imgContour)
    if cv2.waitKey(1) == ord("q"):
        break
    cv2.waitKey(1)