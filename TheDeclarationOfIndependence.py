# Programmer: Tyler Mattson
# Date: 1.20.2023
# Program: Infotech Center Upgrades

#Import Libraries Here
import random


"""

Create a Function to
- Create a list of where the sun is
- Randomly choose a position of the sun

I will create a Function that will tell us what time it is based on where the sun is in the sky
- Choose a time that is right for the sun

Create a Function to 
- Print where the sun is and what time it is based on the sun

"""



# List of where the sun is in the sky
def listOfSunPositions():
    sunPositions = ["The sun is east and on the horizon", "The sun is 45 degrees up from the horizon in the east", "The sun is above your head", "The sun is 45 degrees above the horizon in the west", "The sun is west and on the horizon"]
    sunPositionsInTheSky = random.choice(sunPositions)
    return sunPositionsInTheSky


# Variable to call lidtOfSunPositions
timeIndicator = listOfSunPositions()




# Determine the approximate time based on where the sun is in the sky
def timeSun():
    if timeIndicator == "The sun is east and on the horizon":
        print("The sun is east and on the horizon so that would mean that your current time is approximately 6am.")
    elif timeIndicator == "The sun is 45 degrees up from the horizon in the east":
        print("The sun is 45 degrees up from the horizon in the east so that would mean that your current time is approximately 9am.")
    elif timeIndicator == "The sun is above your head":
        print("The sun is above your head so your current time is approximately 12pm.")
    elif timeIndicator == "The sun is 45 degrees above the horizon in the west":
        print("The sun is 45 degrees above the horizon in the west so your current time is approximately 3pm.")
    elif timeIndicator == "The sun is west and on the horizon":
        print("The sun is west and on the horizon so the current time is approximately 6pm.")


timeSun()


