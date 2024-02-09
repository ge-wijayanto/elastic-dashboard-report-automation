# Elastic Dashboard Report Automation (EDRA)
Authors: Naufal Fransella (fransella), Gregorius Evangelist W. (ge-wijayanto)

Elastic Dashboard Report Automation (EDRA) is a script that is used to automate reporting process in an SOC Environment that is utilizing Elastic SIEM. This script is created to slimline and simplify the execution of the redundant task, in this case Elastic Dashboard reporting (such as the one that needs to be done in a specified interval), so that Security Analysts can focus on other important/urgent matters. 

## Key Features
EDRA contains the following key features: 
* Screen Capturer for Elastic Dashboards, complete with pre-defined time interval queries
* Saving captured dashboard pictures to a folder
* Sending the pictures to the recipient WhatsApp, with their each designated captions
* Delete the files in the folder to minimize storage space usage after execution

## Prerequsites
1. Install Python (3.9+)
2. Install Selenium (4.11.2+)
3. Install pywhatkit

## Installation
```sh
git clone https://github.com/ge-wijayanto/elastic-dashboard-report-automation.git
pip install selenium pywhatkit
cd hourly-automation
```

## Usage Guide
```py
Open Terminal

########## USE CASES ##########
## Run ALL Module at once
python main.py

## Run ONLY the Capturer Module
python Capturer.py

## Run ONLY the Send Module
python Send.py

## Run ONLY the Delete File Module
python deleteFile.py
```

## Configurations
Several configuration changes must be set by the users for this script to run properly. Below is a guide to make those changes.

1. Capturer.py - Change the <Elastic URL> value to the appropriate Elastic SIEM URL that is being used.
```py
# Establish elastic logon session, check if input name=username & password is loaded
driver.get("https://<Elastic URL>/login") # Change <Elastic URL> accordingly
```

2. Capturer.py - Change the <username> and <password> value, this is needed for authentication to the Elastic SIEM that is being used. 
```py
 # Enter credentials
username_field.send_keys('<username>') # Change <username> accordingly
password_field.send_keys('<password>') # Change <password> accordingly
password_field.send_keys(Keys.RETURN)
time.sleep(5) # to ensure session is fully established, add a few second before changing to another tab
```

3. Capturer.py - Change the file path to which the Dashboard screenshots will be saved. The {i} should be left as is (or changed according to operational guidelines), as it is used to mark the loop numbers.
```py
# Perform Screenshot
screenshot_path = f"path/to/file/<filename>{i}.png" # Change File name and path accordingly
driver.save_screenshot(screenshot_path)
```

4. assetArray.py - Adjust the target_link, image_paths, and caption dictionaries to user's needs. target_link is the URL from which the Elastic Dashboard will be retrieved, along with the time interval query. image_paths is used to store file names of each report. caption is used to store captions to be used when sending the report.
```py
# Target Dashboard URL 
target_link = [
    # Target Dashboard 1 - Elastic
    f"https://<Elastic Dashboard URL>?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'{getTime.time.strftime('%Y-%m-%dT%H:00:00.000Z', old_utc_time)}',to:'{getTime.time.strftime('%Y-%m-%dT%H:00:00.000Z', current_utc_time)}'))",
    # ...
]

# File Name for Each Retrieved Dashboards
image_paths = [
    # Target Dashboard 1
    "path/to/file/Report1.png",
    # ...
]

# Captions to be included in WhatsApp messages for reporting (Optional)
caption = [
    f"Report Title 1\n{synonym.synonym_of_day}, {synonym.date} {synonym.synonym_of_month} {synonym.year} {synonym.old_local_clock}:00 - {synonym.current_local_clock}:00 WIB",
    # ...
]
```

5. deleteFile.py - Change file path to the dashboard report folder.
```py
# Path to the folder containing the files to be deleted
folder_to_clean = "path/to/folder/"
```

6. getTime (OPTIONAL) - Change the time interval of dashboards to be used in the query part of the URL.
```py
# Current UTC Time - 3 Hours (Hourly Interval)
three_hours_before_utc = current_datetime_utc - datetime.timedelta(hours=3)

# Current Local Time - 3 Hours (Interval)
three_hours_before_local = current_datetime_local - datetime.timedelta(hours=3)

# Change the "hours=<int>" part for the desired time interval
```

7. Send.py - Change the designated WA recipient.
```py
# Phone Number/Random WhatsApp Generated ID for target recipient
# For Individual recipient, a phone number can be used for <GroupID/PhoneNumber>
# For WA Group recipient, the random invitation ID (Found in group invitation links) can be used for <GroupID/PhoneNumber>
# Open WhatsApp Web
driver.get('https://web.whatsapp.com/accept?code=<GroupID/PhoneNumber>') # Change <GroupID/PhoneNumber> accordingly
```

8. Send.py - Change the location of browser profiles.
```py
# Initialize the Chrome profile
# profile = webdriver.FirefoxProfile(firefox_profile_path)
options = webdriver.ChromeOptions()
# options.profile = firefox_profile_path
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument(r"user-data-dir=C:\Users\<Username>\AppData\Local\Google\Chrome\User Data") # Change <Username> accordingly
options.add_argument('--headless=new') # make browser run in background
```