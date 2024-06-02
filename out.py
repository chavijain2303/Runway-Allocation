from tkinter import *

def output(data):
	root = Tk()
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.title("runway allocation")
	root.minsize(width=400, height=400)
	root.geometry("%dx%d+0+0" % (w, h))
	root.configure(background="#1b262c")
	l=Label(root,text="RUNWAYS ALLOCATED",bg="#1b262c",fg='#3282b8',font=("Times new Roman",24,"bold"))
	l.place(relx=0.5,rely=0.026,anchor=CENTER)
	l=Label(root,text="Flight No",bg="#1b262c",fg='#bbe1fa',font=("Times new Roman",19,"underline"))
	l.place(relx=0.05,rely=0.069,anchor=CENTER)
	l=Label(root,text="Time",bg="#1b262c",fg='#bbe1fa',font=("Times new Roman",19,"underline"))
	l.place(relx=0.35,rely=0.069,anchor=CENTER)
	l=Label(root,text="Runway",bg="#1b262c",fg='#bbe1fa',font=("Times new Roman",19,"underline"))
	l.place(relx=0.65,rely=0.069,anchor=CENTER)
	j=0
	for flight in data:
		j=j+0.05
		l=Label(root,text=str(flight[5]),bg="#1b262c",fg='#bbe1fa',font=("Times new Roman",16))
		l.place(relx=0.05,rely=0.068+j,anchor=CENTER)
		time=flight[1]
		t=str(time//60)+":"+str(time%60)
		l=Label(root,text=str(t),bg="#1b262c",fg='#bbe1fa',font=("Times new Roman",16))
		l.place(relx=0.35,rely=0.068+j,anchor=CENTER)
		l=Label(root,text=str(flight[6]),bg="#1b262c",fg='#bbe1fa',font=("Times new Roman",16))
		l.place(relx=0.65,rely=0.068+j,anchor=CENTER)
		

	root.mainloop()