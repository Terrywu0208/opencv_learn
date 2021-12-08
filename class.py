import cv2
import numpy as np
import random

def img_display():
    img = cv2.imread(r"img\ford_mustang.png")
    # img = cv2.resize(img,(200,300)) 
    img = cv2.resize(img,(0,0),fx=2,fy=2) #以倍數放大 放大兩倍
    cv2.imshow("demo",img)
    cv2.waitKey(0) #等待鍵盤上按任一鍵按下

def video_display():
    video = cv2.VideoCapture(r"img\74622.t.mp4")

    while True:
        ref , frame = video.read() # 會讀取影片的每一幀圖片 回傳 是否成功 及 照片
        if ref == True:
            frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
            cv2.imshow("video",frame)
        else:
            break

        if cv2.waitKey(1) == ord("q"): #如果按q的話影片會停止 ord() =>取得鍵盤的編號
            break
        cv2.waitKey(1) #如果想調快或慢改變裡面的數字

def cam_display():
    cam = cv2.VideoCapture(0)

    while True:
        ref , frame = cam.read() # 會讀取影片的每一幀圖片 回傳 是否成功 及 照片
        if ref == True:
            frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
            cv2.imshow("video",frame)
        else:
            break

        if cv2.waitKey(1) == ord("q"): #如果按q的話影片會停止 ord() =>取得鍵盤的編號
            break
        cv2.waitKey(1) #如果想調快或慢改變裡面的數字


def craete_img():
    img = np.empty((300,300,3),np.uint8) # empty() 創建空的陣列 

    for row in range(300):
        for col in range(300):
            img[row][col]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

    cv2.imshow("img", img)
    cv2.waitKey(0)

def cut_img():
    img = cv2.imread(r"img\ford_mustang.png")
    img = img[:100,:200]
    cv2.imshow("img",img)
    cv2.waitKey(0)

def usual():
    img = cv2.imread(r"img\ford_mustang.png")
    img = cv2.resize(img , (0,0), fx=1.5, fy= 1.5)
    kernel = np.ones((3,3),np.uint8)

    gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img , (1,1), 2) # cv2.GaussianBlur(img,(核),標準差)
    canny = cv2.Canny(img, 200, 250) #cv2.Canny(img, min, max)
    dilate = cv2.dilate(canny, kernel , iterations=1) #cv2.dilate(canny, 核 , iterations=次數)
    erode = cv2.erode(dilate, kernel, iterations=1)

    cv2.imshow("img",img)
    cv2.imshow("gary",gary)
    cv2.imshow("blur",blur)
    cv2.imshow("canny",canny)
    cv2.imshow("dilate",dilate)
    cv2.imshow("erode",erode)
    cv2.waitKey(0)

def draw():
    img = np.zeros((600,600,3),np.uint8)

    cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 0, 255), 2)
    cv2.rectangle(img, (0, 0), (400, 300),(0,255,0), cv2.FILLED)
    cv2.circle(img, (300, 400) ,30 ,(200,200,200),2)
    cv2.putText(img, "Hi" ,(100,500), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2 , (255,255,255), 2)

    cv2.imshow("img", img)
    cv2.waitKey(0)

def filter_color():
    def empty(v):
        pass

    # img = cv2.imread(r"img\winnie.jpg")
    # img = cv2.resize(img,(0,0), fx=0.5, fy=0.5)
    cap = cv2.VideoCapture(0)


    cv2.namedWindow("TrackBar")
    cv2.resizeWindow("TrackBar", 640, 320)

    cv2.createTrackbar("Hue Min" , "TrackBar", 0, 179, empty)
    cv2.createTrackbar("Hue Max" , "TrackBar", 177, 179, empty)
    cv2.createTrackbar("Sat Min" , "TrackBar", 0, 255, empty)
    cv2.createTrackbar("Sat Max" , "TrackBar", 255, 255, empty)
    cv2.createTrackbar("Val Min" , "TrackBar", 0, 255, empty)
    cv2.createTrackbar("Val Max" , "TrackBar", 255, 255, empty)

    while True:
        ref, img = cap.read()
        hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
        h_min = cv2.getTrackbarPos("Hue Min" , "TrackBar")
        h_max = cv2.getTrackbarPos("Hue Max" , "TrackBar")
        s_min = cv2.getTrackbarPos("Sat Min" , "TrackBar")
        s_max = cv2.getTrackbarPos("Sat Max" , "TrackBar")
        v_min = cv2.getTrackbarPos("Val Min" , "TrackBar")
        v_max = cv2.getTrackbarPos("Val Max" , "TrackBar")
        print(h_min, h_max, s_min, s_max, v_min, v_max)

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        mask = cv2.inRange(hsv , lower, upper)

        result = cv2.bitwise_and(img, img, mask = mask)

        cv2.imshow("img",img)
        cv2.imshow("result",result)
        cv2.waitKey(10)
        
def detcet_geometry():
    img = cv2.imread(r"img\geometry.png")
    img = cv2.resize(img,(0,0), fx=2, fy=2)
    imgContour = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(img,150,200)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        cv2.drawContours(imgContour, cnt, -1,(255, 0,0), 4)
        area = cv2.contourArea(cnt)
        if area >200:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri*0.02, True)
            corners = len(vertices)
            x, y, w, h = cv2.boundingRect(vertices)
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 4)
            if corners == 3:
                cv2.putText(imgContour,"Triangle", (x, y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,255),2)
            elif corners == 4:
                cv2.putText(imgContour,"Rectangle", (x, y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,255),2)
            elif corners == 5:
                cv2.putText(imgContour,"Pentagon", (x, y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,255),2)
            elif corners >6 :
                cv2.putText(imgContour,"Circle", (x, y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,255),2)

    cv2.imshow("img", img)
    cv2.imshow("canny",canny)
    cv2.imshow("imgContour", imgContour)
    cv2.waitKey(0)




