import os, datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()

ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")

link1 = "https://appbrewery.github.io/gym/"

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

driver.get(link1)
wait = WebDriverWait(driver, 2)

# Clicks on the login button
wait.until(ec.element_to_be_clickable((By.ID,"login-button"))).click()

#Inputs Email and Password into fields
email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.send_keys(ACCOUNT_EMAIL)
email_input.send_keys(Keys.ENTER)

password_input = wait.until(ec.presence_of_element_located((By.ID, "password-input")))
password_input.send_keys(ACCOUNT_PASSWORD)
password_input.send_keys(Keys.ENTER)

list_of_buttons = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, " button.ClassCard_bookButton__DMM1I")))
dates_and_buttons = {button.get_attribute("id")[17:]:button for button in list_of_buttons}
next_tuesday = __import__('datetime').datetime.now()+__import__('datetime').timedelta(days=(3-__import__('datetime').datetime.now().weekday()+7)%7 or 7);next_tuesday=next_tuesday.replace(hour=19,minute=0).strftime('%Y-%m-%d-%H%M')# Easy way to get next tuesday date
for datestamp in dates_and_buttons.keys():
    if datestamp == next_tuesday:
        print("✓ Booked: Spin Class on Tue, Aug 12")
        dates_and_buttons[datestamp].click()

