import smtplib
import random
import datetime

my_email  = "pranav.mullapudi@gmail.com"
password = "Greenview08"

now = datetime.datetime.now()
day = now.weekday()
print(day)

if day == 1:
    with open(r"/100 days/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Monday Motivation\n\n{quote}")
    connection.close()