import smtplib

my_email="mohaumasukela@gmail.com"
password="nfinuwzdiiylckuu"


connection=smtplib.SMTP('smtp.gmail.com',587)

connection.starttls()
connection.login(my_email,password)
connection.sendmail(from_addr=my_email,to_addrs="mohau.masukela@vodacom.co.za",msg="Hello")
connection.close()

