import math
from tkinter import *
import requests
from pprint import pprint
from PIL import Image, ImageTk
from urllib.request import urlopen
import base64
import io

import datetime

import requests
import base64

MainWindow = Tk()
Face = ""

def key(event):
    if event.char == '\r':
        MainWindow.destroy()

width_value=MainWindow.winfo_screenwidth()
height_value=MainWindow.winfo_screenheight()
MainWindow.geometry("%dx%d" % (width_value, height_value))
MainWindow.wm_attributes('-fullscreen', 'true')
MainWindow.configure(background="black")
MainWindow.bind("<Key>", key)

def encode_str(data_str):
    data = base64.b64encode(data_str.encode("utf-8"))
    return str(data, "utf-8")

def get_access_token(secret, key):
    return encode_str(str(key) + ":" + str(secret))


api_key = "ph7QCU5JM95Kh8IcP81Sk6Y4Smsa"
api_secret = "3eU64rOqVMzKPasOzh_c9pTvV18a"
api_token = 'your_api_token'
api_url_base = 'https://api.vasttrafik.se/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Authorization': 'Basic {0}'.format(get_access_token(api_secret, api_key))}

params = {"grant_type": "client_credentials", "scope": "nextbus"}

print(requests.get(api_url_base, params))

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



def RunFaceRecognition():
    return "Rasmus"
    # https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=1e56ffbb3951c72be777701e5622f3a1&units=metric&lang=se


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        print("DEBUG: INIT")

        Face = RunFaceRecognition()

        if Face == "Rasmus":
            print("Rasmus personliga infromation")
            theLabel = Label(MainWindow, text="Rasmus personliga information", fg="white", bg="black", font=("Helvetica", 16))
            theLabel.pack()
            theLabel.place(x=620, y=180)

            theLabel2 = Label(MainWindow, text="Trångets södra väg 6", fg="white", bg="black", font=("Helvetica", 16))
            theLabel2.pack()
            theLabel2.place(x=667, y=210)

            theLabel3 = Label(MainWindow, text="423 42", fg="white", bg="black", font=("Helvetica", 16))
            theLabel3.pack()
            theLabel3.place(x=730, y=240)

            tempLabel = Label(MainWindow, text=(str(KevToCel) + " °C"), fg="white", bg="black", font=("Helvetica", 16))
            tempLabel.place(x=175, y=90)


        else:
            print("Isac personliga information")
            theLabel = Label(MainWindow, text="Isac personliga infromation", fg="white", bg="black")
            theLabel.pack()

        u = urlopen(icon_url)
        raw_data = u.read()

        load = Image.open(io.BytesIO(raw_data))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render, fg="black", bg="black")
        img.image = render
        img.place(x=145, y=110)

        self.clock_label = Label(self, text="", fg="white", bg="black", font=("Arial", 34))
        self.clock_label.pack()

        self.update_clock()

        self.clock_label.place(x=550, y=650)


    def update_clock(self):
        current_date_time = datetime.datetime.now()
        new_text = current_date_time.strftime("%H:%M:%S")
        self.clock_label.configure(text=new_text)
        self.after(1000, self.update_clock)



app = Window(MainWindow)
app.configure(bg="black")
width_value=MainWindow.winfo_screenwidth()
height_value=MainWindow.winfo_screenheight()
MainWindow.geometry("%dx%d" % (width_value, height_value))
MainWindow.wm_attributes('-fullscreen', 'true')
app.mainloop()