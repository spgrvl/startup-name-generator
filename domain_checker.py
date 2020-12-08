from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re
import time

if os.name == "nt":
    chrome_path = r"C:\chromedriver_win32\chromedriver.exe"
elif os.name == "posix":
    chrome_path = "/usr/lib/chromium-browser/chromedriver"
else:
    print("Error: Chrome path is not set for this os: " + os.name)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

def check_availability(name):
    url = "https://instantdomainsearch.com/#search={}.com".format(name)
    driver.get(url)
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/section[2]/div[1]/div/div[1]/div/a'))
    )
    href = element.get_attribute('href')
    href_domain = re.search(r'^(?:http(?:s?)://)(?:www.)?([\w]+)\.[a-zA-Z]+', href)[1]
    driver.get("about:blank")
    if href_domain == name:
        return False
    else:
        return True

def quit_webdriver():
    driver.quit()