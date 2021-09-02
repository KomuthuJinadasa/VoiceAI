import speech_recognition
import pyttsx3

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()

while True:
    with speech_recognition.Microphone() as mic:
        print("AI Recognition: I'm listening")
        audio = robot_ear.listen(mic)

    try:
        user = robot_ear.recognize_google(audio)  
    except:
        user = ""

    print("User: " + user)

    if user == "" :
        robot_brain = "I can't hear you, please try again!"
    elif "hello" in user:
        robot_brain = "Hello User"
    elif "read" in user:
        robot_brain = "This is Tug Alpha. Yes, I read you"
    elif "VTS" in user:
        robot_brain = "Ship A, this is Melbourne VTS, go ahead"
    elif "bye" in user:
        robot_brain = "Bye!"
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break

    
    print("AI Recognition: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
