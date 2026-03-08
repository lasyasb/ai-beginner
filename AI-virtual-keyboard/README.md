
# Gesture-Based Input Systems

This is a project made by **Lasya Sadubugga** as part of an exploration into gesture-controlled input systems using computer vision and Python.

In this project, we aim to reduce the gap between real-world physical interactions and virtual input systems. The result is a gesture-based virtual keyboard and a YouTube gesture controller that use computer vision to detect and interpret hand gestures, allowing users to interact using just their fingers in the air.

The system uses **OpenCV**, **CVZone**, and **MediaPipe** for hand detection, and **Pynput** or **PyAutoGUI** to simulate keyboard inputs. A webcam acts as the only required hardware, making this system accessible and hardware-independent.

---

## 💡 Problem Statement

As the variety of human-computer interfaces expands—especially for accessibility—traditional keyboard and mouse interfaces prove limiting for many users. This project explores a new approach: creating a functional input system using just a webcam and hand gestures.

Such a system can benefit:
- AR/VR environments
- Touch-free public kiosks
- Users with mobility limitations

---

## 🚩 Objectives

- 🧠 Develop a **virtual keyboard** that detects finger movements to simulate keystrokes.
- 🎬 Create a **YouTube gesture controller** for play/pause, rewind, and forward functions.
- 🧠 Use **OpenCV, CVZone, MediaPipe** for real-time hand tracking and gesture recognition.
- ⌨️ Use **Pynput** and **PyAutoGUI** to simulate keyboard input.
- 💻 Make interaction more flexible and accessible.

---

## 🧠 Methodology

### 1. Virtual Keyboard (`virtual.py`)

**Layout & Display:**
- Define a QWERTY layout.
- Display buttons using `cv2.rectangle` and `cv2.putText`.
- Use a `Button` class for structure.

**Hand Tracking:**
- Use CVZone’s `HandTrackingModule` (built on MediaPipe) to track 21 hand landmarks.

**Click Detection:**
- Detect if the index finger (point 8) is hovering over a key.
- If distance between index and middle fingers (points 8 and 12) is less than 28px, register a click.
- Display typed text on the screen.

### 2. YouTube Gesture Controller (`yt.py`)

**Gesture Actions:**
- ✌️ Index + Middle Up → Play/Pause (`k` key)
- 👉 Index Only on Left Side → Rewind 10s (`j` key)
- 👉 Index Only on Right Side → Forward 10s (`l` key)

**Tech Used:**
- `pyautogui` to simulate keyboard shortcuts on YouTube
- Finger position logic to determine direction

---

## 🔧 Technologies Used

- Python
- OpenCV
- CVZone
- MediaPipe
- Pynput
- PyAutoGUI

---

## ▶️ How to Run

### 1. Install Requirements

```bash
pip install opencv-python mediapipe cvzone pynput pyautogui
```

### 2. Run Virtual Keyboard

```bash
python virtual.py
```

### 3. Run YouTube Gesture Controller

1. Open a YouTube video and focus the player by clicking it.
2. Run:

```bash
python yt.py
```

3. Use the following gestures:
   - ✌️ Play/Pause
   - 👉 Rewind (move index finger to the left side)
   - 👉 Forward (move index finger to the right side)
   - Press `q` to exit.

---

## 🧩 Future Improvements

- Add numbers and special characters to keyboard.
- Add gestures for space/enter/shift keys.
- Add voice feedback for accessibility.
- Add gesture-based app switching or multi-window control.
- Multi-language layout switching.

---

## 🙌 Credits

- **Lasya Sadubugga** – Project Author
- Inspired by open-source gesture UI projects and CVZone documentation.

---
