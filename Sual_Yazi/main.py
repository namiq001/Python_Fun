import speech_recognition as sr
import datetime
import requests

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinləyirəm...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='az')
            print(f"Sən dedin: {query}")  # Burada yalnız yazılı cavab veriləcək
            return query
        except sr.UnknownValueError:
            print("Bağışla, sənin nə dediyini anlamadım.")
            return None
        except sr.RequestError:
            print("Xəta baş verdi.")
            return None

def get_weather():
    api_key = "YOUR_API_KEY"  # Burada API açarınızı daxil edin
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
    print("Salam! Mən sənin virtual asistanınım. Nə edə bilərəm?")  # Bu səsli deyil, sadəcə yazılı olacaq
    while True:
        query = listen()
        if query:
            query = query.lower()

            if 'hava' in query:
                print(get_weather())  # Səsli cavab yoxdur, yalnız yazılı olacaq
            elif 'saat' in query:
                now = datetime.datetime.now()
                print(f"İndiki vaxt: {now.strftime('%H:%M:%S')}")
            elif 'dayan' in query or 'çix' in query:
                print("Görüşərik!")  # Burada da yazılı cavab
                break
            else:
                print("Bağışla, mənim edə biləcəyim başqa bir şey tapmadım.")  # Yazılı cavab

if __name__ == "__main__":
    assistant()
