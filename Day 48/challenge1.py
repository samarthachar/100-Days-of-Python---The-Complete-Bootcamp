from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname_input = driver.find_element(By.NAME, value="fName")
lname_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value="email")

fname_input.send_keys("Samarth")
fname_input.send_keys(Keys.ENTER)

lname_input.send_keys("Achar")
lname_input.send_keys(Keys.ENTER)

email_input.send_keys("random.random@gmail.com")
email_input.send_keys(Keys.ENTER)

submit_button = driver.find_element(By.XPATH, value="/html/body/form/button")
submit_button.click()