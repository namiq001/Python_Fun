import cv2
import mediapipe as mp
import pyautogui
import time
import numpy as np

# Mediapipe əl izləmə modulunu işə salırıq
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Kamera açılır
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

# Siçan hərəkətini hamarlamaq üçün dəyişənlər
alpha = 0.5  # Eksponensial hərəkət ortalaması üçün əmsal
smooth_x, smooth_y = None, None

# Kamera pəncərəsinin ölçüsünü dəyişmək
cv2.namedWindow("Hand Tracking Mouse", cv2.WINDOW_NORMAL)  # Pəncərəni ölçüləndirə bilərik
cv2.resizeWindow("Hand Tracking Mouse", 800, 600)  # Pəncərənin ölçüsünü artırırıq

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # OpenCV üçün görüntünü çevirmək (çünki tərs göstərir)
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Rəng formatını dəyişirik (OpenCV -> Mediapipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # İşarət barmağının ucu (8-ci nöqtə) və baş barmaq ucu (4-cü nöqtə)
            index_finger = hand_landmarks.landmark[8]
            thumb_finger = hand_landmarks.landmark[4]
            
            # Kamera koordinatlarını ekran koordinatlarına çeviririk
            screen_x = int(index_finger.x * screen_width)
            screen_y = int(index_finger.y * screen_height)

            # Hərəkəti hamarlayırıq
            if smooth_x is None or smooth_y is None:
                smooth_x, smooth_y = screen_x, screen_y
            else:
                smooth_x = alpha * screen_x + (1 - alpha) * smooth_x
                smooth_y = alpha * screen_y + (1 - alpha) * smooth_y

            # Siçanı hərəkət etdiririk
            pyautogui.moveTo(int(smooth_x), int(smooth_y), duration=0.05)

            # Əlin skeletini çəkirik
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Əgər baş barmaqla işarət barmağı yaxınlaşarsa, siçanı klikləyirik
            distance = ((index_finger.x - thumb_finger.x) ** 2 + (index_finger.y - thumb_finger.y) ** 2) ** 0.5
            if distance < 0.05:
                pyautogui.click()

    # Görüntünü göstəririk
    cv2.imshow("Hand Tracking Mouse", frame)

    # 'q' düyməsinə basılarsa proqram dayandırılacaq
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
