import requests
import json

filename = "settings.json"
json_filename = "out/data.json"
save_out_data = "out/out.json"

conditions = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями',
              'overcast': 'пасмурно', 'drizzle': 'морось', 'light-rain': 'небольшой дождь',
              'rain': 'дождь', 'moderate-rain': 'умеренно сильный', 'heavy-rain': 'сильный дождь',
              'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
              'wet-snow': 'дождь со снегом', 'light-snow': 'небольшой снег', 'snow': 'снег',
              'snow-showers': 'снегопад', 'hail': 'град', 'thunderstorm': 'гроза',
              'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'}

wind_dir = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное', 'e': 'восточное',
            'se': 'юго-восточное', 's': 'южное', 'sw': 'юго-западное', 'w': 'западное', 'с': 'штиль'}

season = {
    'summer': 'лето',
    'winter': 'зима',
    'spring': 'весна',
    'autumn': 'осень'
}


def open_file(file_name):
    with open(file_name, "r", encoding="UTF-8") as file:
        readfile = file.read()
    return json.loads(readfile)


def write_json_weather(file_name_json, data):
    with open(file_name_json, "w") as file:
        json.dump(data, file, indent=4)


settings_json = open_file(filename)

token = settings_json['token']
api_url = settings_json['url']

payload = {
    'lat': '55.753215',
    'lon': '37.622504',
    'units': 'metric',
    'lang': 'ru'
}


def get_weather(url, settings):
    load_temp = requests.get(url, settings, headers=token)
    write_json_weather(json_filename, json.loads(load_temp.text))


def parse_yandex(json_data_file):
    json_data = open_file(json_data_file)
    json_data['fact']['condition'] = conditions[json_data['fact']['condition']]
    json_data['fact']['wind_dir'] = wind_dir[json_data['fact']['wind_dir']]
    json_data['fact']['season'] = season[json_data['fact']['season']]
    print(json_data)
    write_json_weather(save_out_data, json_data)



if __name__ == '__main__':
    get_weather(api_url, payload)
    parse_yandex(json_filename)