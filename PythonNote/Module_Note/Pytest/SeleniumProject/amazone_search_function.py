import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_chrome_driver ()-> Chrome:
    chrome_options = Options()
    #will not close browser
    #chrome_options.add_experimental_option("detach", True)
    #return Chrome(options=chrome_options)
    return Chrome

#using implicitly_wait 
def request_amazon(driver: Chrome):
    url="https://www.amazon.com"
    driver.get(url)
    #driver.implicitly_wait(10)
    #time.sleep(10)
    search= driver.find_element(By.ID,'twotabsearchtextbox')
    search.send_keys('dress', Keys.ENTER)
    except_txt='"dress"'
    driver.implicitly_wait(10)
    actual_txt=driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
    assert except_txt == actual_txt, f"Error . Expected text: {except_txt}, but actual text: {actual_txt}"

# Explicit Waits
def request_amzaon_new(driver: Chrome):
    url="https://www.amazon.com"
    driver.get(url)
    #driver.implicitly_wait(5)
    except_txt='"dress"'
    
    wait = WebDriverWait(driver, 10)  # Set a timeout of 10 seconds
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys('dress', Keys.ENTER)
    wait = WebDriverWait(driver, 5) 
    actual_txt=driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
    assert except_txt == actual_txt, f"Error . Expected text: {except_txt}, but actual text: {actual_txt}"

def request_site(driver: Chrome):
    url="https://www.google.com"
    driver.get(url)
    time.sleep(10)

if __name__ == '__main__':
    chrome_driver=create_chrome_driver()
    request_amazon(driver=chrome_driver)
    chrome_driver.quit()

