import csv
import pandas as pd

# with open("weather_data.csv") as data_file:
#   data=csv.reader(data_file)
#   temperature=[]
#   for row in data:
# #       if row[1]!="temp":
# #          temperature.append(int(row[1]))

# print(temperature)

# df=pd.read_csv('weather_data.csv')
# print(df)
# print(df['temp'])
# #get average temperature from temp series
# ave=df['temp'].mean()
# maximum=df['temp'].max()
# print(ave)
# print(maximum)

# max_temp=df[df['temp']==df['temp'].max()]
# print(max_temp)

# monday=df[df['day']=='Monday']
# print(monday)
# monday_temp=monday['temp'][0]
# monday_temp_F=monday_temp*9/5+32
# print(monday_temp_F)

#Creat a dataframe from scratch

data_dict={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]

}
df=pd.DataFrame(data_dict)
print(df)
df.to_csv('new_data.csv')



