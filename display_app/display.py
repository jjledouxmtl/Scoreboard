import Tkinter as tk
import time

clocktime = 1200
hscore = 0
ascore = 0
period = 1


def formattime(t):
    mins, secs = divmod(t, 60)
    t = '{:02d}:{:02d}'.format(mins, secs)
    return t

def readTime():
    intime = open("time.txt", "r")
    global clocktime
    clocktime = int(intime.read())
#    print(clocktime)

def readHScore():
    inHScore = open("hscore.txt", "r")
    global hscore
    hscore = int(inHScore.read())
#    print(hscore)

def readAScore():
    inAScore = open("ascore.txt", "r")
    global ascore
    ascore = int(inAScore.read())
#    print(ascore)

def readPeriod():
    inPeriod = open("period.txt", "r")
    global period
    period = int(inPeriod.read())
#    print(period)

def downtime():
    global timerem
    timerem -= 1
    mins, secs = divmod(timerem, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    return timeformat


def Draw():
    global period
    global pdis
    global hscore
    global ascore
    global sdis
    global clocktime
    global cdis
    global timerem
    readPeriod()
    readHScore()
    readAScore()
    distime = formattime(clocktime)
    timerem = clocktime
    frame=tk.Frame(root, width=500, heigh=500, relief="solid", bd=1)
    frame.place(x=10,y=10)
    pdis = tk.Label(frame, text = "Period: " + str(period))
    pdis.grid(column=0, row=1)
    sdis = tk.Label(frame, text = "Home: " + str(hscore) + "  Away: " + str(ascore))
    sdis.grid(column=0, row=3)
    cdis = tk.Label(frame, text = distime)
    cdis.grid(column=0, row = 5) 

def Refresh():
    global pdis
    global period
    global hscore
    global ascore
    global sdis
    global clocktime
    global cdis
    global timerem
    readPeriod()
    readHScore()
    readAScore()
    distime = downtime()
    pdis.configure(text = "Period: " + str(period))
    sdis.configure(text = "Home: " + str(hscore) + "  Away: " + str(ascore))
    cdis.configure(text = distime)
    root.after(1000, Refresh)

root=tk.Tk()
Draw()
Refresh()
root.mainloop()
