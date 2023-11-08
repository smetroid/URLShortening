import requests
from bs4 import BeautifulSoup

url = 'https://popsci.com'  # Replace with the URL of the web page you want to scrape
output_file = 'links.txt'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)

    # Save the links to a file, one link per line
    with open(output_file, 'w') as file:
        for link in links:
            file.write(link + '\n')
else:
    print(f"Failed to fetch the page: {response.status_code}")
