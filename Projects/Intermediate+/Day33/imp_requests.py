import requests
from datetime import datetime

# response=requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data=response.json()

# longitude=float(data['iss_position']['longitude'])
# lattitude=float(data['iss_position']['latitude'])

# iss_position=(longitude,lattitude)
# print(iss_position)

MY_LAT=-26.039511
MY_LONG=28.004030
FORMATTED=0

#formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed
#lat (float): Latitude in decimal degrees. Required.



parameters={

    "lat":MY_LAT,
    "long":MY_LONG,
    "formatted":FORMATTED,

}


response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data=response.json()

sunrise=int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunrise=int(data['results']['sunset'].split("T")[1].split(":")[0])

time_now=datetime.now()
print(sunrise)

print(time_now.hour)
