import os
import pyttsx3
import webbrowser as wb
import speech_recognition as sr

r = sr.Recognizer()

pyttsx3.speak("Welcome to JARVIS")

menu_list = ['chrome', 'firefox', 'explorer', 'media', 'vlc', 'mpc', 'notepad', 'notepad++', 'wordpad', 'calculator',
             'time', 'paint']


while True:
    # --> Start browser menu
    with sr.Microphone() as source:
        print("start saying...")
        audio = r.listen(source)
        print("i got your choice...")
    choice = r.recognize_google(audio)
    if (("chrome" in choice.lower()) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower()))):
        pyttsx3.speak("you have launched chrome")
        os.system("chrome")
    elif (("firefox" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched firefox")
        os.system("firefox")
    
    elif (("explorer" in choice.lower()) or ("internet" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched internet explorer")
        os.system("iexplore")
        # --> End of browser menu
    
        # --> Start of Media player menu
    elif (("vlc" in choice.lower())) and (
                    ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
                        "launch" in choice.lower())):
        pyttsx3.speak("you have launched v l c media player")
        os.system("vlc")
    elif (("window" in choice.lower()) or ("media" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched windows media player")
        os.system("wmplayer")
    elif (("mpc" in choice.lower()) or ("classic" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched media player")
        os.system("mpc-hc64")
    
    # <-- End of Media player menu
    
    # --> Start of Editor Menu
    elif (("notepad++" in choice.lower()) or ("notepad plus" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched notepad plus plus")
        os.system("notepad++")
    elif (("notepad" in choice.lower()) or ("text editor" in choice.lower()) or ("editor" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched notepad")
        os.system("notepad")
    elif (("wordpad" in choice.lower()) or ("pad" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched wordpad")
        os.system("wordpad")
    # <-- End of Editor Menu
    
    # --> Start of Accessories
    elif (("calculator" in choice.lower()) or ("calci" in choice.lower()) or ("calc" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched calculator")
        os.system("calc")
    elif (("paint" in choice.lower()) or ("draw" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched paint")
        os.system("mspaint")
    elif (("clock" in choice.lower()) or ("watch" in choice.lower()) or ("time" in choice.lower())) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        pyttsx3.speak("you have launched time date settings")
        os.system("timedate.cpl")
    # <-- End of Accessories
    
    # --> Start of single name entry     # example : what do you want to launch: "vlc"     elif (choice.lower() in menu_list and choice.lower() == "chrome"):         pyttsx3.speak("you have launched chrome")         os.system("chrome")       elif (choice.lower() in menu_list and choice.lower() == "firefox"):         pyttsx3.speak("you have launched firefox")         os.system("firefox")       elif (choice.lower() in menu_list and choice.lower() == "explorer"):         pyttsx3.speak("you have launched internet explorer")         os.system("iexplore")       elif (choice.lower() in menu_list and choice.lower() == "media"):         pyttsx3.speak("you have launched windwos media player")         os.system("wmplayer")       elif (choice.lower() in menu_list and choice.lower() == "vlc"):         pyttsx3.speak("you have launched v l c media player")         os.system("vlc")
    elif (choice.lower() in menu_list and choice.lower() == "mpc"):
        pyttsx3.speak("you have launched media player")
        os.system("mpc-hc64")
    elif (choice.lower() in menu_list and choice.lower() == "notepad"):
        pyttsx3.speak("you have launched notepad")
        os.system("notepad")
    elif (choice.lower() in menu_list and choice.lower() == "notepad++"):
        pyttsx3.speak("you have launched notepad++")
        os.system("notepad++")
    elif (choice.lower() in menu_list and choice.lower() == "wordpad"):
        pyttsx3.speak("you have launched wordpad")
        os.system("wordpad")
    elif (choice.lower() in menu_list and (choice.lower() == "calculator")):
        pyttsx3.speak("you have launched calculator")
        os.system("calc")
    elif (choice.lower() in menu_list and choice.lower() == "time"):
        pyttsx3.speak("you have launched date time setting")
        os.system("timedate.cpl")
    elif (choice.lower() in menu_list and choice.lower() == "paint"):
        pyttsx3.speak("you have launched paint")
        os.system("mspaint")
    # <-- End of single name entry
    
    #####################TODO
    
    if ("date" in choice.lower()) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        wb.open("http:192.168.43.155/cgi-bin/date.py")
    elif ("cal" in choice.lower() or "calender" in choice.lower()) and (
            ("run" in choice.lower()) or ("open" in choice.lower()) or ("execute" in choice.lower()) or (
            "launch" in choice.lower())):
        wb.open("http:192.168.43.155/cgi-bin/cal.py")
    elif ("current" in choice.lower() or "working directory" in choice.lower() or "pwd" in choice.lower()) and (
            ("run" in choice.lower()) or ("show" in choice.lower()) or ("open" in choice.lower()) or (
            "launch" in choice.lower())):
        wb.open("http:192.168.43.155/cgi-bin/pwd.py")
    elif ("network address" in choice.lower() or "ip" in choice.lower() or "ipaddress" in choice.lower()) and (
            ("run" in choice.lower()) or ("show" in choice.lower()) or ("open" in choice.lower()) or (
            "launch" in choice.lower())):
        wb.open("http:192.168.43.155/cgi-bin/ip.py")
    elif ("process" in choice.lower() or "running" in choice.lower() or "processes" in choice.lower()) and (
            ("run" in choice.lower()) or ("show" in choice.lower()) or ("open" in choice.lower()) or (
            "launch" in choice.lower())):
        wb.open("http:192.168.43.155/cgi-bin/process.py")
    elif ("files" in choice.lower() or "all files" in choice.lower() or "list" in choice.lower()) and (
            ("open" in choice.lower()) or ("show" in choice.lower()) or ("" in choice.lower()) or (
            "launch" in choice.lower())):
        wb.open("http:192.168.43.155/cgi-bin/ls.py")
    ###########
    
    # --> Start of Exit Program
    elif (("exit" in choice.lower()) or ("quit" in choice.lower()) or ("terminate" in choice.lower())):
        break
    # <-- End of Exit Program
    else:
        pyttsx3.speak("sorry, app not available")
        print(" :-( This app isn't available in App-Menu...")
