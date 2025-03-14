import cv2
import numpy as np

# Kamera açılır
cap = cv2.VideoCapture(0)

# Əvvəlki frame (kadr) saxlanacaq
previous_frame = None

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Boz rəngə çevirmək
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # İlk frame təyin etmək
    if previous_frame is None:
        previous_frame = gray
        continue
    
    # Kadrlar arasındakı fərqi tapmaq
    frame_diff = cv2.absdiff(previous_frame, gray)
    thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)[1]
    
    # Konturlar tapılır
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    # Ekranda göstərmək
    cv2.imshow("Real-Time Motion Detector", frame)
    
    # Çıxış üçün 'q' basmaq
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
