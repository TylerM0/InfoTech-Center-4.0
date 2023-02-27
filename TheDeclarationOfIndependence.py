# Programmer: Tyler Mattson
# Date: 2.8.2023
# Program: Weather System Updates

#Import Libraries here
import random

#Create weather conditions in a list and choose it randomly
def weather():
	weatherForcast = ["Snowing", "Blizzard", "Rain", "Foggy", "Wind", "Icy", "Sunshine"]
	weatherCondition = random.choice(weatherForcast)
	return weatherCondition

# Variable to call weather() once in our VRS()
weatherAlert = weather()



# VRS() to respond to the weather condition
def vehicleResponseSystem():
	if weatherAlert == "Snowing":
		print("\nNWS has changed your Alarm by 15 minutes because of the weather forecast of",weatherAlert)
		print("VRS has been engaged only allowing your vehicle to go 45 MPH")
	elif weatherAlert == "Blizzard":
		print("\nNWS has changed your Alarm by 30 minutes because of the weather forecast of",weatherAlert)
		print("VRS has been engaged only allowing your vehicle to go 35 MPH")
	elif weatherAlert == "Rain":
		print("\nNWS is calling for",weatherAlert,",please drive extra carefully.")
	elif weatherAlert == "Foggy":
		print("\nNWS is calling for",weatherAlert,"conditions, please drive extra carefully.")
	elif weatherAlert == "Windy":
		print("\nNWS is calling for",weatherAlert,"conditions, please drive extra carefully.")
	elif weatherAlert == "Icy":
		print("\nNWS has changed your Alarm by 50 minutes because of the weather forecast of",weatherAlert)
		print("VRS has been engaged only allowing your vehicle to go 25 MPH")
	else:
		print("\nNWS is calling for",weatherAlert," drive safely and have a fantastic day!")

vehicleResponseSystem()






# temp
"""
edit a bit
def weatherTemp():
    tempHot = round(random.uniform(50, 100))
    tempCold = round(random.uniform(10, 40))
    if weather == "Heavy Snow":
        print("\nIt is",tempCold,"degrees outside")

    elif weather == "Blizzard":
        print("\nIt is",tempCold,"degrees outside")

    elif weather == "Raining":
        print("\nIt is",tempCold,"degrees outside")
    elif weather == "Sunny":
        print("\nIt is",tempHot,"degrees outside. "
                                "A/C is ON")

    elif weather == "Partly Cloudy":
        print("\nIt is",tempHot,"degrees outside.")

    elif weather == "Sleet":
        print("\nIt is",tempCold,"degrees outside. "
                                 "Heat is ON")


    else:
        print("\nIt is",tempHot,"degrees outside")

"""
