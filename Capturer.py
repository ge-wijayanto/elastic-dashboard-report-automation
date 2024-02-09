from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Style, Fore, Back
import time

import assetArray

def getScreenCapture():
    i = 0

    print(f'Starting Hourly Automation process... {Fore.RED}DO NOT CLOSE THIS WINDOW{Style.RESET_ALL}')
    print(f'{Fore.CYAN}Initializing Session...{Style.RESET_ALL}')
    
    # Configuration for Firefox webdriver
    # Setting ignore certificate to bypass "Your connection is not private"
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless') # make browser run in background
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    # Use Firefox webdriver
    driver = webdriver.Firefox(options=options) # webdriver placed in C:\Users\%username%\AppData\Local\Programs\Python\Python39\Scripts
    
    # Delay time
    # Required to ensure webpage is completely rendered
    wait = WebDriverWait(driver, 30)

    # Establish elastic logon session, check if input name=username & password is loaded
    driver.get("https://<Elastic URL>/login") # Change <Elastic URL> accordingly
    username_field = wait.until(EC.presence_of_element_located(("name", 'username')))
    password_field = wait.until(EC.presence_of_element_located(("name", 'password')))
    
    # Enter credentials
    username_field.send_keys('<username>') # Change <username> accordingly
    password_field.send_keys('<password>') # Change <password> accordingly
    password_field.send_keys(Keys.RETURN)
    time.sleep(5) # to ensure session is fully established, add a few second before changing to another tab

    # Core Capturer Loop
    for i in range(len(assetArray.target_link)):
        print(f'Capturing {Fore.GREEN}{assetArray.caption[i]}{Style.RESET_ALL}...')
        
        # Open a new tab and switch to it
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        
        # Open target dashboards
        # Dictionary for target dashboards can be configured in "assetArray.py"
        driver.get(assetArray.target_link[i])

        # Wait until all contents are rendered, using aria-label as condition
        search_complete_locator = (By.XPATH, "//button[@aria-label='Search session complete']")
        wait.until(EC.presence_of_element_located(search_complete_locator))
        time.sleep(5) # ensure page is completely rendered

        # Set picture size for dashboard screenshot
        driver.maximize_window()
        width = driver.execute_script("return document.documentElement.scrollWidth")
        height = driver.execute_script("return Math.max( document.body.scrollHeight,document.body.offsetHeight,document.documentElement.clientHeight,document.documentElement.scrollHeight,document.documentElement.offsetHeight)")

        driver.set_window_size(width, height)

        # time.sleep(20) # to ensure page is completely rendered

        # Perform Screenshot
        screenshot_path = f"path/to/file/<filename>{i}.png" # Change File path and name accordingly
        driver.save_screenshot(screenshot_path)

        i += 1

    driver.quit()

getScreenCapture()