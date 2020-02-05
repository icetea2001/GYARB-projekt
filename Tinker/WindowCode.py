from tkinter import *
import requests
from pprint import pprint
from PIL import Image, ImageTk
from urllib.request import urlopen
import base64
import io


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

KevToCel = weather_data["main"]["temp"] -273.15

# JSON data is difficult to visualize, so you need to pretty print
pprint(KevToCel)

icon_url = "http://openweathermap.org/img/wn/" + weather_data["weather"][0]["icon"] + "@2x.png"

pprint(weather_data["weather"])
pprint(icon_url)



def RunFaceRecognition():
    return "Rasmus"

Face = RunFaceRecognition()

if Face == "Rasmus":
    print("Rasmus personliga infromation")
    theLabel = Label(MainWindow, text="", fg="white", bg="black")
    theLabel.pack()

    theLabel = Label(MainWindow, text=KevToCel, fg="white", bg="black")
    theLabel.pack()

else:
    print("Isac personliga infromation")
    theLabel = Label(MainWindow, text="Isac personliga infromation", fg="white", bg="black")
    theLabel.pack()

    # https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=1e56ffbb3951c72be777701e5622f3a1&units=metric&lang=se


class Window(Frame):
    def __init__(self, master=None):
        print("DEBUG: INIT")




        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)


        u = urlopen(icon_url)
        raw_data = u.read()

        load = Image.open(io.BytesIO(raw_data))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render, fg="black", bg="black")
        img.image = render
        img.pack()

app = Window(MainWindow)
width_value=MainWindow.winfo_screenwidth()
height_value=MainWindow.winfo_screenheight()
MainWindow.geometry("%dx%d" % (width_value, height_value))
MainWindow.wm_attributes('-fullscreen', 'true')
MainWindow.configure(background="black")
MainWindow.mainloop()