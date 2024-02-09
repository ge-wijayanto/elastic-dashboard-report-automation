# import pyperclip
import webbrowser
import pywhatkit as kit
import time
import sys

import assetArray

# Phone Number/Random WhatsApp Generated ID for target recipient
# For Individual recipient, a phone number can be used for <target value>
# For WA Group recipient, the random invitation ID (Found in group invitation links) can be used for <target value>
recipient_number = "<target value>" # Change <target value> accordingly
i = 0

def sendWA():
    # Web Browser to send report, can be changed to preferred browser
    # Below is a sample for Microsoft Edge browser
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
    # Core Send Loop
    for i in range(len(assetArray.image_paths)):
        # pyperclip.copy(assetArray.caption[i])
        # time.sleep(5) # Ensure caption copied completely
        webbrowser.open(kit.sendwhats_image(recipient_number, assetArray.image_paths[i], assetArray.caption[i]), 'edge')
        time.sleep(20) # Ensure image sent completely

        i += 1

sendWA()

sys.exit()