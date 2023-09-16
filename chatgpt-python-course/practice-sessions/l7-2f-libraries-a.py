import random
import requests

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print("Random number:", random_number)

# Make an HTTP GET request to a website
response = requests.get("https://www.joyjunction.co.uk")

# Print the content of the response
print("Response content:")
print(response.text)