YES = "Yes"
NO = "No"

weather = input("Is it currently raining? ")

if weather == YES:
    umbrella = input("Do you have an umbrella? ")
    if umbrella == YES:
        print("Go outside")
    elif umbrella == NO:
        print("Wait inside a while")
    else:
        print("Invalid response")

elif weather == NO:
    print("Go outside")

else:
    print("Invalid response")