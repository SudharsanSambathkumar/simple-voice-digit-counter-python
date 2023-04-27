import cv2
import mediapipe as mp
import time
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice to use
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    lmList = []
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
    fingers = []
    
    if len(lmList) != 0:
        # Thumb
        if lmList[4][1] > lmList[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Fingers 1-4
        for i in range(1, 5):
            if lmList[i*4+3][2] < lmList[i*4+1][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        total_fingers = fingers.count(1)
        cv2.putText(img, str(total_fingers), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        engine.say(str(total_fingers))
        engine.runAndWait()
        
    cv2.imshow("Image", img)
    #press "q" to exit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()