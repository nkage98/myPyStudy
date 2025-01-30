import time
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'chromedriver-win64' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome: 

    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    chrome_service = Service(
        executable_path=CHROMEDRIVER_EXEC
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return browser

if __name__ == '__main__':

    options = ('--disable-gpu', ) # --headless
    browser = make_chrome_browser(*options)
    browser.get('https://myanimelist.net/anime/season')
    
    # search_input = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located(
    #         (By.NAME, 'q')
    #     )
    # )

    #search_input.send_keys('babado')
    #search_input.send_keys(Keys.ENTER)

    links = browser.find_elements(By.CLASS_NAME,'link-title')
    links[0].click()
    
    time.sleep(30) 


