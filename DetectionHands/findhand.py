import cv2
import mediapipe as mp
import math


class HandDetector:
    """
     Tìm kiếm Bàn tay bằng cách sử dụng thư viện mediapipe. Xuất các mốc
     ở định dạng pixel. Và các chức năng bổ sung như tìm cách nhiều ngón tay lên.
    """

    def __init__(self, mode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        """
            : chế độ tham số: Ở chế độ tĩnh, việc phát hiện được thực hiện trên mỗi hình ảnh: chậm hơn
            : tham số maxHands: Số lượng bàn tay tối đa để phát hiện
            : tham số detectionCon:  Ngưỡng tin cậy phát hiện tối thiểu
            : tham số minTrackCon: Ngưỡng tin cậy theo dõi tối thiểu
        """
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def findHands(self, img, draw=True):
        """
        Tìm bàn tay trong hình ảnh BGR.
         : param img: Hình ảnh để tìm bàn tay.
         : param draw: Flag để vẽ đầu ra trên ảnh.
         : Trả về: Hình ảnh có hoặc không có bản vẽ
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        """
        Tìm bàn tay trong hình ảnh BGR.
         : param img: Hình ảnh để tìm bàn tay.
         : param draw: Flag để vẽ đầu ra trên ảnh.
         : return: Hình ảnh có hoặc không có bản vẽ

        """
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            boxW, boxH = xmax - xmin, ymax - ymin
            bbox = xmin, ymin, boxW, boxH

            if draw:
                cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                              (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),
                              (0, 255, 0), 2)

        return self.lmList, bbox

    def fingersUp(self):
        if self.results.multi_hand_landmarks:
            myHandType = self.handType()
            fingers = []
            # Thumb
            if myHandType == "Right":
                if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers


    def handType(self):

        if self.results.multi_hand_landmarks:
            if self.lmList[17][1] < self.lmList[5][1]:
                return "Right"
            else:
                return "Left"

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.8, maxHands=1)
    while True:
        # Get image frame
        success, img = cap.read()
        # Find the hand and its landmarks
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        print(detector.handType())

        # Display
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
