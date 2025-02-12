from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

links = soup.find_all("a")
for link in links:
    #print(link)
    print(link.get('href'))