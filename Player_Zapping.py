# script for zapping channels in the player 
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
file_name = str(input("File name? "))
hours = float(input("How long to run this script (hours)? "))
sleep = float(input("How long to watch the program between each channel switch (minutes)? "))
channels = int(input("How many channels do you have? "))
repeats = int((hours*60)/sleep) # number of repeats (channel switching) according to hours and time to switch channels

input("Go to Home Page and hit Enter.")

memory(file_name, userId)
os.system(RCU_NR1)
time.sleep(5)
zapping(repeats, channels, sleep, file_name, userId)
print("Thanks. I am already finished.")