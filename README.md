# hourly-automation

This repository contains a code that is used to automate Hourly Reporting for Bank Raya monitoring process. Created to slimline and simplify the execution of the redundant task so the analysts can focus on other important/urgent stuffs.

## Features
* Screen Capturer for all 12 Report Dashboards
* Saving the captured pictures to a folder
* Sending the pictures to the recepient WhatsApp, with their designated captions
* Delete the files in the folder to minimize storage space usage after execution

## Prerequsites
1. Install Python (3.9+)
2. Install Selenium (4.11.2+)
3. Install pywhatkit

## Installation
```sh
git clone https://github.com/ge-wijayanto/hourly-automation
pip install selenium pywhatkit
cd hourly-automation
```

## Manual Usage
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

## To-Do
|                         Task                              | Progress |
| --------------------------------------------------------- | -------- |
| Manually test the program in an actual reporting process  | ON-GOING |
| Add automation task to Task Scheduler                     | PENDING  |
| Refactor code for optimization (if necessary)             |          |