#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-
# Developed by Marc-Alx

from tkinter import *
from math import cos,sin,radians
from time import gmtime, strftime
import tkinter.messagebox

class Application(object):
    """ Hour """
    _Version,_Name=1.0,"Hour"
    _REFRESHTIME,_WIDTH,_HEIGHT,_CENTERX,_CENTERY,_RAD,_BGCOLOR=10,300,300,150,150,125,'white'
    _SECONDHANDLENGHT,_MINUTEHANDLENGHT,_HOURHANDLENGHT,_SECONDHANDWIDTH,_MINUTEHANDWIDTH,_HOURHANDWIDTH,_SECONDHANDCOLOR,_MINUTEHANDCOLOR,_HOURHANDCOLOR,_HOURMARKCOLOR,_HOURMARKWIDTH=70,100,120,1,2,3,'red','blue','black','black','2'
    _RDV=[]

    def __init__(self):
        self._tk = Tk()
        self._tk.protocol("WM_DELETE_WINDOW", self.onQuit)
        self._tk.title(self._Name)
        self.createMenuBar()
        self._tk.lift()
        self._tk.resizable(width=False, height=False)
        self._blockMiddle = Frame(self._tk)
        self._FRAME = Canvas(self._blockMiddle, width=self._WIDTH, height=self._HEIGHT, bg='white')
        if(sys.platform.startswith("darwin")):
            self._tk.bind_all('<Command-q>',self.quit)
            self._tk.bind_all('<Command-Q>',self.quit)
        self._FRAME.bind_all('<Key>',self.onKeyPress)
        self._FRAME.pack()
        self._blockMiddle.pack(side = LEFT)

        self.init()

    def mainloop(self):
        self._tk.mainloop()
    
    def about(self):
        tkinter.messagebox.showinfo("About", "Developed by\n\nMarc-Alexandre Blanchard\n\nmarc-alx@outlook.com")
    
    def createMenuBar(self):
        self.menubar = Menu(self._tk)
        self.appmenu = Menu(self.menubar, tearoff=0)
        self.appmenu.add_command(label="Quit", command=self._tk.destroy)
        self.menubar.add_cascade(label=self._Name, menu=self.appmenu)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.helpmenu.add_command(label="Help & How-To", command=self.help)
        self.helpmenu.add_command(label="Version", command=self.version)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self._tk.config(menu=self.menubar)
    
    def help(self):
        tkinter.messagebox.showinfo("Help & How-To", "About : A\nVersion : V\n\n\nRestart : R\n")
    
    def onKeyPress(self,event):
        if(event.char=="a" or event.char=="A"):
            self.about()
        elif(event.char=="v" or event.char=="V"):
            self.version()
        elif(event.char=="r" or event.char=="R"):
            self.init()
    
    def onQuit(self):
        self.cancelation()
        self._tk.destroy()

    def quit(self,event):
        self.onQuit()

    def version(self):
        tkinter.messagebox.showinfo("Version", "Version "+str(self._Version))

    def cancelation(self):
        for i in self._RDV:
            self._FRAME.after_cancel(i)

    def draw(self):
        self._FRAME.delete(ALL)
        self.drawCircle(self._CENTERX,self._CENTERY,self._RAD)
        self.drawMarks()
        self.drawHand(self._SECONDHANDLENGHT,self._SECONDHANDCOLOR,self._SECONDHANDWIDTH,radians((self.getSeconds()*6)-89))
        self.drawHand(self._MINUTEHANDLENGHT,self._MINUTEHANDCOLOR,self._MINUTEHANDWIDTH,radians((self.getMinutes()*6)-89))
        self.drawHand(self._HOURHANDLENGHT,self._HOURHANDCOLOR,self._HOURHANDWIDTH,radians(((self.getHours()-1)*30)))
        self._RDV.append(self._FRAME.after(self._REFRESHTIME,self.draw))

    def drawCircle(self,x,y,rad):
        self._FRAME.create_oval(x-rad,y-rad,x+rad,y+rad,width=1,fill='white')

    def drawHand(self,length,color,width,alpha):
        x = self._CENTERX + length * cos(alpha)
        y = self._CENTERY + length * sin(alpha)
        self._FRAME.create_line(self._CENTERX,self._CENTERY,x,y,fill=color,width=width)

    def drawMarks(self):
        for i in range(0,361,30):
            alpha = radians(i)
            x1 = self._CENTERX + (self._RAD-4) * cos(alpha)
            y1 = self._CENTERY + (self._RAD-4) * sin(alpha)
            x2 = self._CENTERX + (self._RAD+4) * cos(alpha)
            y2 = self._CENTERY + (self._RAD+4) * sin(alpha)
            self._FRAME.create_line(x1,y1,x2,y2,fill=self._HOURMARKCOLOR,width=self._HOURMARKWIDTH)

    def getSeconds(self):
        return int(strftime("%S", gmtime()))

    def getMinutes(self):
        return int(strftime("%M", gmtime()))

    def getHours(self):
        return int(strftime("%H", gmtime()))

    def init(self):
        self.cancelation()
        self.draw()

if __name__ == '__main__':
    Application().mainloop()
