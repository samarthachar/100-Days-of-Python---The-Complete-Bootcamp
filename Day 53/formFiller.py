import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from BeautifulSoupRendering import addresses, prices, links

driver = webdriver.Chrome()

class FormFiller:
    def __init__(self, address, price, link ):
        time.sleep(1)

        driver.get("https://forms.gle/a4NbpgJSzDTBm5Vq5")

        time.sleep(2)

        address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(address)

        price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(price)

        link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input.send_keys(link)

        submit_button = driver.find_element(By.CSS_SELECTOR, value='.l4V7wb.Fxmcue')
        submit_button.click()

for index in range(len(addresses)):
    bot = FormFiller(addresses[index], prices[index], links[index])
driver.quit()