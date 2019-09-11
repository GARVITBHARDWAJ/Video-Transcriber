# -*- coding: utf-8 -*-
import io
import os

import audio_extractor
from google.oauth2 import service_account
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import subprocess
import threading
import translation
source_lan="en"
target="en"
n=audio_extractor.segments
#providing the key

credentials  = service_account.Credentials.from_service_account_file(r'C:/Users/steve/Downloads/samkey.json')
# Instantiates a client
client = speech.SpeechClient(credentials=credentials)

startTime = "00:00:00"
i = audio_extractor.interval

def calculate_start(start="",interval=0):
    arr=start.split(":")
    time=int(arr[0])*3600+int(arr[1])*60+int(arr[2])
    time+=interval
    hours=time//3600
    mins=(time-3600*hours)//60
    sec=time-mins*60-hours*3600

    if hours // 10 == 0:
        hour = '0' + str(hours)
    else:
        hour = str(hours)

    if mins // 10 == 0:
        min = '0' + str(mins)
    else:
        min = str(mins)

    if sec // 10 == 0:
        s = '0' + str(sec)
    else:
        s = str(sec)
    return hour +":"+ min +":"+ s

def srt(s):
    str(s)
    global startTime
    f = open("marvelhindi.srt", "a+")
    nextTime = calculate_start(startTime, i)
    a = [startTime]
    a.append(',000')
    a.append(" --> ")
    a.append(nextTime)
    a.append(',000')
    f.write(''.join(a) + '\n')
    f.write(s )
    startTime = nextTime
    f.write("\n\n")
    f.close()
final_arr=['', '', '', '']
def recognition(file, pos):
    # The name of the audio file to transcribe
    file_name = file
    # print(file_name)
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=source_lan)

    # Detects speech in the audio file
    response = client.recognize(config, audio)
    s = []
    for result in response.results:
        s.append(result.alternatives[0].transcript)

    final_arr[pos]=" ".join(s)

if __name__ == "__main__":
    print(n)
    for _ in range(n//4):
        audio_extractor.gen_set()
        t1 = threading.Thread(target=recognition, args=(r'0.wav', 0,))
        t2 = threading.Thread(target=recognition, args=(r'1.wav', 1,))
        t3 = threading.Thread(target=recognition, args=(r'2.wav', 2,))
        t4 = threading.Thread(target=recognition, args=(r'3.wav', 3,))
        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        audio_extractor.deleto(4)
        if (source_lan==target):
            for x in range(4):
                srt(final_arr[x])
        else:
            for x in range(4):
                srt((translation.translate(final_arr[x], target)))
                print(translation.translate(final_arr[x], target))


cmd= r"vlc C:\Users\steve\Desktop/final/"+audio_extractor.name

p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p1.communicate()

print("Done!")