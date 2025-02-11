import cv2
import mediapipe as mp
import time
import threading

class Roke:
    def __init__(self):
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.STATUS = False
        # Initialize OpenCV video self.capture
        self.cap = cv2.VideoCapture(1)  # Use 0 for the default webcam

    def getStatus(self):
        return self.STATUS

    def rokeVnSekud(self, a: int):
        couter = a
        while True:
            # Read frame from webcam
            ret, frame = self.cap.read()

            # Convert the frame to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame to detect hands
            results = self.hands.process(rgb_frame)

            # Check if hands are detected
            if results.multi_hand_landmarks:
                couter=a
            else:
                couter-=1

            if couter <= 0:
                self.STATUS = True
            else: self.STATUS = False

            time.sleep(1)

if __name__ == "__main__":
    roke = Roke()
    threading.Thread(target=roke.rokeVnSekud, args=[3,]).start()

    while True:
        print(roke.getStatus())