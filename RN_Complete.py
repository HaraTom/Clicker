# importing OS modul and time modul
import os
import time
from Clicker_Library import *
     
# disconnect all connected devices  
os.system("adb disconnect")

# User need to enter IP of device
DeviceIP = input("Enter the DeviceIP: ")

# connect device to PC
os.system(f"adb connect {DeviceIP}")

userId = str(input("What is USER (e.g. u0_a71) of the app? (can be checked with 'adb shell top command' - please check this before you will continue this script) "))

# How many repeats the opening/closing
program_repeats = int(input("How many repeats (EPG - Detail - Player - EPG) are you expecting? "))

# How long to watch the Player
watch = int(input("How long you watch to the Player (seconds)? "))

# How many programs need to be checked
programs_back = int(input("How many programs in the past want to check? "))

# How many rails the script will check
rails = int(input("How many rails do you have in HP? "))

# How many repeats of whole cycle is needed
cycle_repeats = int(input("How many cycles of this script you want? "))

# What position is EPG in Top menu
epg_position = int(input("What position in TOP Menu is EPG? (do not count the logo) "))

# How many assets in Top menu
top_menu = int(input("How many buttons are in TOP Menu (do not count the logo) "))

# User need to enter name of file to save the memory consumtion of the app
file_name = str(input("Enter the name of the file (no spaces, no file type - e.g. .txt, .log): "))

print("Thank you! I will handle it from here. All requested data will be stored in the document provided by you for your later analysis.")
print("In the meantime, enjoy your cup of coffee! :)")

os.system(RCU_MENU)
time.sleep(5)
anotherPage(cycle_repeats, top_menu, epg_position, programs_back, program_repeats, rails, file_name, userId)