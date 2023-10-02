from Body.Listen import MicExecution
from Body.Speak import Speak

def MainExe():
    while True:
        query = MicExecution()
        
        if "hello" in query.lower():
            Speak("Hi Sir! I am Jarvis!")
            return True
        elif "bye" in query.lower():
            Speak("Bye Bye Sir!")
            return False
            
MainExe()