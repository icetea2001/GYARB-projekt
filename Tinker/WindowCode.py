from tkinter import *

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

def RunFaceRecognition():
    return "Rasmus"

Face = RunFaceRecognition()

if Face == "Rasmus":
    print("Rasmus personliga infromation")
    theLabel = Label(MainWindow, text="Rasmus personliga infromation", fg="white", bg="black")
    theLabel.pack()

    #Lägg in din skit här Isac.

else:
    print("Isac personliga infromation")
    theLabel = Label(MainWindow, text="Isac personliga infromation", fg="white", bg="black")
    theLabel.pack()

    #Lägg in din skit här Isac.

MainWindow.mainloop()