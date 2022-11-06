import speech_recognition
from datetime import date
import pyttsx3
import time 

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
with speech_recognition.Microphone() as mic:
    print('Listening...')
    audio = robot_ear.listen(mic)

print("Robot: ...")

print("You:", you)

try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""    
print("You: ", you)

if you == "" in you:
     robot_brain = "I can't hear you (Please check your mic or restart the computer)"
elif you == "hello" in you:
    robot_brain = "Hello, Chez_Zak!"
elif you == "today" in you:
    today = date.today()
    robot_brain = today.strftime("%B, %d, %Y")
elif "how are you" in you:
    robot_brain = "Im fine, thanks!"
elif you == "time":
    now = datetime.now()
    robot_brain = current_time = now.strftime("%H hours, %M minutes, %S seconds")
elif you == "president" in you:
    robot_brain = "Vietnam's president is Nguyễn Xuân Phúc!"
    

print("Robot: ", robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
#More Update Comming Soon
