import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def request_google_search(driver: Chrome):
    url = "https://www.google.com"
    driver.get(url)
    search_bar= driver.find_element(
        By.XPATH,
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea"
         )
    search_text="Youtube"
    search_bar.send_keys(search_text)
    time.sleep(10)
    
    search_bar.send_keys(Keys.ENTER)
    time.sleep(10)

def create_chrome_driver() -> Chrome:
    return Chrome()



if __name__ == '__main__':
    chrome_driver=create_chrome_driver()
    request_google_search(driver=chrome_driver)
    time.sleep(10)
    #chrome_driver.quit()
    # with create_chrome_driver() as chrome_driver:
    #     demo_keyboard_action(driver=chrome_driver)

        
