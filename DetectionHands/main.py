import SerialModule
import cv2
import time
import findhand

cap = cv2.VideoCapture(0)
detector = findhand.HandDetector(maxHands=1, detectionCon=0.7)
mySerial = SerialModule.SerialObject("COM3", 9600, 1)
cap.set(3, 1280)
cap.set(4, 720)

def main():
    global pTime
    pTime = 0
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        if lmList:
            fingers = detector.fingersUp()
            #print(fingers)
            mySerial.sendData(fingers)
        #imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #cv2.imshow("imrgb", imgRGB)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow('i', img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
