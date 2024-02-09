from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import pyperclip

import assetArray
from colorama import Style, Fore, Back

# Initialize the Chrome profile
# profile = webdriver.FirefoxProfile(firefox_profile_path)
options = webdriver.ChromeOptions()
# options.profile = firefox_profile_path
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument(r"user-data-dir=C:\Users\<Username>\AppData\Local\Google\Chrome\User Data") # Change <Username> accordingly
options.add_argument('--headless=new') # make browser run in background

# Initialize the Chrome webdriver with the profile
driver = webdriver.Chrome(options=options)

# # ****************************************************
# # Initialize the Firefox profile
# # profile = webdriver.FirefoxProfile(firefox_profile_path)
# options = webdriver.FirefoxOptions()
# # options.profile = firefox_profile_path
# options.add_argument('--headless') # make browser run in background
# options.add_argument('--ignore-ssl-errors=yes')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('-profile')
# options.add_argument(r"C:\Users\<Username>\AppData\Roaming\Mozilla\Firefox\Profiles\uze728cx.default-release")
# # Initialize the Chrome webdriver with the profile
# driver = webdriver.Firefox(options=options)
# # ************************************************

print()
print(f'Starting {Fore.CYAN}Sending to WhatsApp{Style.RESET_ALL} process...')

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/accept?code=<GroupID/PhoneNumber>') # Change <GroupID/PhoneNumber> accordingly 
# driver.get('https://web.whatsapp.com')
time.sleep(30)  # Wait for the page to load fully

# Locate the chat input field using a different approach (XPath)
chat_input = driver.find_element('xpath', '//div[@contenteditable="true"]')

i = 0

# Loop through the captions and send them to the "Test Script" group
for i in range(len(assetArray.image_paths)):
    caption = assetArray.caption[i]
    print(f'Sending {Fore.GREEN}{caption}{Style.RESET_ALL}...')

    time.sleep(5)

    # Send the caption
    # chat_input = driver.find_element('css selector', 'div.selectable-text.copyable-text.iq0m558w.g0rxnol2')
    wait = WebDriverWait(driver, 10)
    chat_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._3Uu1_')))
    chat_input.click()
    
    chat_input.send_keys(caption)
    chat_input.send_keys(Keys.SHIFT + Keys.ENTER)
    chat_input.send_keys(assetArray.dateandtime[0])
    # time.sleep(15)
    # chat_input.send_keys(Keys.ENTER)

    # time.sleep(5)  # Wait for the caption to be sent

    # Click on the plus icon
    clip_icon = driver.find_element('css selector', 'span[data-icon="attach-menu-plus"]')  # Click on the clip icon
    action = ActionChains(driver)
    action.move_to_element(clip_icon).click().perform()
    time.sleep(5)
    
    # Click on the photos and videos option
    photos_videos_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[fill="var(--attachment-type-photos-color)"]')))
    
    # photos_videos_option.click()
    action = ActionChains(driver)
    action.move_to_element(photos_videos_option).click().perform()
    time.sleep(5)

    # Click on the upload photo and videos option
    driver.find_element('css selector', 'input[type="file"][accept="image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys(assetArray.image_paths[i])  # Upload the image
    time.sleep(5)  # Wait for the image to upload

    driver.find_element('css selector', 'span[data-icon="send"]').click()  # Click the send button

    time.sleep(15)  # Adjust the delay as needed

    i += 1

print(f'Sending process finished, initializing {Fore.YELLOW}Delete Files{Style.RESET_ALL} process...')

# Close the webdriver
driver.quit()