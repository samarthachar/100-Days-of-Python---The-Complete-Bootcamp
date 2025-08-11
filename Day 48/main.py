from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_pounds = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_pennies = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_pounds.text}.{price_pennies.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[6]/a')
# print(bug_link.text)

dates = driver.find_elements(By.CSS_SELECTOR, value="div.event-widget div.shrubbery ul.menu time")
names = driver.find_elements(By.CSS_SELECTOR, value="div.event-widget div.shrubbery ul.menu a")

dictionary = {}
for i in range(0,len(dates)):
    dictionary[f"{i}"] = {"time": f"{dates[i].text}", "name": f"{names[i].text}"}

print(dictionary)
driver.quit()

