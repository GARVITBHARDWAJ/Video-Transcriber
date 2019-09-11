import subprocess
import os
time=0

start="00:00:00"
name="marvelhindi.mp4"
duration="00:02:00"
interval=10
arr=duration.split(":")
time=int(arr[0])*3600+int(arr[1])*60+int(arr[2])
hours=time//3600
mins=(time-3600*hours)//60
sec=time-mins*60-hours*3600
duration_in_sec=hours*3600+mins*60+sec


segments = duration_in_sec//interval;
def calculate_start(start="",interval=0):
    arr=start.split(":")
    time=int(arr[0])*3600+int(arr[1])*60+int(arr[2])
    time+=interval
    hours=time//3600
    mins=(time-3600*hours)//60
    sec=time-mins*60-hours*3600
    return str(hours)+":"+str(mins)+":"+str(sec)


def gen_set():
    global start
    for x in range(0,4,1):

        cmd_trim="ffmpeg -i "+name+" -ss "+start+" -t 00:00:"+str(interval)+".0 -ar 16000 -ac 1 "+str(x)+".wav"
        start=calculate_start(start,interval)
        p1 = subprocess.Popen(cmd_trim, stdout=subprocess.PIPE)
        p1.communicate()

def deleto(n):
    for x in range(n):
        os.remove(str(x)+".wav")
