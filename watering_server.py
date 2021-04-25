import socket
import time
import json
import threading

from file_reading import *
from watering import *

MAIN_AREAS = []

HEADERSIZE = 10
port = 1235

data = {}

is_server_active = True
is_watering_active = True

def send_data():
    print("·")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((socket.gethostname(), port))
    s.listen(5)
    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")

        clientsocket.send(bytes(data,"utf-8"))


def waterings():
    for w in read():
        print(w,read()[w])
        try:
            MAIN_AREAS.append(wateringLoops(w,read()[w]))
        except:
            print("E5")
    print("A")
    while is_watering_active:
        global data
        state = []
        for w in MAIN_AREAS:
            w.tick()
            wi = w.watering.is_watering
            wm = w.watering.is_manual
            wl = w.watering.active_area
            state.append({'is_watering':wi,'is_manual':wm,'active_area':wl})

        data = json.dumps({'state_areas':state})
        data = f"{len(data):<{HEADERSIZE}}"+data



class wateringLoops():
    def __init__(self, name, data):
        self.data = data
        self.name = name
        self.watering = watering(
            data[0], 
            data[1], 
            data[2], 
            data[3], 
            data[4])#zon, t, T_ini, pin, dia

    def tick(self):
        self.watering.check()
        
        '''if(state[1] == True):############33
            self.watering.manual()'''
        '''if(self.watering.is_watering):
            state[0] = self.watering.active_area
        elif(state[2] == True):
            state[0] = False
            state[2] = False
            state[1] = False
            quit()
        else:
            state[0] = self.watering.is_watering
        state[1] = self.watering.is_manual'''



    
th1 = threading.Thread(target=send_data, args=())
th1.start()
th2 = threading.Thread(target=waterings, args=())
th2.start()