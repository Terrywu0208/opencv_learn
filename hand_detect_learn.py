import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)

mphands = mp.solutions.hands #call the detect fuction
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils # call the function which can help us draw points or lines on hands
handlmkstyle_dot = mpdraw.DrawingSpec(color=(0,0,255), thickness=5)
handlmkstyle_connection = mpdraw.DrawingSpec(color=(0,255,0), thickness=5)

while True:
    ref, frame = cam.read()
    imgrgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #change img to RGB format
    result = hands.process(imgrgb)
    landmarks = result.multi_hand_landmarks #landmarks of each detection 
    screen_height = frame.shape[0] #get screen height
    screen_weidth = frame.shape[1] #get screen weidth
    if landmarks:
        for handlmk in landmarks:        #point      #connect each point                     #style of oints          #style of lines
            mpdraw.draw_landmarks(frame, handlmk, mphands.HAND_CONNECTIONS, handlmkstyle_dot, handlmkstyle_connection) #draw landmarks on hands
            for i, lm in enumerate(handlmk.landmark): #print all landmark for each piont
                position_x = int(screen_weidth * lm.x) # actually position
                position_y = int(screen_height * lm.y) # actually position
                cv2.putText(frame, str(i), (position_x - 25, position_y +5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2) # put number on the points
                # if i == 4:
                #     cv2.circle(frame, (position_x, position_y), 20, (0,0,255), cv2.FILLED) #enlarge the specific point
                print(i,position_x,position_y)
                # print(i, lm.x, lm.y) # unit => proportion
    cv2.imshow("cam", frame)

    if cv2.waitKey(1)==ord("q"):
        break
