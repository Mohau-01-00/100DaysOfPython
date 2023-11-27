with smtplib.SMTP('smtp.gmail.com',587) as connection:

    connection.starttls()
    connection.login(my_email,password)

    connection.sendmail(from_addr=my_email,to_addrs="mohau.masukela@vodacom.co.za",msg=random_quote)





