import smtplib

my_email="mohaumasukela@gmail.com"
password="nfinuwzdiiylckuu"


connection=smtplib.SMTP('smtp.gmail.com',465)
connection.ehlo()


connection.starttls()
connection.login(my_email,password)
connection.sendmail(from_addr=my_email,to_addrs="mohaumasukela@gmail.com",msg="Hello")
connection.close()

