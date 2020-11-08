from flask import Flask, request, render_template, flash
import win32com.client as wincl
import time
import speech_recognition as sr
import serial
import re

app = Flask(__name__)

@app.route('/')
@app.route('/registration')

ard_data=serial.Serial('COM5',9600)

speak = wincl.Dispatch("SAPI.SpVoice")

def servo_rot():
    ard_data.write('1')
    print('1')

def remove(string): 
	return string.replace(" ", "")

def index():
    return render_template('index.html')

def registration():
    for i in range(1):
        time.sleep(1)

    for i in range(1):
        speak.Speak("As part of corona protocole please state your name phone number and place where you are coming from")

    r=sr.Recognizer()
    print("please talk")
    with sr.Microphone() as source:
        audio_data=r.record(source, duration=7)
        print("Recognizing..")
        text_old=r.recognize_google(audio_data)
        print(text_old)
        text = remove(text_old)
        print(text)
        temp = re.compile('([a-zA-Z]+)([0-9]+)([a-zA-Z]+)')
        res = temp.match(text).groups()
        name_ex = str(res[0])
        ph_no = str(res[1])
        place_ex = str(res[2])
        with open('data.txt','a') as writer:
            writer.write(name_ex)
            writer.write('\t')
            writer.write(ph_no)
            writer.write('\t')
            writer.write(place_ex)
            writer.write('\n')
	name=name_ex
	mob=ph_no
	place=place_ex
	
	return render_template('exam.html', name=name,mob=mob,place=place)

if __name__ == "__main__":
    app.run()
    x=ard_data.read()
    if(x=='1'):
        registration()
        servo_rot()
    else:
        flash('Please Move Close to the Circle')