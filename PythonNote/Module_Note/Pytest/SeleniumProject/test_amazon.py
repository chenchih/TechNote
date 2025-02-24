import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class Testamazonsearch:     
    search_word= ('dress','shoes')
    
    def setup_method(self):
        self.driver=Chrome()
        self.driver.implicitly_wait(10)
        url="https://www.amazon.com"
        self.driver.get(url)

    #create a parametrize, when test case are doing the same thing
    @pytest.mark.parametrize('searching',search_word)
    def test_amazon_searching(self, searching):
        wait = WebDriverWait(self.driver, 10) 
        search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys(searching, Keys.ENTER)
        except_txt=f'\"{searching}\"'  #ignore quote \ 
        actual_txt=self.driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
        assert except_txt == actual_txt, f"Error . Expected text: {except_txt}, but actual text: {actual_txt}"
    
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






# def test_amazon_search_shoes():
#     driver=Chrome()
#     driver.implicitly_wait(10)
#     url="https://www.amazon.com"
#     driver.get(url)
#     #driver=self.driver
#     wait = WebDriverWait(driver, 10)  # Set a timeout of 10 seconds
#     search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
#     search_box.send_keys('shoes', Keys.ENTER)
#     wait = WebDriverWait(driver, 5) 
#     except_txt='"shoes"'
#     actual_txt=driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
#     assert except_txt == actual_txt, f"Error . Expected text: {except_txt}, but actual text: {actual_txt}"
#     driver.close()

