from tkinter import *
from tkinter import ttk, messagebox
from file_reading import *
from watering import *
import datetime
import time
import threading


class App():

    def __init__(self):
        self.root = Tk()
        self.root.title("Tabs")

        self.root.geometry('400x250')
        self.label1 = ttk.Label(self.root, text="hola"                  )
        self.label2 = ttk.Label(self.root, text="Estado: Funcionando...")
        self.label3 = ttk.Label(self.root, text="by: hola"              )

        self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL, style="line.TSeparator")

        self.tab_control = ttk.Notebook(self.root)
        self.tab     = []
        self.buttons = []

        self.tabs()

        self.label1.place(x=50,  y=50 )
        self.label2.place(x=195, y=50 )
        self.label3.place(x=5,   y=230)

        self.separ1.place(x=5,   y=95, bordermode=OUTSIDE, height=10, width=390)
        
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
                ttk.Button(self.tab[x], text='manual'      , padding=(5,5), command= lambda c=x: print(self.buttons[c][0].cget("text"))),
                ttk.Button(self.tab[x], text='a'           , padding=(5,5), command= lambda c=x: print(self.buttons[c][1].cget("text"))),
                ttk.Button(self.tab[x], text='siguiente'   , padding=(5,5), command= lambda c=x: print(self.buttons[c][2].cget("text"))),
                ttk.Button(self.tab[x], text='parar manual', padding=(5,5), command= lambda c=x: print(self.buttons[c][3].cget("text")))
                ])

            self.buttons[x][0].place(x=95,  y=135)
            self.buttons[x][1].place(x=215, y=135)
            self.buttons[x][2].place(x=95,  y=105)
            self.buttons[x][3].place(x=215, y=105)

        self.tab_control.pack(expand=100, fill='both')



    def clock(self):#################33
        self.label1.configure(text=time.strftime("%H : %M : %S    Dia: ")+str(datetime.datetime.today().weekday()+1))
        if(lec[1] == True):
            self.label2.configure(text="Estado: riego manual")
        elif(lec[2] == True):
            self.label2.configure(text="Estado: off")
        elif(not lec[0] == False):
            self.label2.configure(text="Estado: regando Auto, zon: "+str(lec[0]))
        else:
            self.label2.configure(text="Estado: funcionando...")
        self.root.after(1000, self.reloj)

    def stop(self):
        self.root.destroy()
    def manual(self):
        pass
    def next(self):
        pass



class buclesRiego():
    def __init__(self, name, data):

        self.data = data

        self.watering = watering(data[0], data[2], data[2][0], data[1], data[3])#zon, t, T_ini, pin, dia
        self.thread = threading.Thread(target=self.bucle, args=())
        self.thread.start()

    def bucle(self):
        while True:
            self.watering.checkWeekday()
            time.sleep(0.3)
            if(lec[1] == True):############33
                self.watering.manual()
            elif(lec[2] == True):
                lectura.escribirParam("riego", False)
                lectura.escribirParam("off", False)
                lectura.escribirParam("manual", False)
                quit()


def mainApp():
    app = App()

mainApp()
    
'''
def bucles():
    a = buclesRiego(1)

th1 = threading.Thread(target=mainApp, args=())
th1.start()'''
