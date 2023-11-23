import requests
from datetime import datetime
import time
import pandas as pd

my_latt=-26.039511
my_long=28.004030



def read_csv():
    global data
    try:
        data=pd.read_csv("iss.csv") 
    except FileNotFoundError:
        data=pd.DataFrame()


#----------------------------------------------------------------------------------------


def check_time():
    global time_now
 
    '''Checks if TIME is sunset'''
    
    parameters={

        "lat":my_latt,
        "long":my_long,
        "formatted":0,

    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    #sunrise and sunset at my location taken from the sunrise api above
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now_full = datetime.now()
    time_now=time_now_full.hour
   
    if time_now>=sunset:
        return True
    else:
        return False
    


#----------------------------------------------------------------------------------------

def check_iss():
    global latt_diff,long_diff,iss_latitude,iss_longitude
    '''Function Checks ISS is in Range'''
        
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    #If the ISS is close to my current position
    latt_diff=iss_latitude-my_latt
    long_diff=iss_longitude-my_long

    if -5 <=latt_diff <=5 and -5 <=long_diff <=5:
        

        return True
    else:
        return False


#---------------------------------------------------------------------------------------

def dic_df():
    '''Create df from dic(new_data) '''
    #dictionary created to turn to dataframe for csv export

    global data
    # for some reason i had to declare global data here and at
    #read_csv

    new_data={

            "Time_Stamp":time_now,
            "Latt_Difference":latt_diff,
            "Long_Difference":long_diff,
            "Mohau_Long":my_long,
            "Mohau_Latt":my_latt,
            "ISS_Latt":iss_latitude,
            "ISS_Long":iss_longitude
        
    }

    data = pd.concat([data, pd.DataFrame([new_data])], ignore_index=True)
    

#----------------------------------------------------------------------------------------

should_continue=True
while should_continue:
    read_csv()
    check_time()
    check_iss()


    if check_iss():
       dic_df()

       data["Range"]="True"
       data.to_csv("iss.csv", index=False)
    

    elif  check_iss() and check_time():
       
        dic_df()

        data["Range"]="True"
        data.to_csv("iss.csv", index=False)



    else:

        dic_df()
        data["Range"]="False"
        data.to_csv("iss.csv", index=False)
    

    time.sleep(100) 
    print(data)
    




