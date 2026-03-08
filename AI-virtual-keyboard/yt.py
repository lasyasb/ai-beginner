import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
from time import sleep

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Frame width for dynamic thresholding
frameWidth = 1280
leftThreshold = frameWidth * 0.25  # 25% from left
rightThreshold = frameWidth * 0.75  # 75% from left

# Helper function to check finger states
def fingersUp(lmList):
    fingers = []
    if lmList[8][1] < lmList[6][1]:  # Index finger
        fingers.append(1)
    else:
        fingers.append(0)
    if lmList[12][1] < lmList[10][1]:  # Middle finger
        fingers.append(1)
    else:
        fingers.append(0)
    return fingers

# Main loop
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]["lmList"]  # Landmark list of the first hand
        fingers = fingersUp(lmList)

        indexX = lmList[8][0]
        print(f"Index Finger X: {indexX}")

        # Play/Pause if both index and middle fingers are up
        if fingers == [1, 1]:
            pyautogui.press('k')
            print("Play/Pause")
            sleep(1)

        # Rewind if only index finger up and on left side
        elif fingers == [1, 0] and indexX < leftThreshold:
            pyautogui.press('j')
            print("Rewind 10s")
            sleep(1)

        # Forward if only index finger up and on right side
        elif fingers == [1, 0] and indexX > rightThreshold:
            pyautogui.press('l')
            print("Forward 10s")
            sleep(1)

    cv2.imshow("Hand Gesture Control", img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
