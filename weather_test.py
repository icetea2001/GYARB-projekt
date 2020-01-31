#https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=1e56ffbb3951c72be777701e5622f3a1&units=metric&lang=se

import requests
from pprint import pprint

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

load = Image.open(icon_url)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

pprint(weather_data["weather"])
pprint(icon_url)

