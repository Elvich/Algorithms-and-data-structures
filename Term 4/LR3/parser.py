import requests
from bs4 import BeautifulSoup

def extract_paragraphs(url):
    """Извлекает список абзацев с указанного URL."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = [p.text.strip() for p in soup.find_all('p') if p.text.strip()]
        
        return paragraphs
    except Exception as e:
        return []

