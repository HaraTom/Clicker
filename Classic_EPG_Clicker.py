# Clicking through the EPG
# importing OS modul and time modul
import os
import time
from Clicker_Library import *

os.system("adb disconnect")
# User need to enter IP of device
DeviceIP = input("Enter the DeviceIP: ")

# connect device to PC
os.system(f"adb connect {DeviceIP}")

# how many repeats the opening/closing
program_repeat = int(input("How many repeats (EPG - Detail - Player - EPG) are you expecting? "))

# How many programs need to be checked
programs_back = int(input("How many programs in the past want to check? "))

# User need to enter name of file
file_name = str(input("Enter the name of the file (no spaces, no file type - e.g. .txt, .log): "))

print("Thank you! I will handle it from here. All requested data will be stored in the document provided by you for your later analysis.")
print("In the meantime, enjoy your cup of coffee! :)")

channel1()
os.system(RCU_EPG)
browse_in_epg()
detail(programs_back, program_repeat)
