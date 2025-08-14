import os, time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


load_dotenv()
SIMILAR_ACCOUNT = "el0n_rev_musk"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/")

        time.sleep(3)

        try:
            safety_click = self.driver.find_element(By.CLASS_NAME, value="_akzz")
            safety_click.click()
        except:
            pass

        accept_cookies = self.driver.find_element(By.CSS_SELECTOR, value='._a9--._ap36._asz1')
        accept_cookies.click()
        time.sleep(3)

        username_input = self.driver.find_element(By.NAME, value="username")
        username_input.send_keys(USERNAME)

        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys(PASSWORD)

        log_in_button = self.driver.find_element(By.CSS_SELECTOR, value='button._aswp._aswr._aswu._asw_._asx2')
        log_in_button.click()
        time.sleep(10)

        save_info_button = self.driver.find_element(By.CSS_SELECTOR, value='button._aswp._aswr._aswu._asw_._asx2')
        save_info_button.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5.2)
        modal = self.driver.find_element(By.XPATH, "//span[contains(text(), 'followers')]")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

#-- This Project doesn't work as Instagram has updated its terms of service, so I cannot access the modal with selenium. --#

