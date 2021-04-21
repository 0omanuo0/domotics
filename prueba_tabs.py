from tkinter import *
from tkinter import ttk, messagebox
from lectura import *
from riego import *
import datetime
import time
import threading


class App():

    def __init__(self):
        self.root = Tk()
        self.root.title("Tabs")
        
        #root.overrideredirect(1)
        self.root.geometry('400x250')
        self.tab_control = ttk.Notebook(self.root)
        self.label1 = ttk.Label(self.root, text="hola")
        self.label2 = ttk.Label(self.root, text="Estado: Funcionando...")
        self.label3 = ttk.Label(self.root, text="by: hola")
        self.separ1 = ttk.Separator(self.root, orient=HORIZONTAL, style="line.TSeparator")
        self.label1.place(x=50, y=50)
        self.label2.place(x=195, y=50)
        self.label3.place(x=5, y=230)
        self.separ1.place(x=5, y=95, bordermode=OUTSIDE, height=10, width=390)
        self.tab = []
        self.tab_control.pack(expand=100, fill='both')
        #self.reloj()
    
        self.root.mainloop()

    def tabs(self):
        self.zonas = read()
        if self.zonas == "error lectura":
            messagebox.showerror("Error", "Error lectura")
            #self.parar() 
        for x in range(len(self.zonas)):
            self.tab.append(ttk.Frame(self.tab_control))
            self.tab_control.add(self.tab[x], text=str(x))
            boton1 = ttk.Button(self.tab[x], text='manual', padding=(5,5), command= print("holaaa"))
            boton1.place(x=95, y=135)
            print("hola")
            '''exec("self.tab{} = ".format(x))
            exec("self.tab_control.add(self.tab{}, text='{}')".format(x,self.zonas[x][0]))
            exec("self.boton1{} = ttk.Button(self.tab{}, text='manual', padding=(5,5), command= self.Rmanual)".format(x,x))
            exec("self.boton2{} = ttk.Button(self.tab{}, text='salir', padding=(5,5), command= self.parar)".format(x,x))
            exec("self.boton3{} = ttk.Button(self.tab{}, text='siguiente', padding=(5,5), command= lambda: br({}))".format(x,x,x))
            exec("self.boton4{} = ttk.Button(self.tab{}, text='parar Manual', padding=(5,5), command= lambda: brn({}))".format(x,x,x))
            exec("self.boton1{}.place(x=95, y=135)".format(x))
            exec("self.boton2{}.place(x=215, y=135)".format(x))
            exec("self.boton3{}.place(x=95,y=105)".format(x))
            exec("self.boton4{}.place(x=215,y=105)".format(x))'''
'''
    def reloj(self):
        self.label1.configure(text=time.strftime("%H : %M : %S    Dia: ")+str(datetime.datetime.today().weekday()+1))
        lec = leerParam()
        if(lec[1] == True):
            self.label2.configure(text="Estado: riego manual")
        elif(lec[2] == True):
            self.label2.configure(text="Estado: off")
        elif(not lec[0] == False):
            self.label2.configure(text="Estado: regando Auto, zon: "+str(lec[0]))
        else:
            self.label2.configure(text="Estado: funcionando...")
        self.root.after(1000, self.reloj)
    def parar(self):
        escribirParam("riego", False)
        escribirParam("off", True)
        escribirParam("manual", False)
        self.root.destroy()
    def Rmanual(self):
        lectura.escribirParam("manual", True)#######lisbo[0]!!!!!!!! poner las zonas
class buclesRiego():
    def __init__(self, pos):
        self.p = pos
        s = ["pepe",3,"hola"]##
        d = [1,1,1]####cargar desde el programa raise NameError('HiThere')
        f = [14,3]####
        g = [14,15,18]####
        h = [True,True,True,True,True,True,False]
        lectura.escribirParam("parar", True)
        self.a = riego(s, d, f, g, h)
        self.bucle()
    def bucle(self):
        while True:
            self.a.comprobar()
            print(datetime.datetime.today().weekday())
            time.sleep(0.3)
            lec = lectura.leerParam()
            if(lec[1] == True):
                self.a.riegoManual()
            elif(lec[2] == True):
                lectura.escribirParam("riego", False)
                lectura.escribirParam("off", False)
                lectura.escribirParam("manual", False)
                quit()'''
def mainApp():
    app = App()
    
mainApp()
'''
def bucles():
    a = buclesRiego(1)

th1 = threading.Thread(target=mainApp, args=())
th1.start()
th2 = threading.Thread(target=bucles, args=())
th2.start()'''
