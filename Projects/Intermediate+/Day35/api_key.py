
import requests


api_key="6b02bb865310dfea9a86e713ee49eaea"
url="https://api.openweathermap.org/data/2.5/forecast"


parameters={

    'lat':-26.039511,
    'lon':28.004030,
    'appid':api_key,
    'units':'metric',
    'cnt':37
}

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()


weather_list=data['list']



for weather in weather_list:
    date=weather['dt_txt']
    print(date)
  
    w_descrip=weather['weather']
    # print(w_descrip)
    #output [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]
    
    for weather_type in w_descrip:
      weather_id=weather_type['id']
      print(weather_id) #output 802

      if weather_id<=500:
         print("its raining")





