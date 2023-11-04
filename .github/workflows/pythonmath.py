import pyttsx3
import math
pi = 3.14159265359
def speak(thisisinput):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    voices = engine.getProperty('voices')
    engine.say(thisisinput)
    engune.runAndWait()

justsomevectors = [0,1,2,3,4,5,6,7,8,9,10]

input1 = input("Yo want to do some math I got the formula for converting degrees to radians ")
speak("Yo do you want to do some math i got the formula for converting degrees to radians")
if input1 == "yes":
    speak("Enter the rad")
    rad = (int(input("Enter the rad: ")))
    answer1 = 180/pi
    fullanswer = rad/answer1
    print(f"The {rad} radians to degrees is {fullanswer}")
    speak(f"The {rad} radians to degrees is {fullanswer}")

if input1 == 'secret':
    secret2 = input("Whats the vectors?: ")
    secret3 = input("Whats the first vector?: ")
    speak("Whats the first vector")
    if secret3 == justsomevectors[1]:
        print("good i'm just gonna guess you know them now lol")
    
