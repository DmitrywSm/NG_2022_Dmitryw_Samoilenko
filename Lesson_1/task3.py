from email.utils import localtime
from os import curdir
import datetime
import time
localtime = 555
CurrentTime = input("Enter required number of seconds: ")
CurrentFormat = time.strftime("day: %d\nhour: %H\nminute: %M\nSecond: %S")

print(CurrentFormat)
input("Press Enter to close the program")
exit()