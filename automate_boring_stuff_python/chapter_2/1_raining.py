YES = True
NO = False

weather = input("Is it currently raining? ")
weather = str(weather)

if weather == YES:
    umbrella = input("Do you have an umbrella? ")
    umbrella = str(umbrella)
    if umbrella == YES:
        print("Go outside")
    elif umbrella == NO:
        print("Wait inside a while")

elif weather == NO:
    print("Go outside")

else:
    print("Invalid response")