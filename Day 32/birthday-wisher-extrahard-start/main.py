##################### Extra Hard Starting Project ######################
import datetime as dt
import random, smtplib, pandas

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter) as file:
        content = file.read()
        new_content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="sha*********l.com", password="gg************gsg")
        connection.sendmail(
            from_addr="sh***********m",
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{new_content}"
        )

