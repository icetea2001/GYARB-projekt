import base64
import json
import requests

def b64_encode_str(data_str):
    data = base64.b64encode(data_str.encode("utf-8"))
    return str(data, "utf-8")


class Buss:
    def __init__(self, line, name, time, track, fg_color, bg_color):
        self.line = line
        self.name = name
        self.time = time
        self.track = track
        self.fg_color = fg_color
        self.bg_color = bg_color


class BussInfo:
    api_token_url = 'https://api.vasttrafik.se/token'
    api_departure_board_url = 'https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard'

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.basic_token = None
        self.access_token = None

        self.create_basic_token()

    def create_basic_token(self):
        self.basic_token = b64_encode_str(str(self.api_key) + ":" + str(self.api_secret))

    def create_access_token(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Basic {0}'.format(self.basic_token)}

        params = {"grant_type": "client_credentials", "scope": "nextbus"}

        data = json.loads(requests.post(self.api_token_url, params, headers=headers).text)
        self.access_token = data["access_token"]

    def get_buss_info(self, date):
        time = date.strftime('%H:%M')
        date = date.strftime('%Y-%m-%d')

        headers = {'Authorization': 'Bearer {0}'.format(self.access_token)}

        params = {'id': 9021014002740000, 'date': date, 'time': time, 'format': 'json'}

        req_res = requests.get(self.api_departure_board_url, params, headers=headers)
        data = json.loads(req_res.text)

        busses = data['DepartureBoard']['Departure']

        res = []
        for buss in busses:
            res.append(Buss(buss['sname'],
                            buss['direction'],
                            buss['time'],
                            buss['track'],
                            buss['fgColor'],
                            buss['bgColor']))

        return res
