import pandas
from datetime import datetime
import random
import smtplib

my_email  = "pranav.mullapudi@gmail.com"
password = "Greenview08"

number_guess = random.randint(1,3)

print(number_guess)

today = datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv(r"C:/Users/prana/OneDrive/Documents/Python Scripts/100 days/birthdaywisher/birthdays.csv")


birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"C:/Users/prana/OneDrive/Documents/Python Scripts/100 days/birthdaywisher/letter_templates/letter_{number_guess}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
    
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday!\n\n{contents}"
                        )
    connection.close()