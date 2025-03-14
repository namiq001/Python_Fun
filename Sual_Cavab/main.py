import speech_recognition as sr
import pyttsx3
import datetime
import requests

# Səsli cavab üçün engine hazırlayıb başlatmaq
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinləyirəm...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='az')
            print(f"Sən dedin: {query}")
            return query
        except sr.UnknownValueError:
            print("Bağışla, sənin nə dediyini anlamadım.")
            return None
        except sr.RequestError:
            print("Xəta baş verdi.")
            return None

def get_weather():
    # Burada real hava məlumatları almaq üçün API istifadə edəcəyik
    api_key = "YOUR_API_KEY"
    location = "Baku"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&lang=az"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"] - 273.15
        description = response["weather"][0]["description"]
        return f"Havanın temperaturu {temp:.1f}°C və {description}."
    else:
        return "Hava məlumatlarını əldə etmək mümkün olmadı."

def assistant():
    speak("Salam! Mən sənin virtual asistanınım. Nə edə bilərəm?")
    while True:
        query = listen()
        if query:
            query = query.lower()

            if 'hava' in query:
                speak(get_weather())
            elif 'saat' in query:
                now = datetime.datetime.now()
                speak(f"İndiki vaxt: {now.strftime('%H:%M:%S')}")
            elif 'dayan' in query or 'çix' in query:
                speak("Görüşərik! :)")
                break
            else:
                speak("Bağışla, mənim edə biləcəyim başqa bir şey tapmadım.")

if __name__ == "__main__":
    assistant()
