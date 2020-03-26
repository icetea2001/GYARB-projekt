import math
from tkinter import *
import requests
from pprint import pprint
from PIL import Image, ImageTk
from urllib.request import urlopen
import base64
import io
import cv2

import datetime

import requests
import base64

import BussInfo

from FaceReconitionCode import FaceReconition
import current

from Rasmus import Rasmus
from Isac import Isac

lastFace = "Unknown"

date = datetime.datetime.now()

buss_info = BussInfo.BussInfo('ph7QCU5JM95Kh8IcP81Sk6Y4Smsa', '3eU64rOqVMzKPasOzh_c9pTvV18a')
buss_info.create_access_token()

MainWindow = Tk()

def key(event):
    if event.char == '\r':
        MainWindow.destroy()

width_value=MainWindow.winfo_screenwidth()
height_value=MainWindow.winfo_screenheight()
MainWindow.geometry("%dx%d" % (width_value, height_value))
# MainWindow.wm_attributes('-fullscreen', 'true')
MainWindow.configure(background="black")
MainWindow.bind("<Key>", key)



#https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=1e56ffbb3951c72be777701e5622f3a1&units=metric&lang=se



# API KEY
API_key = "1e56ffbb3951c72be777701e5622f3a1"

# This stores the url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# This will ask the user to enter city ID
city_id = "2711537"

# This is final url. This is concatenation of base_url, API_key and city_id
Final_url = base_url + "appid=" + API_key + "&id=" + city_id

# this variable contain the JSON data which the API returns
weather_data = requests.get(Final_url).json()

KevToCel = round(weather_data["main"]["temp"] - 273.15)


# JSON data is difficult to visualize, so you need to pretty print
pprint(KevToCel)

icon_url = "http://openweathermap.org/img/wn/" + weather_data["weather"][0]["icon"] + "@2x.png"

pprint(weather_data["weather"])
pprint(icon_url)


#Initiera Rasmus och Isac klassen
rasmus_data = Rasmus(MainWindow, [KevToCel])
isac_data = Isac(MainWindow)

def RunFaceRecognition():
    return "Rasmus"
    # https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=1e56ffbb3951c72be777701e5622f3a1&units=metric&lang=se


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        self.vid = FaceReconition(1)
        self.canvas = Canvas(MainWindow, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        #Hur ofta kameran ska uppdatera, startar också update metoden som senare kommer köras av sig själv
        self.delay = 15
        self.update()

        u = urlopen(icon_url)
        raw_data = u.read()

        load = Image.open(io.BytesIO(raw_data))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render, fg="black", bg="black")
        img.image = render
        img.place(x=1075, y=110)

        self.clock_label = Label(self, text="", fg="white", bg="black", font=("Arial", 34))
        self.clock_label.pack()

        self.buss_labels = []

        busses = buss_info.get_buss_info(datetime.datetime.now())
        y = 0
        for buss in busses:
            text = buss.line + " " + buss.name + " - " + buss.time + " - " + buss.track

            label = Label(self, text=text, fg="white", bg=buss.fg_color)
            label.pack()
            label.place(x=50, y = y)

            y += 30
            self.buss_labels.append(label)


        self.update_clock()

        self.clock_label.place(x=550, y=650)


    def update_clock(self):
        current_date_time = datetime.datetime.now()
        new_text = current_date_time.strftime("%H:%M:%S")
        self.clock_label.configure(text=new_text)
        self.after(1000, self.update_clock)

    # Uppdatera kameran
    def update(self):
        global lastFace
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo, anchor=NW)

            #uppdaterar data ifall ansiktet har ändrats
            if lastFace != current.name:
                self.update_data()
                lastFace = current.name

        #Kör update metoden igen
        self.master.after(self.delay, self.update)

    #Uppdatera datan
    def update_data(self):
        if current.name == "Rasmus":
            #Förstör isacs data och skapa rasmus
            isac_data.destroy_data()
            rasmus_data.get_data()
        elif current.name == "Isac":
            #Förstör rasmus data och skapa isacs
            rasmus_data.destroy_data()
            isac_data.get_data()




app = Window(MainWindow)
app.configure(bg="black")
width_value=MainWindow.winfo_screenwidth()
height_value=MainWindow.winfo_screenheight()
MainWindow.geometry("%dx%d" % (width_value, height_value))
MainWindow.wm_attributes('-fullscreen', 'true')
app.mainloop()