from Features.Clap import Tester

def Listen():
    import speech_recognition as sr
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,7)
    
    try:
        print("Recognizing...")
        print()
        query = r.recognize_google(audio, language='en')
        
    except:
        return ""
    
    query = str(query).lower()
    print(f"You : {query}")
    print()
    return query

def WakeUpDetected():
    import speech_recognition as sr
    queery = Listen().lower()
    
    if "wake up" in queery:
        return
        
    else:
        WakeUpDetected()
    

def Main():
    WakeUpDetected()
    
    from Body.Speak import Speak
    
    print()
    print("Jarvis : Welcome Sir")
    Speak("Welcome Sir")
    a=True
    # from Body.Listen import MicExecution
    from Jarvis import MainExe
    while(a):
         a = MainExe()
        # text = MicExecution()
        # Speak(text)
    
def main():
    print()
    print()
    print("********** Welcome to Jarvis Assistant **********")
    print()
    print()
    Tester()
    from Body.Speak import Speak
    Speak("Hello")
    print()
    Main()
    
if __name__ == "__main__":
    main()
    