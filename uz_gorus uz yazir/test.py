import cv2
import numpy as np
import subprocess

# Haar Cascade modelləri yükləyirik
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
fullbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Kamera açılır
cap = cv2.VideoCapture(0)
previous_frame = None

# Başqa proqramı işə salmaq üçün dəyişən
program_started = False

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
    
    # Üz tanıma
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, "Uz", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        
        # Proqramı yalnız bir dəfə işə salmaq
        if not program_started:
            try:
                subprocess.run(["code", r"C:\xampp\htdocs\php-dersler-2"], check=True)  # Burada path dəyişdirin
                program_started = True
            except Exception as e:
                print(f"Proqramı işə salarkən xəta baş verdi: {e}")
    
    # Ekranda göstərmək
    cv2.imshow("Real-Time Motion & Object Detector", frame)
    
    # Çıxış üçün 'q' basmaq
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
