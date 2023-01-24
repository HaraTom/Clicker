import os
import time
from Clicker_Library import *

file_name = input(str("File name? "))
userId = input(str("userId of the app? "))
waiting = input(int("How long to write the memory (whole number in hours - min 1)? "))
repeats = (waiting*60)/5 # how many repeats

def mem(repeats, file_name, userId):
    for loop in range(repeats):
        memory(file_name, userId)
        time.sleep(300) # 5 minutes

mem(repeats, file_name, userId)
