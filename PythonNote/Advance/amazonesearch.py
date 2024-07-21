import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# https://www.youtube.com/watch?v=XaoQi6L34vE&t=218s

def create_chrome_driver ()-> Chrome:
    return Chrome()

def request_amazon(driver: Chrome):
    url="https://www.amazon.com"
    driver.get(url)
    #driver.implicitly_wait(10)
    time.sleep(10)
    search= driver.find_element(By.ID,'twotabsearchtextbox')
    search.send_keys('dress', Keys.ENTER)
    except_txt='"dress"'
    driver.implicitly_wait(10)
    actual_txt=driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
    assert except_txt == actual_txt, f"Error . Expected text: {except_txt}, but actual text: {actual_txt}"
    #time.sleep(10)
    #driver.quit()
    

def request_site(driver: Chrome):
    url="https://www.amazon.com"
    driver.get(url)
    time.sleep(20)
    
if __name__ == '__main__':
    #print ("hello")
    chrome_driver=create_chrome_driver()
    
    request_site(driver=chrome_driver)
    #request_amazon(driver=chrome_driver)
    # chrome_driver.quit()
    #with create_chrome_driver() as chrome_driver:
        #demo_keyboard_action(driver=chrome_driver)
