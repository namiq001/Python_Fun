import pyautogui
import time

# Auto-clicker funksiyası
def auto_clicker(interval, count):
    print(f"Auto-clicker başladı! {count} dəfə tıklanacaq.")
    for i in range(count):
        pyautogui.click()  # Siçan tıklaması
        time.sleep(interval)  # Tıklama aralığı (millisaniyə ilə)

# Parametrlər
click_interval = 0.00001  # Tıklamalar arasındakı interval (0.001 saniyə)
click_count = 100  # Neçə dəfə tıklanacaq

# 5 saniyəlik gecikmə
print("Proqram başladıldı, 5 saniyə sonra işə düşəcək...")
time.sleep(5)  # 5 saniyə gözləyir

auto_clicker(click_interval, click_count)
