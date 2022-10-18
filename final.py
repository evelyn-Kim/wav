import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyaudio
import wave
from numpy import dot
from numpy.linalg import norm
from tkinter import*

FORMAT = pyaudio.paInt16

CHANNELS = 1

RATE = 44100

CHUNK = 1024

RECORD_SECONDS = 3.0

WAVE_OUTPUT_FILENAME = "save.wav"

audio = pyaudio.PyAudio()

# 녹음시작 함수
def record():
    stream = audio.open(format=pyaudio.paInt16, 

                    channels=CHANNELS, 

                    rate=RATE, 

                    input=True, 

                    frames_per_buffer=CHUNK)

    print("recording...")

    frames = []

 

    for j in range(0, int(RATE / CHUNK * RECORD_SECONDS)):

        data = stream.read(CHUNK)

        frames.append(data)

    print("finished recording")


#녹음종료 함수

    stream.stop_stream()

    stream.close()

    audio.terminate()

 

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, "wb")

    waveFile.setnchannels(CHANNELS)

    waveFile.setsampwidth(audio.get_sample_size(FORMAT))

    waveFile.setframerate(RATE)

    waveFile.writeframes(b''.join(frames))

    waveFile.close()

    return 0

# 소리분석 함수
def analyze():
    def cos_sim(A, B):
           return dot(A, B)/(norm(A)*norm(B))
        
    y1, sr1=librosa.load('bell.wav')
    
    x1=[]

    for i in range(20000):
        x1.append(y1[i])

    y2, sr2=librosa.load('car.wav')


    x2=[]

    for i in range(20000):
        x2.append(y2[i])

    y3, sr3=librosa.load('siren.wav')
   
    x3=[]

    for i in range(20000):
        x3.append(y3[i])

    y4, sr4=librosa.load('save.wav')
    
    x4=[]

    for i in range(20000):
        x4.append(y4[i])
    
    doc1=np.array(x1)

    doc2=np.array(x2)

    doc3=np.array(x3)

    doc4=np.array(x4)

    doclist = []

    doclist.append(cos_sim(doc1, doc4))

    doclist.append(cos_sim(doc2, doc4))

    doclist.append(cos_sim(doc3, doc4))

    if max(doclist) == cos_sim(doc1, doc4):
        lab2 = Label(w,text='벨소리', fg="black",font=100, padx=50, pady=20)
        lab2.pack()

    if max(doclist) == cos_sim(doc2, doc4):
        lab3 = Label(w,text='자동차 경적소리', fg="black",font=100, padx=50, pady=20)
        lab3.pack()

    if max(doclist) == cos_sim(doc3, doc4):
        lab3 = Label(w,text='사이렌 소리', fg="black",font=100, padx=50, pady=20)
        lab3.pack()
    
    return 0

w = Tk()
w.configure(bg="lavenderblush")
w.geometry("500x300")
w.title("소리 유사도 검사기")

lab1 = Label(w, text = "ෆ(•ө•)소리 입력하기(•ө•)ෆ", bg="lavenderblush", font=100, fg="black", padx=50, pady=10)
lab1.pack()

but1 = Button(w, text = "입력시작", command = record, font=100, bg="palevioletred", fg="lavenderblush", padx=28, pady=10)
but1.pack()

but2 = Button(w, text = "소리분석 시작", command = analyze, font=100, bg="palevioletred", fg="lavenderblush", padx=10 ,pady=10)
but2.pack()

w.mainloop()
