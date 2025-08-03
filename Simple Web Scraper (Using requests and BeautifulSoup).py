# web_scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    url = "https://news.ycombinator.com"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch page")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('a', class_='storylink', limit=10)

    print("Top 10 Hacker News Titles:\n")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title.get_text()}")

scrape_hacker_news()
