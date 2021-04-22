from tkinter import *
from tkinter import ttk, messagebox

from file_reading import *
from watering import *

import json
import datetime
import time
import threading
import socket

state = [False,False,False]

port = 12351
HEADERSIZE = 10
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockt.connect(('127.0.0.1' port))

class App():

    def __init__(self):
        self.root = Tk()
        self.root.title("Tabs")

        self.root.geometry('400x250')
        self.tab_control = ttk.Notebook(self.root)

        self.label1 = ttk.Label(self.root, text="hola"                  )
        self.label2 = ttk.Label(self.root, text="Estado: Funcionando...")
        self.label3 = ttk.Label(self.root, text="by: hola"              )

        self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL, style="line.TSeparator")

        self.tab     = []
        self.buttons = []

        self.label1.place(x=50,  y=50 )
        self.label2.place(x=195, y=50 )
        self.label3.place(x=5,   y=230)

        self.separ1.place(x=5,   y=95, bordermode=OUTSIDE, height=10, width=390)

        self.tabs()
        
        self.clock()
    
        self.root.mainloop()

    def tabs(self):
        areas = read()
        if areas == "E4":
            messagebox.showerror("Error", areas)

        for x in range(len(areas)):
            self.tab.append(ttk.Frame(self.tab_control))
            self.tab_control.add(self.tab[x], text=str(x))
            self.buttons.append([
                ttk.Button(self.tab[x], text='manual'      , padding=(5,5), command= lambda c=x: self.manual(c)),
                ttk.Button(self.tab[x], text='a'           , padding=(5,5), command= lambda c=x: print(self.buttons[c][1].cget("text"))),
                ttk.Button(self.tab[x], text='siguiente'   , padding=(5,5), command= lambda c=x: print(self.buttons[c][2].cget("text"))),
                ttk.Button(self.tab[x], text='parar manual', padding=(5,5), command= lambda c=x: print(self.buttons[c][3].cget("text")))
                ])

            self.buttons[x][0].place(x=95,  y=135)
            self.buttons[x][1].place(x=215, y=135)
            self.buttons[x][2].place(x=95,  y=105)
            self.buttons[x][3].place(x=215, y=105)

        self.tab_control.pack(expand=100, fill='both')

    def client(self):
        full_msg = ''
        new_msg = True
        msg = sockt.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        while len(full_msg)-HEADERSIZE == msglen:
            full_msg += msg.decode("utf-8")

        data = json.loads(full_msg)
        return data

    def clock(self):#################3hay que hacerlo con todooooooos
        self.label1.configure(
            text=time.strftime("%H : %M : %S    Dia: ") +
            str(datetime.datetime.today().weekday()+1)
            )

        state = self.client()['state_areas'][0]
        try:
            if(state['is_manual']):
                self.label2.configure(text="Estado: riego manual")
            elif(state['is_watering']):
                self.label2.configure(text="Estado: regando Auto, zon: "+str(state['active_area']))
            else:
                self.label2.configure(text="Estado: funcionando...")
        except:
            self.label2.configure(text="Estado: off")

        self.root.after(1000, self.clock)

    def stop(self):
        self.root.destroy()
    def manual(self,pos):
        pass
        #a.watering.manual()
    def next(self):
        pass


app = App()