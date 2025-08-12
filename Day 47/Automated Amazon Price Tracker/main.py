import os

from bs4 import BeautifulSoup
import requests
import smtplib
from unidecode import unidecode
from dotenv import load_dotenv

load_dotenv()

app_email = os.getenv("APP_EMAIL")
app_password = os.getenv("APP_PASSWORD")
to_email = os.getenv("TO_EMAIL")

link = "https://www.amazon.co.uk/Haikyuu-T-Shirt-Clothing-Karasuno-Volleyball/dp/B09Y676KSC/ref=sr_1_15?crid=FTISMDMTXJ7M&dib=eyJ2IjoiMSJ9.rDf1DMKz0EPlN6p_K7rQfm6qBNM1r9PXf7I2RRHHZHja2YZyrUeN6dQdZmM_B5EuYEl6zd5K72ltOx0Ak8RFmp-qmPZe-V7ik1ZKvp2k6jnGPIOSHJ9TQkthdt3V_jsLRRYyF84z5S2ekf5TdugbC-x-29xkHKr5UeVggJqGk0dXUYzvvPTCjfLduLCDv_RFnvlZXU5PTm5omM6j8ZKlTBhLiSES3qT4Rc3btqkMHQnu8FVUgeZJK1tregdOtZhU3gs298JSnesU_q3jGKQ_5lCK8UMzgfjoHN4LEuWBP54.pFA7dfBH9k6JYzSM2G3OffixXrQLhkX4phDJeAxTM8I&dib_tag=se&keywords=orange%2Banime%2Btshirt&qid=1754914021&sprefix=orange%2Banime%2Btshirt%2Caps%2C89&sr=8-15&th=1&psc=1"
target = 100

def get_price(url):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  }

    response = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    price_whole = soup.select_one(
        "div#corePriceDisplay_desktop_feature_div  span.a-price span.a-price-whole").text
    price_decimal = soup.select_one(
        "div#corePriceDisplay_desktop_feature_div  span.a-price span.a-price-fraction").text
    total_price = float(price_whole + price_decimal)
    big_title = soup.select_one("span#productTitle").text
    list_title = big_title.split()
    joined_title = " ".join(list_title)
    return total_price, joined_title

def send_email(final_price: float, final_title):

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=app_email, password=app_password)
        connection.sendmail(
            from_addr=app_email,
            to_addrs=to_email,
            msg=unidecode(f"Subject: Amazon Price Alert!\n\n{final_title} is now £{final_price}\n{link}")
        )


tpl = get_price(link)
price = tpl[0]
title = tpl[1]
if price < 20:
    send_email(price, title)


