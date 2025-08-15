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

