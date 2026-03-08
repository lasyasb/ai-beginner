import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize detector
detector = HandDetector(detectionCon=0.8)

# Keyboard layout
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "<"]]
finalText = ""

# Controller for physical keyboard input
keyboard = Controller()


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text


# Draw all keyboard buttons
def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (x, y, w, h), 20, rt=0)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img


# Create button objects
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# Main loop
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # Detect hands

    img = drawAll(img, buttonList)

    if hands:
        lmList = hands[0]['lmList']  # Landmark list of first hand

        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            # Check if index finger is over the button
            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                # Distance between index and middle finger
                l, _, _ = detector.findDistance(lmList[8][:2], lmList[12][:2], img)



                if l < 28:
                    keyboard.press(button.text)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    if button.text == '<':
                        finalText = finalText[:-1]
                    else:
                        finalText += button.text
                    sleep(0.5)

    # Display the typed text
    cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Image", img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
