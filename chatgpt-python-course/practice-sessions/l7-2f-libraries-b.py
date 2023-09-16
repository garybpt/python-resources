import requests
from bs4 import BeautifulSoup

# Make an HTTP GET request to a website
response = requests.get("https://www.joyjunction.co.uk")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print the page title
page_title = soup.title.string
print("Page Title:", page_title)

# Extract and print the body text
body = soup.body.get_text("|")  # Use "|" as a separator for readability
print("Body Text:")
print(body)