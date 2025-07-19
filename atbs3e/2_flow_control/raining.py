# Had a go at the starting flowchart to recall my knowledge from a few years ago.

yes = 'Y'
no = 'N'

print('Is it raining? (Y/N)')
raining = input('Answer: ')

if raining == yes:
    print('Do you have an umbrella? (Y/N)')
    umbrella = input('Answer: ')
    if umbrella == yes:
        print('Go outside, softy!')
    else:
        print("Best stay in a while")

else:
    print('Why are you asking then?!')