from fileinput import filename
import os
import time

# CONSTANTS:
RCU_MENU = "adb shell input keyevent 3"
RCU_BACK = "adb shell input keyevent 4"
RCU_NR1 = "adb shell input keyevent 8"
RCU_UP = "adb shell input keyevent 19"
RCU_DOWN = "adb shell input keyevent 20"
RCU_LEFT = "adb shell input keyevent 21"
RCU_RIGHT = "adb shell input keyevent 22"
RCU_OK = "adb shell input keyevent 23"
RCU_CH_PLUS = "adb shell input keyevent 166"
RCU_CH_MINUS = "adb shell input keyevent 167"
RCU_LIVETV = "adb shell input keyevent 170"
RCU_EPG = "adb shell input keyevent 172"
RCU_PREMIUM = "adb shell input keyevent 174"

RCU_LEFT_LONG = "adb shell input keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21 keyevent 21"
RCU_RIGHT_LONG = "adb shell input keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22 keyevent 22"

#-----------------------------------------------------------------------------------------------------------------------------------------------

# FUNCTIONS:

# Relevant for all
# Show me the current date, time and memory usage for specific app and her specific atributes and close after it
def memory(file_name, userId):
    os.system(f"date /t >> {file_name}.txt")
    os.system(f"time /t >> {file_name}.txt")
    os.system(f"adb shell top -n 1 -o ARGS -o RES -u {userId} -q>> {file_name}.txt")
    os.system(f"adb shell free -h >> {file_name}.txt")

# Play channel number 1 for a few seconds (to have it in the first postion) and return to Home page (default position focused)
def channel1():
    os.system(RCU_NR1)
    time.sleep(5)
    os.system(RCU_MENU)

# Focus all assets in the rail and return to the first position, go to the next rail and repeat - repeat for whole page
def pageClicker(rails, top_menu, file_name, userId):
    time.sleep(5)
    memory(file_name, userId)
    for page in range(rails):
        os.system(RCU_RIGHT_LONG) # Click x times right (simulates long press)
        time.sleep(2)
        os.system(RCU_LEFT_LONG) # Click x times left (simulates long press)
        time.sleep(2)
        os.system(RCU_DOWN)
    for up in range(rails + 1): # Focus the asset in the Top menu
        os.system(RCU_UP)
    for left in range(top_menu + 2): # Focus the first asset in the Top menu
        os.system(RCU_LEFT)
#--------

# Relevant for Player_Zapping.py:
# Zapping in the player via CH+ or CH-
def zapping(repeats, channels, sleep, file_name, userId):
    cycle = 0
    while cycle < repeats:   
        for switch in range(channels):
            if cycle >= repeats:            # Repeats until ...
                break
            time.sleep(sleep*60)            # Watch the channel x minutes
            memory(file_name, userId)       
            print("I will switch the channel up now.")              
            os.system(RCU_CH_PLUS)          # Switch channel up
            cycle += 1            
        for switch in range(channels):
            if cycle >= repeats:
                break
            time.sleep(sleep*60)            # Watch the channel x minutes
            memory(file_name, userId)
            print("I will switch the channel down now.")
            os.system(RCU_CH_MINUS)         # Switch channel down
            cycle += 1

#--------

# Relevant for EPG (Classic)
# Press RCU button 100x ↓ - 50x ← - 50x → - 50x ↓ - 150x ↑
def browse_in_epg():
    for pressing in range(75):
        os.system(RCU_DOWN)
    for pressing in range(50):
        os.system(RCU_LEFT)
    for pressing in range(50):
        os.system(RCU_RIGHT)
    for pressing in range(50):
        os.system(RCU_DOWN)
    for pressing in range(125):
        os.system(RCU_UP)

# From the default position in EPG go to the left once, open the detail, play the show, return to EPG, open the detail, close the detail - and repeat the whole cycle
def detail(programs_back, program_repeat, watch):
    browse_in_epg()
    os.system(RCU_EPG) # default focus in EPG
    time.sleep(5)
    click_left = 1
    for detail in range(programs_back):
        for cycle in range(program_repeat):
            for left in range(click_left):
                os.system(RCU_LEFT)
            os.system(RCU_OK) # should open the detail page
            time.sleep(5) # wait x seconds to load up the page
            os.system(RCU_OK) # play the show
            time.sleep(watch) # watch the show for x seconds
            os.system(RCU_EPG) # go to the EPG
            os.system(RCU_EPG) # default position in EPG
        click_left += 1
#--------

# Relevant for EPG (Vertical)
# Vertical EPG = 3 columns -> 1. Channel - 2. Date - 3. Program
# Press RCU button 10x ↑ - 20x ↓ - 10x ↑ - 1x ← (to the date column)
def loop_programs():
    for pressing in range(10):
        os.system(RCU_UP)
    for pressing in range(20):
        os.system(RCU_DOWN)
    for pressing in range(10):
        os.system(RCU_UP)
    os.system(RCU_LEFT)

# Press Up RCU button 14x and go to right (to the program column)
def date_up():
    for pressing in range(14):
        os.system(RCU_UP)
    os.system(RCU_RIGHT)

# Check assets in program column and scroll throught the date column and return to channel column
def loop_date(file_name, userId):
    for pressing in range(14):
        loop_programs()
        os.system(RCU_DOWN)
        os.system(RCU_RIGHT)
        time.sleep(5)
    os.system(RCU_LEFT)
    os.system(RCU_LEFT)
    memory(file_name, userId)

# Scroll throught all channels
def loop_channels(file_name, userId):
    for pressing in range(150):
        os.system(RCU_RIGHT)
        date_up()
        loop_date(file_name, userId)
        time.sleep(5)
        print("Lets check another channel.")
        os.system(RCU_DOWN)
        time.sleep(5)

#--------

# Relevant for Browsing in the App (without EPG - functions above)
# Move to another section and click in the section
def anotherPage(cycle_repeats, top_menu, epg_position, programs_back, program_repeats, rails, file_name, userId, watch):
    for loop in range(cycle_repeats):
        to_side = 0
        while to_side <= top_menu:
            if to_side == epg_position:
                print("Lets browse in EPG.")
                for next_page in range(to_side):
                    os.system(RCU_RIGHT)
                os.system(RCU_OK)
                time.sleep(2) # Time to loads up the page
                detail(programs_back, program_repeats, watch) # Classic EPG clicker
                time.sleep(5)
                to_side += 1
                print("I will return to the Home page now.")
                os.system(RCU_MENU) # Return to Home page - default position
                time.sleep(5)
                os.system(RCU_UP)
                time.sleep(2)
                os.system(RCU_LEFT)
            elif to_side != epg_position and to_side > 0:
                if to_side > 1:
                    print("Lets go to another page. ")
                for next_page in range(to_side):
                    os.system(RCU_RIGHT)
                os.system(RCU_OK)
                time.sleep(5)
                print("I will check another page now.")
                pageClicker(rails, top_menu, file_name, userId)
                time.sleep(5)
                os.system(RCU_UP)
                to_side += 1
            else:
                pageClicker(rails, top_menu, file_name, userId)
                to_side += 1

#--------
