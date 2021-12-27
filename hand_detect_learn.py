import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)

mphands = mp.solutions.hands #call the detect fuction
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils # call the function which can help us draw points or lines on hands
handlmkstyle_dot = mpdraw.DrawingSpec(color=(0,0,255), thickness=5)
handlmkstyle_connection = mpdraw.DrawingSpec(color=(0,255,0), thickness=7)

while True:
    ref, frame = cam.read()
    imgrgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #change img to RGB format
    result = hands.process(imgrgb)
    landmarks = result.multi_hand_landmarks #landmarks of each detection 
    if landmarks:
        for handlmk in landmarks:        #point      #connect each point                     #style of oints          #style of lines
            mpdraw.draw_landmarks(frame, handlmk, mphands.HAND_CONNECTIONS, handlmkstyle_dot, handlmkstyle_connection) #draw landmarks on hands
            for i, lm in enumerate(handlmk.landmark): #print all landmark for each piont
                print(i, lm.x, lm.y) # unit => proportion
    cv2.imshow("cam", frame)

    if cv2.waitKey(1)==ord("q"):
        break
