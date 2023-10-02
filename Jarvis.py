from Body.Listen import MicExecution
from Body.Speak import Speak
from main import main
import webbrowser

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
            Speak("Hi Sir! I am Jarvis!")
            return True
        elif("bye" in query.lower() or "close yourself" in query.lower() or "shut down" in query.lower() or "shutdown" in query.lower()):
            Speak("Bye Bye Sir!")
            break
        elif "go to sleep" in query.lower():
            Speak("Sleep Mode Activated...")
            main()
            return True
        elif "how are you" in query.lower():
            Speak("I am Well Sir!")
            return True
        else:
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    Speak(f"Opening {site[0]} Sir..")
                    webbrowser.open(site[1])
            
MainExe()