import pyautogui
import webbrowser
import time
from datetime import datetime
import pytz

def open_youtube_and_play_song(song_name):
    # Google Chrome-u açmaq
    webbrowser.open('https://www.youtube.com')

    # YouTube-un tam açılmasını gözləyirik
    time.sleep(5)  # Bir neçə saniyə gözləyirik ki, səhifə tam açılsın

    # YouTube səhifəsinin açıldığından əmin olduqdan sonra axtarış qutusunun koordinatlarını tapıb klikləyirik
    # Əgər birbaşa axtarış qutusunun koordinatlarına klikləmək istəyirsinizsə, bu koordinatları əldə edərək aşağıdakı şəkildə istifadə edin:
    
    # Axtarış qutusunun koordinatlarına klikləyirik (burada bu koordinatlar sizin ekranınıza uyğun olaraq dəyişə bilər)
    pyautogui.click(710, 134)  # Bu koordinatları YouTube səhifəsindəki axtarış qutusunun yeri ilə uyğunlaşdırın
    time.sleep(1)

    # Axtarış qutusuna mahnının adını yazırıq
    pyautogui.write(song_name)
    pyautogui.press('enter')  # Enter düyməsinə basır

    # Axtarış nəticələrinin yüklənməsi üçün əlavə vaxt gözləyirik
    time.sleep(5)

    # Videonun açılmasını gözləmək üçün bir az daha gözləyirik
    pyautogui.moveTo(591, 348)  # Bu koordinatlar dəyişə bilər. YouTube səhifəsində doğru nəticəni tapana qədər dəyişdirin.
    pyautogui.click()  # İlk nəticəni klikləyirik

def check_time_and_play_song():
    # Bakı vaxtını alırıq (və ya öz vaxt zonanızı əlavə edə bilərsiniz)
    tz = pytz.timezone('Asia/Baku')
    current_time = datetime.now(tz).strftime('%H:%M')

    print(f'Hal-hazırkı vaxt: {current_time}')

    # istediyiniz saatda musiqini açırıq
    if current_time == "13:26":
        print("Saat 13:26 oldu! Musiqini açırıq...")
        song_name = "Balaeli & Sebnem - Tesaduf 2024 (Yeni Klip)"
        open_youtube_and_play_song(song_name)
    else:
        print("Saat hələ gəlməyib. Gözləyirik...")

# Bu funksiyanı hər dəqiqə bir dəfə çağıracağıq
while True:
    check_time_and_play_song()
    time.sleep(20)  # Hər 60 saniyədən bir yoxlayırıq
