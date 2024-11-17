import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def demo_keyboard_action(driver: Chrome):
    url = "https://www.google.com/webhp?hl=zh-TW"
    driver.get(url)
    search_bar= driver.find_element(
        By.XPATH,
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea"
         )
    search_text="Hahow"
    # for i in search_text:
    search_bar.send_keys(search_text)
    time.sleep(5)
    
    search_bar.send_keys(Keys.ENTER)
    time.sleep(10)

def create_chrome_driver() -> Chrome:
    return Chrome()

def request_ptt_boards(driver: Chrome):
    url="https://www.ptt.cc/bbs/index.html"
    driver.get(url)
    time.sleep(10)

if __name__ == '__main__':
    # chrome_driver=create_chrome_driver()
    # request_ptt_boards(driver=chrome_driver)
    # chrome_driver.quit()
    with create_chrome_driver() as chrome_driver:
        demo_keyboard_action(driver=chrome_driver)

        
