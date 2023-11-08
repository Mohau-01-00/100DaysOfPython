
import pandas as pd


#fur color,Count


df=pd.read_csv("2018_Central_Park_Squirrel_Census.csv")
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 150)
# print(df)

sq_color_count=df.groupby("Primary Fur Color")["Primary Fur Color"].count()
print(sq_color_count)

