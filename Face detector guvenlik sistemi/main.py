import cv2
import mediapipe as mp
import numpy as np

# Profil şəkilini yükləyirik (yəni, istifadəçinin tanınması üçün şəkil)
known_face_image = cv2.imread("profile_picture.jpg")  # Burada öz şəkilinizi yükləyin
known_face_gray = cv2.cvtColor(known_face_image, cv2.COLOR_BGR2GRAY)

# Üz tanıma üçün Haar Cascade yükleyirik
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Mediapipe üz tanıma modulu
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Kamera açılır
cap = cv2.VideoCapture(0)

# Üz tanıma modelini başlatırıq
with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Çərçivəni boz tonlara çeviririk
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Üzləri aşkar edirik
        faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

        # Üz tanıma nəticələrini Mediapipe ilə müqayisə edirik
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)

        # Profil şəkli ilə qarşılaşdırma edirik
        face_found = False
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)
                face_found = True

        # Profil şəkli ilə müqayisə
        if face_found:
            # Üz tanındı, profil şəkli ilə müqayisə etməliyik
            face_roi = frame[50:250, 50:250]  # Profil şəkli ilə müqayisə etmək üçün çərçivə təyin edirik
            gray_roi = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)

            # Profil şəkli ilə tanıma (sadə şəkildə)
            result = cv2.matchTemplate(gray_roi, known_face_gray, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  # 5 yox, 4 dəyəri olacaq

            # Həqiqətən profil şəklinə bənzəyirsə
            if max_val > 0.7:  # Uyğunluq dərəcəsi
                cv2.rectangle(frame, (50, 50), (400, 400), (0, 255, 0), 2)  # Yaşıl çərçivə
                cv2.putText(frame, "Xoş Gəldin reis!", (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                # Başqa bir üz aşkar olunduqda
                cv2.rectangle(frame, (50, 50), (400, 400), (0, 0, 255), 2)  # Qırmızı çərçivə
                cv2.putText(frame, "Girisiniz qadagandir", (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            # Heç bir üz tapılmadıqda heç nə göstərilmir
            pass

        # Nəticəni göstəririk
        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
