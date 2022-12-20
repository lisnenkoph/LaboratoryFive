import requests
print(requests.get('http://api.covidtracking.com'))

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=3f0db68cab77504bcf6b9619d77b56f3&units=metric'.format(city)

res = requests.get(url)

data = res.json()

description = data['weather'][0]['description']
temp = data['main']['temp']
wind_speed = data['wind']['speed']
humidity = data['main']['humidity']
pressure = data['main']['pressure']

print('Description : ', f'{description}')
print('Temperature : ', f'{temp}', '°C')
print('Wind Speed : ', f'{wind_speed}', 'м/с')
print('Humidity : ', f'{humidity}', '%')
print('Pressure : ', f'{pressure}', 'мм рт. ст.')


url = 'https://api.covidtracking.com/v2/us/daily/2021-01-02/simple.json'

r = requests.get(url)
data = r.json()


states = data['data']['states']
date = data['data']['date']
cases = data['data']['cases']['total']
testing = data['data']['testing']['total']
hospitalized = data['data']['outcomes']['hospitalized']['currently']
icu = data['data']['outcomes']['hospitalized']['in_icu']['currently']
ventilator = data['data']['outcomes']['hospitalized']['on_ventilator']['currently']
death = data['data']['outcomes']['death']['total']


print('States : ', f'{states}')
print('Date : ', f'{date}')
print('Cases : ', f'{cases}')
print('Testing : ', f'{testing}')
print('Hospitalized : ', f'{hospitalized}'
      + ', из них в отделении интенсивной терапии', f'{icu}'
      + ', на искусственной вентиляции легких', f'{ventilator}')
print('Death : ', f'{death}')