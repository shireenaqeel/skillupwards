import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.youtube.com/"  # Replace this with the actual URL of the website you want to scrape
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the webpage")

soup = BeautifulSoup(html_content, 'html.parser')

headlines = []
for item in soup.find_all('h2', class_='headline'):  # Replace 'h2' and 'headline' with the actual tag and class
    headlines.append(item.get_text())

# Create a DataFrame from the headlines list
df = pd.DataFrame(headlines, columns=["Headline"])

# Save the DataFrame to a CSV file
df.to_csv("headlines.csv", index=False)
