# Programmer: Tyler Mattson
# Date: 1.20.2023
# Program: Infotech Center Upgrades

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

#Import Libraries Here
import time
import sys

print('\n\033[3;30;36m Welcome - InfoTechCenter 4.0')

x = 0
a = 0

time.sleep(2)
print('')

while x != 20:
    x += 1
    b = ("\033[3;30;36m Infotech Center 4.0 OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b)
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\n\n\033[3;31;36m Mission Accomplished - Retina Scanned - Access Granted!')
timeToSleep = 2

