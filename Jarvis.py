from Body.Listen import MicExecution
from Body.Speak import Speak
from main import main
from Brain.AIBrain import ReplyBrain
import webbrowser
from datetime import datetime as dt
import pytz

def MainExe():
    while True:
        query = MicExecution()
        
        sites = [["YouTube","https://youtube.com"], ["Facebook","https://facebook.com"], ["Google","https://google.com"], ["Wikipedia","https://wikipedia.com"],
                 ["Instagram", "https://www.instagram.com/"], ["Open AI", "https://chat.openai.com/"], ["GeeksforGeeks", "https://www.geeksforgeeks.org/"],
                 ["Lead code","https://leetcode.com/"], ["LinkedIN", "https://www.linkedin.com/feed/"], ["Github", "https://github.com/"],
                 ["CodeChef", "https://www.codechef.com/"], ["Code forces", "https://codeforces.com/"],["Twitter", "https://www.twitter.com"], ["Amazon", "https://www.amazon.com"],
                 ["Whatsapp", "https://www.whatsapp.com"], ["Microsoft", "https://www.microsoft.com"],["Netflix", "https://www.netflix.com"], ["IMDb", "https://www.imdb.com"],
                 ["Discord", "https://www.discord.com"], ["Ms office", "https://www.office.com"], ["Zoom", "https://www.zoom.us"], ["Pinterest", "https://www.pinterest.com"],
                 ["Paypal", "https://www.paypal.com"], ["Spotify", "https://www.spotify.com"], ["Indeed", "https://www.indeed.com"], ["Ebay", "https://www.ebay.com"],
                 ["Samsung", "https://www.samsung.com"], ["Apple", "https://www.apple.com"], ["Walmart", "https://www.walmart.com"], ["Adobe", "https://www.adobe.com"],
                 ["Tumbler", "https://www.tumblr.com"], ["Telegram", "https://www.telegram.org"], ["Stack Overflow", "https://www.stackoverflow.com"],
                 ["Cricbuzz", "https://www.cricbuzz.com"], ["Disney plus", "https://www.disneyplus.com"], ["Speed Test", "https://www.speedtest.net"],
                 ["Hotstar", "https://www.disneyplus.com"], ["Snapchat", "https://www.snapchat.com"], ["Cambridge", "https://www.cambridge.org"],
                 ["Physics Wala", "https://www.pw.live/study/auth"]]
        
        if "hello" in query.lower():
            print("")
            print("Jarvis : Hi Sir! I am Jarvis!")
            print("")
            Speak("Hi Sir! I am Jarvis!")
            return True
        elif("bye" in query.lower() or "close yourself" in query.lower() or "shut down" in query.lower() or "shutdown" in query.lower() or "turn yourself off" in query.lower()):
            print("")
            print("Jarvis : Bye Bye Sir...")
            print("")
            Speak("Bye Bye Sir!")
            return False
        elif "go to sleep" in query.lower():
            print("")
            print("Jarvis : Sleep Mode Activated..")
            print("")
            Speak("Sleep Mode Activated...")
            main()
            return True
        elif "how are you" in query.lower():
            print("")
            print("Jarvis : I am well sir! What about You?")
            print("")
            Speak("I am Well Sir! What about You?")
            return True
        elif "time" in query.lower():
            print("")
            tz = None
            if 'london' in query.lower():
                tz = pytz.timezone('Europe/London')
            elif 'new york' in query.lower():
                tz = pytz.timezone('America/New_York')
            elif ('costarica' in query.lower()) or ('costa rica' in query.lower()):
                tz = pytz.timezone('America/Costa_Rica')
            elif 'chicago' in query.lower():
                tz = pytz.timezone('America/Chicago')
            elif 'los angeles' in query.lower():
                tz = pytz.timezone('America/Los_Angeles')
            elif 'mexico' in query.lower():
                tz = pytz.timezone('America/Mexico_City')
            elif 'dubai' in query.lower():
                tz = pytz.timezone('Asia/Dubai')   
            elif 'bangkok' in query.lower():
                tz = pytz.timezone('Asia/Bangkok')
            elif 'colombo' in query.lower():
                tz = pytz.timezone('Asia/Colombo')
            elif 'dhaka' in query.lower():
                tz = pytz.timezone('Asia/Dhaka')
            elif 'hong' in query.lower():
                tz = pytz.timezone('Asia/Hong_Kong')
            elif 'shanghai' in query.lower():
                tz = pytz.timezone('Asia/Shanghai')
            elif 'singapore' in query.lower():
                tz = pytz.timezone('Asia/Singapore')
            elif 'sydney' in query.lower():
                tz = pytz.timezone('Australia/Sydney')
            elif 'melbourne' in query.lower():
                tz = pytz.timezone('Australia/Melbourne')
            elif 'mosco' in query.lower():
                tz = pytz.timezone('Europe/Moscow')
            elif 'maldives' in query.lower():
                tz = pytz.timezone('Indian/Maldives')
            elif 'mauritius' in query.lower():
                tz = pytz.timezone('Indian/Mauritius')
            elif 'right now' in query.lower():
                tz = None
            
            now = dt.now(tz)
            ct = now.strftime("%H:%M:%S")
            hr, min, sec = ct.split(":")
            hr = int(hr)
            min = int(min)
            sec = int(sec)
            mx = "Am"
            if hr > 12:
                hr = hr-12
                mx = 'Pm'
            elif hr == 12 and (min > 0 or sec > 0):
                mx = 'Pm'
            print(f"Jarvis: The Time is {hr} : {min} : {sec} {mx}")
            print("")
            Speak(f"The Time is {hr}, {min}, {mx}")
        elif "open" in query.lower():
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    print(f"Jarvis : Opening {site[0]} Sir")
                    Speak(f"Opening {site[0]} Sir")
                    webbrowser.open(site[1])
        else:
            answer = ReplyBrain(query)
            print(f"Jarvis : {answer}")
            Speak(answer)