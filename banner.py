import time
import subprocess
from colorama import Style, Fore, Back

def graphics():
    print()
    print(rf'{Fore.CYAN} _______ ______  ______  _______ {Style.RESET_ALL}')
    print(rf'{Fore.CYAN}(_______|______)(_____ \(_______){Style.RESET_ALL}')
    print(rf'{Fore.CYAN} _____   _     _ _____) )_______ {Style.RESET_ALL}')
    print(rf'{Fore.CYAN}|  ___) | |   | |  __  /|  ___  |{Style.RESET_ALL}')
    print(rf'{Fore.CYAN}| |_____| |__/ /| |  \ \| |   | | {Style.RESET_ALL}')
    print(rf'{Fore.CYAN}|_______)_____/ |_|   |_|_|   |_|{Style.RESET_ALL}')
    print(rf'{Fore.CYAN}┏┓┓    •   ┳┓   ┓ ┓        ┓  ┳┓           ┏┓           •    {Style.RESET_ALL}')
    print(rf'{Fore.CYAN}┣ ┃┏┓┏╋┓┏  ┃┃┏┓┏┣┓┣┓┏┓┏┓┏┓┏┫  ┣┫┏┓┏┓┏┓┏┓╋  ┣┫┓┏╋┏┓┏┳┓┏┓╋┓┏┓┏┓{Style.RESET_ALL}')
    print(rf'{Fore.CYAN}┗┛┗┗┻┛┗┗┗  ┻┛┗┻┛┛┗┗┛┗┛┗┻┛ ┗┻  ┛┗┗ ┣┛┗┛┛ ┗  ┛┗┗┻┗┗┛┛┗┗┗┻┗┗┗┛┛┗{Style.RESET_ALL}')
    print(rf'{Fore.CYAN}                                  ┛                          {Style.RESET_ALL}')
    print()
                                                                                        
def banner():
    subprocess.call('cls', shell=True)
    graphics()
    time.sleep(1.5)

banner()