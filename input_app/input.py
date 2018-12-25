from Tkinter import *
from ttk import *

def setPeriod():
    period = open("/home/pi/sboard/display_app/period.txt", "w")
    p = periodcombo.get()
    period.write(p)
    period.close()

window = Tk()

window.title("Scorebord Input")

lblperiod = Label(window, text="Period: ")
lblperiod.grid(column=0, row=0)
periodcombo = Combobox(window)
periodcombo['values']= (0,1,2,3,4,"OT")
periodcombo.grid(column=1, row=0)
btnperiod = Button(window, text="Save", command=setPeriod)
btnperiod.grid(column=3,row=0)

lblhscore = Label(window, text="Home score: ")
lblhscore.grid(column=0, row=2)
btnhscore = Button(window, text = "+1")
btnhscore.grid(column=1, row=2)
btnhminus = Button(window, text = "-1")
btnhminus.grid(column=2, row=2)

lblascore = Label(window, text="Away score: ")
lblascore.grid(column=0, row=4)
btnascore = Button(window, text = "+1")
btnascore.grid(column=1, row=4)
btnaminus = Button(window, text = "-1")
btnaminus.grid(column=2, row=4)

lbltime = Label(window, text="Enter time in minutes for period: ")
lbltime.grid(column=0, row=6)
txttime = Entry(window, width=5)
txttime.grid(column=1, row=6)
btntime = Button(window, text="Start/Restart Time")
btntime.grid(column=3, row=6)

window.mainloop()
