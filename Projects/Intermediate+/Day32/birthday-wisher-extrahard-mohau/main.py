# ##################### Extra Hard Starting Project ######################
import datetime as dt
import random

now=dt.datetime.now()



# Get the current day in the month
current_day=now.day
# Get the current month in the year
current_month=now.month


letter_list=["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]

random_letter=random.choice(letter_list)


with open("birthdays.csv") as file:
    contents=file.read()
    print(contents)
    detail_list=contents.split("\n")
    print(detail_list)


for birth_date in detail_list:
    
    birth_month=int(birth_date.split(",")[3])
    birth_day=int(birth_date.split(",")[4])
    name=birth_date.split(",")[0]

 
    if birth_month==current_month and birth_day==current_day:
        with open(random_letter) as letter:
            open_letter=letter.read()
            new_name=open_letter.replace("[NAME]",name)
            print(new_name)


    # print(birth_day)
    # print(birth_month)
    # print(name)





# 2. Check if tobirth_day matches a birthbirth_day in the birthbirth_days.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthbirth_days.csv



# 4. Send the letter generated in step 3 to that person's email address.

