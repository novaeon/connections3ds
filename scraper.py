from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import chromedriver_autoinstaller
import time
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
# Define window size here
"--window-size=1200,1200",
    "--ignore-certificate-errors"

    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200", 
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options = chrome_options)
url = "https://www.nytimes.com/games/connections"

driver.get(url)

try:
    cookies = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Reject all')]"))
    )
    time.sleep(0.5)
    cookies.click()
except TimeoutException:
    pass

play = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Play')]"))
)
time.sleep(0.5)
play.click()

try:
    tutorial = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[6]/div[3]/div/div/div[2]/div/div[1]"))
    )
    time.sleep(0.5)
    tutorial.click()
except TimeoutException:
    pass

time.sleep(0.5)
words = [word.text for word in driver.find_elements(By.XPATH, "//div[contains(concat(' ', normalize-space(@class), ' '), ' item ')]")]
with open('words.txt', 'w') as file:
    file.write(','.join(words))
