import cv2

def man_face_detect():
    img = cv2.imread(r"img\man.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
    faceRect = faceCascade.detectMultiScale(gray,1.1, 7)
    print(len(faceRect))

    for (x, y, w, h) in faceRect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("img", img)
    cv2.waitKey(0)


def cam_face_detect():
    cam = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")

    while True:
        ref , frame = cam.read() # 會讀取影片的每一幀圖片 回傳 是否成功 及 照片
        if ref == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faceRect = faceCascade.detectMultiScale(gray,1.1, 7)
            for (x, y, w, h) in faceRect:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame,"Face", (x, y-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4, (0,255,0),2)

            cv2.imshow("video",frame)
        else:
            break

        if cv2.waitKey(1) == ord("q"): #如果按q的話影片會停止 ord() =>取得鍵盤的編號
            break
        cv2.waitKey(1) #如果想調快或慢改變裡面的數字

    