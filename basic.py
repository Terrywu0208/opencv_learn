import cv2
import numpy as np
import combine

# # 匯入圖片
# img = cv2.imread("img/ford_mustang.jfif")

# cv2.imshow("output" , img)

# cv2.waitKey(0)

# #動態影像
# video = cv2.VideoCapture(0) #如果使用攝影機 : 0 如果使用影片打影片的檔名
# while True:
#     success , img = video.read() # success回傳布林
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'): #按Q跳出
#         break


#影像處理手法

# img = cv2.imread("img/ford_mustang.png")
# imgGary = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #將rgb轉換成灰度圖
# imgBlur = cv2.GaussianBlur(imgGary,(1,1),0) #將影像平滑模糊化
# imgCanny = cv2.Canny(imgBlur,10,250)#影像邊緣偵測 low_threshold與high_threshold 的數值取決於灰階的像素質
# kernel = np.ones((2,2),np.uint8)  #為啥要這樣寫
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #影像膨脹， 用途1：Dilation 影像膨脹通常是配合著影像侵蝕 Erosion 使用，先使用侵蝕的方式使影像中的線條變窄，同時也去除雜訊，之後再透過 Dilation 將影像膨脹回來。 用途2：用來連接兩個很靠近但分開的物體。
# imgEroded = cv2.erode(imgDialation, kernel ,iterations=1) #影像侵蝕 用途1：Erosion 影像侵蝕對於移除影像中的小白雜點很有幫助，可用來去噪，例如影像中的小雜點，雜訊。 用途2：細化影像，消除毛刺。
# cv2.imshow("imgGary",imgGary)
# cv2.imshow("imgBlur",imgBlur)
# cv2.imshow("imgCanny",imgCanny)
# cv2.imshow("imgEroded",imgEroded)
# cv2.imshow("imgDialation",imgDialation)
# cv2.waitKey(0)

#改變照片大小
# img = cv2.imread("img/ford_mustang.png")
# print(img.shape) # (圖片高度,圖片寬度,RGB維度)
# imgResize = cv2.resize(img,(150,500)) #改變大小 (內放心的尺寸) (寬、高)
# cv2.imshow("imgResize" , imgResize)
# print(imgResize.shape)
# cv2.waitKey(0)

#擷取照片
# img = cv2.imread("img/ford_mustang.png")

# imgCropped = img[0:200,200:500] #想擷取的範圍 [高 , 寬]

# cv2.imshow("imgCropped",imgCropped)
# cv2.waitKey(0)

#畫圖形
# img = np.zeros((512,512,3),np.uint8)

# cv2.line(img,(0,0),(300,300),(0,0,255),2) #cv2.line(影像, 開始座標, 結束座標, 顏色, 線條寬度)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),3) #cv2.rectangle(影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)
# cv2.circle(img,(400,50),30,(255,255,0),5) #cv2.circle(影像, 圓心座標, 半徑, 顏色, 線條寬度)
# cv2.putText(img,"OPENCV",(300,300),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
# cv2.imshow("opencv",img)
# cv2.waitKey(0)

#影像合併
# img = cv2.imread("img/book.jpg")
# print(img.shape)
# imgresize = cv2.resize(img,(384,384))
# imgv = np.vstack((imgresize,imgresize))
# imgh = np.hstack((imgresize,imgresize))
# cv2.imshow("imgv",imgv)
# cv2.imshow("imgh",imgh)

# cv2.waitKey(0)



#Color Detection

# def empty(a):
#     pass

# img = cv2.imread("img/geometry.png")
# # imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgresize = cv2.resize(img,(598,338))
# cv2.namedWindow("Trackbox")
# cv2.resizeWindow("Trackbox",(640,240))
# cv2.createTrackbar("Hue Min","Trackbox",1,179,empty)
# cv2.createTrackbar("Hue Max","Trackbox",179,179,empty)
# cv2.createTrackbar("Sat Min","Trackbox",0,255,empty)
# cv2.createTrackbar("Sat Max","Trackbox",255,255,empty)
# cv2.createTrackbar("Val Min","Trackbox",0,255,empty)
# cv2.createTrackbar("Val Max","Trackbox",255,255,empty)

# while True:
#     imgHSV = cv2.cvtColor(imgresize,cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos("Hue Min","Trackbox")
#     h_max = cv2.getTrackbarPos("Hue Max","Trackbox")
#     s_min = cv2.getTrackbarPos("Sat Min","Trackbox")
#     s_max = cv2.getTrackbarPos("Sat Max","Trackbox")
#     v_min = cv2.getTrackbarPos("Val Min","Trackbox")
#     v_max = cv2.getTrackbarPos("Val Max","Trackbox")
#     lower = np.array([h_min,s_min,v_min])
#     higher = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHSV,lower,higher)
#     imgResult = cv2.bitwise_and(imgresize,imgresize,mask=mask) #問題
#     imgStack = combine.stackImages(1,([img,imgHSV],[mask,imgResult]))
#     cv2.imshow("imgStack",imgStack)
#     cv2.waitKey(1)


# # draw bounding box and detect shapes

# def getCountour(img):
#     #抓出輪廓的各點形成list
#     countours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in countours:
#         area = cv2.contourArea(cnt) #輪廓面積
#         print(area)
#         if area > 20:
#             cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
#             peri = cv2.arcLength(cnt,True) #輪廓長度
#             # print(peri)
#             # cv2.approxPolyDP()來提取圖像中的輪廓近似值
#             # contour 做多邊形逼近 (approxPolyDP)
#             # 對 contour 做多邊形逼近的目的, 可以想成是用粗一點的線來描邊, 來忽略掉細微的毛邊或雜點
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#             print(len(approx))
#             objCor = len(approx)
#             x,y,w,h = cv2.boundingRect(approx)
#             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)

#             if objCor == 3:
#                 Objt = "Tri"
#             elif objCor == 4:
#                 aspratio = w/h
#                 if aspratio > 0.95 and aspratio < 1.05:
#                     Objt = "square"
#                 else:
#                     Objt = "rectangle"
#             else:
#                 Objt="NONE"
#             cv2.putText(imgContour,Objt,
#                         (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),2)
    

# img = cv2.imread("img/geometry.png")
# re_img = cv2.resize(img,(598,338))
# imgContour = re_img.copy() #為了把bounding box畫上
# imgGray = cv2.cvtColor(re_img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
# imgCanny = cv2.Canny(imgBlur,50,50)
# getCountour(imgCanny)
# imgStack = combine.stackImages(1,([re_img,imgGray],[imgBlur,imgContour]))
# cv2.imshow("img",imgStack)
# cv2.waitKey(0)


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("1.jpg")
imgGary = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)

faces = faceCascade.detectMultiScale(imgGary,1.1,4)


