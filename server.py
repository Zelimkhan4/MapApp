import requests
import json

URL = 'https://geocode-maps.yandex.ru/1.x/'
apikey = "40d1649f-0493-4b70-98ba-98533de7710b"


def get_ll(address):
    params = {'apikey': apikey, 'geocode': address, 'format': "json"}
    r = requests.get(URL, params=params)
    if r:
        data = r.json()
        ll = ','.join(data['response']["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]['pos'].split(' '))
        return ll
    print('Вы ввели неправильный адрес')
        