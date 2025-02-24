import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#chrome_driver=Chrome()
chrome_options = Options()
# let browser will not close
#chrome_options.add_experimental_option("detach", True)
#driver=Chrome(options=chrome_options)

driver=Chrome()
url="https://www.amazon.com"
driver.get(url)
except_txt='"dress"'
# search= driver.find_element(By.ID,'twotabsearchtextbox')
# search.send_keys('dress', Keys.ENTER)
# driver.implicitly_wait(10)
# actual_txt=driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
# assert except_txt == actual_txt, f"Error . Expected text: {except_txt}, but actual text: {actual_txt}"

# Wait for the search box element to be present
wait = WebDriverWait(driver, 10)  # Set a timeout of 10 seconds
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys('dress', Keys.ENTER)
wait = WebDriverWait(driver, 5) 
actual_txt=driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text


# You can remove the time.sleep() now
driver.quit()
