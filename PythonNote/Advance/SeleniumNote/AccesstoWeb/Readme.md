# Access Web using Selenium Framework Basic

## Introduction

In this project or example, I am going to show how to navigate to website like google, or amazon without password.

I will show using many different way to achieve it like with normal way, adding function, or class for more cleaner code.
**Note** This project will not contain any releate to account, I will show access to account like Instagram or Facebook in other project in future.

I just want to keep the note about using different way of writting selenium.
There are many people using many various method of writting selenium automation cause I see many different way throughout learning selenium myself.

I will show using selenium with two website, one is `google` one is `amazon`. I will also show how to use pytest to validate whether your search result is correct or not.

I will cover navigate to URL using:

- various way of using browser driver
- various way of wait method, like `sleep`, `implicit`, `explict` wait
- using cleaning code like function, or class
- pytest method to test it

### Install Library and How to run

> Install selenium, `request`, `beautifulsoup4`, and `pytest`:
>
> > `pip install selenium requests beautifulsoup4 pytest`

### File Description

- Ex1: Navigate to google search engine:
  - `access_google_basic.py`: with basic code
  - `access_google_function.py`: add the code into function
- Ex2: Navigate to amazon page search product
  - `access_amazonSearch_Basic.py`: with basic code
  - `access_amazonSearch_Function.py`: add code into function
- Test Amazon Site and check match result
  - `test_amazonSearch_Class.py`: Test the code and validate search string
  - `test_amazonSearch_Parametrize.py`: Test the code and validate search string with parametrize on multiply search keyword

### Keypoint on the code for Selenium

#### 1. Define webdriver and Option setting

You can use either method to initializing a Selenium WebDriver instance for the Chrome browser

- using default system chrome driver

```
from selenium.webdriver import Chrome
driver=Chrome()
url="https://www.amazon.com"
driver.get(url)
```

- assign your chrome driver path
  You need to first [download chrome driver](https://developer.chrome.com/docs/chromedriver/downloads) and assign the path like below

```
from selenium import webdriver
#assign full path
driver = webdriver.Chrome("chrome full path ")
#if driver same directory can leave full path as empty
#driver = webdriver.Chrome()
url="https://www.google.com"
driver.get(url)
```

I believe there are many more way to intalize, but i think these two method is most commonly been use.

##### Option

If you are interesting of using option, you can use like this:

```
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

# let browser will not close
chrome_options.add_experimental_option("detach", True)
driver=Chrome(options=chrome_options)
driver=Chrome()
```

These are common use option, you can use as below. Please keep in mind if you want to use my setting on `driver` variable, then you need to change `driver=Chrome(options=chrome_options)`. Below is the offical site syntax:

```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()# or
#Opens Chrome in maximized mode:
options.add_argument("--start-maximized")

#set Chrome screen specfic size
options.add_argument("--window-size=1920,1080")

#Runs Chrome in headless mode (without a graphical interface):
options.add_argument("--headless")

# Opens Chrome in incognito mode
options.add_argument("--incognito"):

```

#### 2. waiting method

From above you can access a URL, if you don't add the waiting option, then your window will automatic been close. You need to let it wait for specfic second depend on your system. I will show you differnt way you can use the waiting option and choose which one you perfer.

##### sleep

This is not the best approach, basically it just doing pause which need to wait for specific time or static time. For example your web is open already, but you set to` sleep(10)`, this mean even the URL is open still have to wait for 10 second to do next step. It will just waste your time or your code might run longer if you use other waiting method.

```
import time
driver.get(url)
time.sleep(10)
```

##### Implicity

```
import time
driver.get(url)
driver.implicitly_wait(10)
```

##### Explicit wait

Using Explicit, is much better than sleep, because once your element is been find, it will start to run the next process and not wait till the max time. Below is an example of how to use explicit wait, you need to import the module first.

```
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)  # Set a timeout of 10 seconds
wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys('dress', Keys.ENTER)
```

#### 3. Find and Locate elements

When access to web you we use mouse select or locate on specific target on web. So you need to located the element by finding the element, which is like select on html tag like `class`, `id`, `xpath` or etc.

##### 3.1 Locate element by Xpath:

> There are `relative path` and `absolute path`
>
> > Relative Xpath: use often, which is much flexible
> > Absolute Xpath: use when you know the page structure will not change, then you can change. If not next time will not be able to find

```
# Relative XPath
driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text

# Absolute Path
driver.find_element(
        By.XPATH,
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea"
         )
```

##### 3.2 Locate element by id or class:

You can also use the id or class to locate the element, just like below example:

> locate element by ID:
>
> > `driver.find_element(By.ID,'twotabsearchtextbox')`

#### 4. send key or type string

continue from above since we can click on specific button or location on the web, we can also type in string or send specific key or keyboard.

Once you have locate correct element using above method, now you can type some word by sending key like:

```
#type youtube on google search bar
search_text="Youtube"
search_bar.send_keys(search_text)

#press enter by key to search
search_bar.send_keys(Keys.ENTER)
time.sleep(10)

```

#### 5. close driver

after finish access to url, you need to close your driver. You can use either of these.

- `driver.close()`: Use when you want to close a specific window but keep the WebDriver session alive (for example, when handling multiple windows).
- `driver.quit()`: Use when you're finished with all your tests and want to completely terminate the browser session.

### Pytest item

In the pytest I will change it to class, and move the function inside. All of the function will be name as test_XXX as unit test.

```
# Locate the search product element
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

type in dress
search_box.send_keys('dress', Keys.ENTER)

except_txt='"dress"'
#compare the except_txt with the URL and validate
actual_txt=self.driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
        assert except_txt == actual_txt, f"Error . Expected text: {except_txt}, but actual text: {actual_txt}"
```

In this example you are searching on amazon page on specfic product, in my example is `dress`, but if you want to search multiply product, then you need to create multiple function or unittest, and add change `except_txt="item name"` to a different product name.

This is not a good approach, you will have duplicate code and code will be longer. To solve this solution you just have to add `parametrize` like below:

```
class Testamazonsearch:
    def setup_method(self):
      search_word= ('dress','shoes')
      ....
      ....
    @pytest.mark.parametrize('searching',search_word)
    def test_amazon_searching(self, searching):
      ....
      search_box.send_keys(searching, Keys.ENTER)
      except_txt=f'\"{searching}\"'  #ignore quote
      ....
      ...

```

## update

- 2024.8.1: intial added
