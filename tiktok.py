from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time




PATH = "C:\webdriver.exe"

driver = webdriver.Chrome(executable_path='C:/webdriver/chromedriver.exe')
driver.get("https://www.tiktok.com/foryou?lang=en")
print(driver.title)

#time.sleep(2)
#element = driver.find_element_by_xpath('')
#element.click()
#time.sleep(2)


button =  driver.find_element_by_css_selector('#main > div.jsx-1666249274.main-body.page-with-header.middle > div:nth-child(4) > div > div > main > div > div.jsx-1115548107.video-feed-container > span:nth-child(1) > div > div > div.jsx-179939359.jsx-2715883145.item-video-container > div.jsx-179939359.jsx-2715883145 > a > div > div > span.jsx-2055372491.event-delegate-mask')
button.click()
while True:
    try:
        time.sleep(9)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div.jsx-1666249274.main-body.page-with-header.middle > div:nth-child(4) > div > div > main > div > div.jsx-1331557196.video-card-big.browse-mode > div.jsx-1331557196.video-card-container > img.jsx-1169024735.control-icon.arrow-right"))).click()
    except TimeoutException:

        break



