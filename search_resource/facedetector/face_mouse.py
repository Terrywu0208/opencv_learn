import cv2
import pyautogui
from cvzone.FaceMeshModule import FaceMeshDetector
import time
import math
import numpy as np

ptime = 0
clx, cly = 0, 0
plx, ply = 0, 0

smk = 5
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

w, h = 640, 360

cap.set(3, w)
cap.set(4, h)

ws, hs = pyautogui.size()
#print(ws, hs)

# idList = range(10)

idList = [6, 12, 15]

while True:
    # pyautogui.PAUSE = 0.1
    # pyautogui.FAILSAFE = False
    success, img = cap.read()
    mirrow = cv2.flip(img,1)

    img, faces = detector.findFaceMesh(mirrow, draw=False)

    if faces:
        face = faces[0]

        for id in idList:
            cv2.circle(mirrow, face[id], 5, (0, 0, 255), cv2.FILLED)
            # print(face[12][1],face[12])

        x1, y1 = face[12][0], face[12][1]
        x2, y2 = face[15][0], face[15][1]
        x6, y6 = face[6][0], face[6][1]
        # xc, yc = (x1 + x2) // 2, (y1 + y2) // 2
        x4, y4 = 280, 110
        x5, y5 = 360, 150

        cv2.rectangle(mirrow, (x4, y4), (x5, y5), (255, 0, 255), 3)

        x3 = np.interp(x6, (x4, x5), (0, ws))
        y3 = np.interp(y6, (y4, y5), (0, hs))
        clx = plx + (x3 - plx) // smk

        cly = ply + (y3 - ply) // smk
        #plx, ply = clx, cly
        # print(yc)
        length = math.hypot(x1 - x2, y1 - y2)

        if length < 15 and x4-10 < x6 < x5+10 and y4-10 < y6 < y5+10:

            cv2.line(mirrow, (x1, y1), (x2, y2), (0, 255, 0), 3)
            # cv2.circle(mirrow, (xc, yc), 5, (0, 0, 255), cv2.FILLED)
            cv2.rectangle(mirrow, (x4, y4), (x5, y5), (0, 255, 0), 3)
            pyautogui.moveTo(clx, cly)



        elif length >= 15 and x4-10 < x6 < x5+10 and y4-10 < y6 < y5+10:
            cv2.line(mirrow, (x1, y1), (x2, y2), (0, 255, 0), 3)
            # cv2.line(mirrow, (x1, y1), (x2, y2), (0, 0, 255), 3)
            pyautogui.leftClick(clx, cly, duration=0.3)
        plx, ply = clx, cly
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, f'FPS:{int(fps)}', (20, 30), cv2.FONT_ITALIC, 1, (0, 0, 100), 5)

    cv2.imshow("image", img)
    cv2.waitKey(1)

