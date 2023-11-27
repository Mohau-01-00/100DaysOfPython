import random
import smtplib
import datetime as dt



my_email="mohaumasukela@gmail.com"
password="nfinuwzdiiylckuu"

now=dt.datetime.now()
week_day=now.weekday()
print(now.weekday())

with open(file="quotes.txt") as quotes:
    contents=quotes.read()

    quote_list = contents.split("\n")

    random_quote=random.choice(quote_list)
    # print(random_quote)

weekday_list=[0,1,2,3,4]

if week_day  in weekday_list:
    print(random_quote)


with smtplib.SMTP('smtp.gmail.com',587) as connection:

    connection.starttls()
    connection.login(my_email,password)
    if week_day  in weekday_list:
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Monday Motivation\n\n{random_quote}")
        connection.sendmail(from_addr=my_email,to_addrs="mohau.masukela@vodacom.co.za",msg=f"Subject:Daily Motivation\n\n{random_quote}")
        connection.sendmail(from_addr=my_email,to_addrs="michael.kaudi@vodacom.co.za",msg=f"Subject:Daily Motivation\n\n{random_quote}")



