import os

from rain_times import print_str
import smtplib

app_email = "shadowsharinganrainreminder@gmail.com"
app_password = "qzbi ofgb gfri oscs"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=app_email, password=app_password)
    connection.sendmail(
        from_addr=app_email,
        to_addrs="s************2@gmail.com",
        msg=f"Subject: RAIN INCOMING: BRING UMBRELLA\n\n{print_str}"
    )