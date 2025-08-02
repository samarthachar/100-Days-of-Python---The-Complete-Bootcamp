import datetime as dt
import smtplib
import random

def send_mail():
    with open("quotes.txt") as file:
        list_of_quotes = file.readlines()
        quote = random.choice(list_of_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="shadow.sharingan.test@gmail.com", password="ggng regn zbqw ngsg")
        connection.sendmail(
            from_addr="shadow.sharingan.test@gmail.com",
            to_addrs="shadow.sharingan.test@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 5:
    send_mail()


# import smtplib
#
# my_email = "shadow.sharingan.test@gmail.com"
# password = "ggng regn zbqw ngsg"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:#For Yahoo, "smtp.mail.yahoo.com"
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="shadowsharingantest@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
#
# date_of_birth = dt.datetime(year=2011, month=9,day=12)