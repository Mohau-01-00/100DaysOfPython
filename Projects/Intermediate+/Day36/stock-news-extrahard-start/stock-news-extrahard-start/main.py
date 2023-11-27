import requests
import pandas as pd
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
url="https://www.alphavantage.co/query"
api_key='3D1AHE5GS45A3ERC'



parameters={

     'symbol':STOCK,
     'apikey':api_key,
     'function':'TIME_SERIES_DAILY'
}


try:
     response = requests.get(url, params=parameters)
     response.raise_for_status()
     all_data = response.json()
     data=all_data["Time Series (Daily)"]
except KeyError:
     with open(file="stock.txt") as stock:
          all_data=stock.read()

          print(all_data)
        
       



data=all_data['Time Series (Daily)']








data_list=[value for (key,value) in data.items()]

yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data['4. close']
print(f"Yesterday Closing Price{yesterday_closing_price}")

day_before_yesterday_data=data_list[1]
day_before_closing_price=day_before_yesterday_data['4. close']
print(f" Day Before Yesterday{day_before_closing_price}")





## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

