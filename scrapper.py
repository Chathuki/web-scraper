import requests
from bs4 import BeautifulSoup

def scrape_website(url):
  """Scrape a website and return the title and body text."""
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  title = soup.find("title").text
  body = soup.find("body").text
  return title, body

if __name__ == "__main__":
  url = "https://martiantobe.wixsite.com/martiantobe/blog/"
  title, body = scrape_website(url)
  print(title)
  print(body)
