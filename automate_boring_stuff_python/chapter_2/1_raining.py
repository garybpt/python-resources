# This was an experiment to see if I could create the first flow chart from chapter two

YES = "Yes"
NO = "No"

weather = input("Is it currently raining? (Yes/No): ")

if weather == YES:
    umbrella = input("Do you have a jacket? (Yes/No): ")
    if umbrella == YES:
        print("Go for your run")
    elif umbrella == NO:
        print("Wait inside a while")
    else:
        print("Invalid response")

elif weather == NO:
    print("Go for your run")

else:
    print("Invalid response")