import os
import smtplib
import datetime as dt
import random
import pandas

PLACEHOLDER = "[NAME],"

my_email = "your_email@gmail.com"
my_pass = "generate app password from google account"

data = pandas.read_csv("birthdays.csv")
birthday = data.to_dict(orient="records")
print(birthday)
today = dt.datetime.now()
day = today.day
for birth in birthday:
    if birth["day"] == day:
        thr_email = birth["email"]
        message_choice = random.choice(os.listdir("letter_templates"))
        print(message_choice)
        with open(f"./letter_templates/{message_choice}") as letter_file:
            letter_contents = letter_file.read()
            stripped_name = f"{birth['name']},"
            new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
            print(new_letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:  # smtp can change according to your Email.
            connection.starttls()
            connection.login(my_email, my_pass)
            connection.sendmail(from_addr=my_email, to_addrs=thr_email, msg=f"Subject:Happy Birthday\n\n{new_letter}")
