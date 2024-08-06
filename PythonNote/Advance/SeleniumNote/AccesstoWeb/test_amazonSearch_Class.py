import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class Testamazonsearch:     
    def setup_method(self):
        self.driver=Chrome()
        self.driver.implicitly_wait(10)
        url="https://www.amazon.com"
        self.driver.get(url)
    #without paraterize hotcode the search keyword 
    def test_amazon_search_dress(self):
        wait = WebDriverWait(self.driver, 10) 
        search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys('dress', Keys.ENTER)
        except_txt='"dress"'
        actual_txt=self.driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
        assert except_txt == actual_txt, f"Error . Expected text: {except_txt}, but actual text: {actual_txt}"
    def teardown_method(self):
        self.driver.quit()


#pytest with function
# def test_amazon_search_dress():
#     driver=Chrome()
#     #
#     url="https://www.amazon.com"
#     driver.get(url)
#     #driver=self.driver
#     wait = WebDriverWait(driver, 30)  # Set a timeout of 10 seconds
#     search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
#     search_box.send_keys('shoes', Keys.ENTER)
#     except_txt='"shoes"'
#     actual_txt=driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
#     assert except_txt == actual_txt, f"Error . Expected text: {except_txt}, but actual text: {actual_txt}"
#     driver.close()

