from selenium import webdriver
import os
from dotenv import load_dotenv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
PROMISED_UP = 500
PROMISED_DOWN = 1500
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
X_EMAIL = os.getenv("X_EMAIL")
X_PASSWORD = os.getenv("X_PASSWORD")
X_USERNAME = os.getenv("X_USERNAME")

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self,driver_path):
        self.driver.get(driver_path)
        time.sleep(3)

        try:
            accept_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
            accept_button.click()
        except:
            pass
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()
        time.sleep(60)

        current_link = self.driver.current_url
        self.driver.get(f"{current_link}#")
        time.sleep(5)

        self.down = float(self.driver.find_element(By.CLASS_NAME, value="download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, value="upload-speed").text)

        return self.up, self.down
    def tweet_at_provider(self, driver_path):
        self.driver.get(driver_path)
        time.sleep(3)

        email_input = self.driver.find_element(By.NAME, value="text")
        email_input.send_keys(X_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(3)

        try:
            username_input = self.driver.find_element(By.NAME, value="text")
            username_input.send_keys(X_USERNAME)
            username_input.send_keys(Keys.ENTER)
            time.sleep(3)
        except:
            pass
        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys(X_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(6)

        post_input = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post_input.send_keys(f"Hey Internet Provider, why is my internet speed {down}down/{up}up when I pay for 150down/10up?")

        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()
bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed(driver_path="https://www.speedtest.net/")
down = speed[1]
up = speed[0]
if down < PROMISED_DOWN or up < PROMISED_UP:
    bot.tweet_at_provider("https://x.com/i/flow/login")

