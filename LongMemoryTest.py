import os
import time
from Clicker_Library import *

def clicking(repeat):
    for clic in range(repeat):
        memory(file_name, userId)   # current memory?
        print("Browsing in the page")
        for page in range(6):       # 
            os.system(RCU_RIGHT_LONG) # Click x times right (simulates long press)
            time.sleep(2)
            os.system(RCU_LEFT_LONG) # Click x times left (simulates long press)
            time.sleep(2)
            os.system(RCU_DOWN)
        os.system(RCU_MENU)
        time.sleep(5)
        memory(file_name, userId)   # current memory?
        os.system(RCU_LIVETV)
        print("Watching channel for 5 minutes.")
        time.sleep(300)
        memory(file_name, userId)   # current memory?
        print("I will switch channel now.")
        time.sleep(2)
        os.system(RCU_CH_PLUS)
        print("Watching channel for another 5 minutes.")
        time.sleep(300)
        os.system(RCU_MENU)
        time.sleep(5)
        memory(file_name, userId)   # current memory?
        os.system(RCU_PREMIUM)
        print("Browsing in the page")
        time.sleep(5)
        for page in range(6):       # 
            os.system(RCU_RIGHT_LONG) # Click x times right (simulates long press)
            time.sleep(2)
            os.system(RCU_LEFT_LONG) # Click x times left (simulates long press)
            time.sleep(2)
            os.system(RCU_DOWN)
        os.system(RCU_MENU)
        time.sleep(5)
        memory(file_name, userId)   # current memory?
        print("Lets go browse in EPG now.")
        os.system(RCU_EPG)
        time.sleep(5)
        browse_in_epg()
        os.system(RCU_MENU)
        time.sleep(5)
        memory(file_name, userId)   # current memory?

# disconnect all connected devices  
os.system("adb disconnect")

# User need to enter IP of device
DeviceIP = input("Enter the DeviceIP: ")

# connect device to PC
os.system(f"adb connect {DeviceIP}")

userId = str(input("What is USER (e.g. u0_a71) of the app? (can be checked with 'adb shell top' command - please check this before you will continue this script) "))

# User need to enter name of file to save the memory consumtion of the app
file_name = str(input("Enter the name of the file (no spaces, no file type - e.g. .txt, .log): "))

# how many repeats
repeat = int(input("How many repeats of the program? One cycle is about approximately 20 minutes. "))

channel1()
time.sleep(5)
os.system(RCU_MENU)         # play channel nr.1 and return to default position in Home page
time.sleep(5)
clicking(repeat)

