#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:26:20 2018

@author: aayushbhargava
"""
import tkinter
#from Tkinter import *

#from tkinter.ttk import *
def quit1():
    top.destroy
#    sys.exit()

top = tkinter.Tk()
#s=Style()
#back = tk.Frame(master=mw, width=500, height=500, bg='black')
top.geometry("500x500")
top.title("enter_time")


hrs=tkinter.Label(top, text="Hours")
hrs.grid(row=0,column=0)

hours = tkinter.StringVar(top)
hours.set("00")
h = tkinter.OptionMenu(top, hours, "00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23")
h.grid(row=0,column=1,ipadx="50")

#-------------------------------------------------------------
mins=tkinter.Label(top, text="Minutes")
mins.grid(row=1,column=0)

minuts = tkinter.StringVar(top)
minuts.set("00")
m = tkinter.OptionMenu(top, minuts, "00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24",
"25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59",)
m.grid(row=1,column=1,ipadx="50")

#-------------------------------------------------------------
topics=tkinter.Label(top, text="topics")
topics.grid(row=2,column=0)

def passval():
    print(hours.get())
    print(minuts.get())

tkinter.Button(top,text="PASS",command=passval).grid(row=3,column=2)
#hrs=tkinter.Label(top, textvariable="Hours").pack()
#.pack(side="left")



'''
hours = tkinter.StringVar(top)
hours.set("00") # default value
minuts = tkinter.StringVar(top)
minuts.set("00") # default value


h = tkinter.OptionMenu(top, hours, "00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23")
h.pack()

m = tkinter.OptionMenu(top, minuts, "00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24",
"25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59",)
m.pack()


def hours():
    print(hours.get())
def minuts():
    print(minuts.get())


tkinter.Button(top,text="print",command=hours).pack()
tkinter.Button(top,text="printx",command=minuts).pack()
top.protocol("Quit", quit1)
'''
top.mainloop()
