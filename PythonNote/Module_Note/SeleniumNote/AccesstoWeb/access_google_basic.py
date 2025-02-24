import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#This is access to google with basic method no function, or class

#chrome_driver=Chrome()
#chrome_options = Options()
# let browser will not close
#chrome_options.add_experimental_option("detach", True)
#driver=Chrome(options=chrome_options)

driver=Chrome()
url="https://www.google.com"
driver.get(url)
#time.sleep(10)
driver.implicitly_wait(10)
#WebDriverWait(driver, 5) 
# You can remove the time.sleep() now
driver.quit()
