import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_fintech_blog_articles(urls: list[str]) -> pd.DataFrame:
    data = []
    for url in urls:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")

        articles = soup.select("article")
        for article in articles:
            headline = article.find("h2")
            if not headline: continue
            text = article.get_text()
            if "fundador" in text.lower() or "startup" in text.lower():
                data.append({
                    "name": "Desconhecido",  # Pode usar LLM para extrair nome
                    "startup": "Desconhecido",
                    "bio": text.strip(),
                    "country": "Brasil"
                })
    return pd.DataFrame(data)
