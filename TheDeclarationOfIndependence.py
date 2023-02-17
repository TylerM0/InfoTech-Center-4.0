# Programmer: Tyler Mattson
# Date: 1.20.2023
# Program: Infotech Center Upgrades

#Import Libraries Here
import random

"""

Create a Function to tell the time based on where the sun is
- Create a list of where the sun is
- Randomly choose a position of the sun

I will create a Function that will tell us what time it is based on where the sun is in the sky
- Choose a time that is right for the sun

Create a Function to 
- Print where the sun is and what time it is based on the sun

"""



# List of where the sun is in the sky
def listOfSunPositions():
    sunPositions = ["6am", "9am", "12pm", "3pm", "6pm"]
    sunPositionsInTheSky = random.choice(sunPositions)
    return sunPositionsInTheSky



# Variable to call listOfSunPositions
timeIndicator = listOfSunPositions()


# Determine the approximate time based on where the sun is in the sky
def timeSun():
    if timeIndicator == "6am":
        print("The sun is east and on the horizon so it is 6am.")
    elif timeIndicator == "9am":
        print("The sun is 45 degrees up from the horizon in the east so it is 9am.")
    elif timeIndicator == "12pm":
        print("The sun is above your head so it is 12pm.")
    elif timeIndicator == "3pm":
        print("The sun is 45 degrees above the horizon in the west so it is 3pm.")
    elif timeIndicator == "6pm":
        print("The sun is west and on the horizon so it is 6pm.")


timeSun()


"""
Create a function to tell us the closest place to get snacks.
- Randomize snacks and randomize store
"""
def snacks():
    snacksList = ["Oreos","Cookies","Popcorn","Potato Chips","Pop-Tarts","Chocolate"]
    currentSnacksList = random.choice(snacksList)
    return currentSnacksList


snacksIndicator = snacks()


def listOfStores():
   stores = ["Walmart","Costco","Target","SUPERVALU","7-11","Dollar Tree","Meijer","Dollar General"]
   storesNear = random.choice(stores)
   return storesNear

def snackks():
    if snacksIndicator == "Oreos":
        print("\nI see that you would like Oreos and I also see that the closest store to you is", listOfStores())
    elif snacksIndicator == "Cookies":
        print("\nIf you would like some cookies then I would recommend that you should go to", listOfStores())
    elif snacksIndicator == "Popcorn":
        print("\nThe closest place to you to get popcorn is", listOfStores())
    elif snacksIndicator == "Potato Chips":
        print("\nThe best place to get potato chips that is near you is", listOfStores())
    elif snacksIndicator == "Pop-Tarts":
        print("\nThe closest place to get pop-tarts is", listOfStores())
    else:
        print("\nI see you would like some chocolate so you should head to", listOfStores())


if timeIndicator == "12pm":
    print(snackks())
elif timeIndicator == "3pm":
    print(snackks())
elif timeIndicator == "9am":
    print("\nSince it is 9am, you shouldn't be getting any snacks until later in the day.")
elif timeIndicator == "6am":
    print("\nSince it is 6am you shouldn't be getting any snacks.")
else:
    print("\nSince it is 6pm, it would be too late to have any types of snacks.")












