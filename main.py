from tkinter import *
from out import *
import priority
import processing

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.title("runway allocation")
root.minsize(width=400, height=400)
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background="#121212")
data = []
options = {"international", "diplomatic", "private", "domestic", "cargo"}
variable = StringVar(root)
variable.set("choose")


def addinfo():
    typeOfFlight = variable.get()
    variable.set("choose")
    nameOfFlight = nameOfFlightEntry.get()
    flightNo = flightNoEntry.get()
    time = int(hrEntry.get()) * 60 + int(minEntry.get())
    startBufferTime = int(startBufferTimeEntry.get())
    endBufferTime = int(endBufferTimeEntry.get())
    a = [typeOfFlight, time, startBufferTime, endBufferTime, nameOfFlight, flightNo]
    data.append(a)
    getinfo()


def addinfoanddestroy():
    typeOfFlight = variable.get()
    variable.set("choose")
    nameOfFlight = nameOfFlightEntry.get()
    flightNo = flightNoEntry.get()
    time = int(hrEntry.get()) * 60 + int(minEntry.get())
    startBufferTime = int(startBufferTimeEntry.get())
    endBufferTime = int(endBufferTimeEntry.get())
    a = [typeOfFlight, time, startBufferTime, endBufferTime, nameOfFlight, flightNo]
    data.append(a)
    root.destroy()
    priority.assign(data)
    processing.allocation(data)
    output(data)


def getinfo():
    global root, typeOfFlightEntry, nameOfFlightEntry, flightNoEntry, hrEntry, minEntry, startBufferTimeEntry, endBufferTimeEntry, data

    lb1 = Label(root, text="Type of flight : ", bg="#121212", fg='white', font=("Times new Roman", 24))
    lb1.place(relx=0.3, rely=0.095, relwidth=0.15, relheight=0.05)
    typeOfFlightEntry = OptionMenu(root, variable, *options)
    typeOfFlightEntry.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.05)

    lb2 = Label(root, text="Name of Airline : ", bg="#121212", fg='white', font=("Times new Roman", 24))
    lb2.place(relx=0.3, rely=0.195, relwidth=0.165, relheight=0.05)
    nameOfFlightEntry = Entry(root, bg='#C4C4C4')
    nameOfFlightEntry.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.05)

    lb3 = Label(root, text="Flight No : ", bg="#121212", fg='white', font=("Times new Roman", 24))
    lb3.place(relx=0.3, rely=0.295, relwidth=0.15, relheight=0.05)
    flightNoEntry = Entry(root, bg='#C4C4C4')
    flightNoEntry.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.05)

    lb4 = Label(root, text="Landing Time : ", bg="#121212", fg='white', font=("Times new Roman", 24))
    lb4.place(relx=0.3, rely=0.395, relwidth=0.15, relheight=0.05)
    hrEntry = Spinbox(root, from_=0, to=24, bg='#C4C4C4')
    hrEntry.place(relx=0.5, rely=0.4, relwidth=0.07, relheight=0.05)

    lb7 = Label(root, text="hrs", bg="#121212", fg='white', font=("Times new Roman", 24))
    lb7.place(relx=0.58, rely=0.395, relwidth=0.028, relheight=0.05)
    minEntry = Spinbox(root, from_=0, to=59, bg='#C4C4C4')
    minEntry.place(relx=0.63, rely=0.4, relwidth=0.07, relheight=0.05)
    lb8 = Label(root, text="mins", bg="#121212", fg='white', font=("Times new Roman", 24))
    lb8.place(relx=0.71, rely=0.395, relwidth=0.042, relheight=0.05)

    lb5 = Label(root, text="Pre Buffer Time : ", bg="#121212", fg='white', font=("Times new Roman", 24))
    lb5.place(relx=0.3, rely=0.495, relwidth=0.175, relheight=0.05)
    startBufferTimeEntry = Entry(root, bg='#C4C4C4')
    startBufferTimeEntry.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.05)

    lb6 = Label(root, text="Post Buffer Time : ", bg="#121212", fg='white', font=("Times new Roman", 24))
    lb6.place(relx=0.3, rely=0.595, relwidth=0.175, relheight=0.05)
    endBufferTimeEntry = Entry(root, bg='#C4C4C4')
    endBufferTimeEntry.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.05)

    SubmitBtn = Button(root, text="SUBMIT", bg='#03DAC6', activebackground='#03DAC6', fg='black',
                       font=("Times new Roman", 24), command=addinfoanddestroy)
    SubmitBtn.place(relx=0.35, rely=0.72, relwidth=0.18, relheight=0.08)
    NxtBtn = Button(root, text="Next", bg='#03DAC6', fg='black', activebackground='#03DAC6',
                    font=("Times new Roman", 24), command=addinfo)
    NxtBtn.place(relx=0.57, rely=0.72, relwidth=0.18, relheight=0.08)
    root.mainloop()


getinfo()