# app/agents/parser.py
from bs4 import BeautifulSoup

def parse_html(html: str):
    soup = BeautifulSoup(html, "html.parser")

    sections = []

    for div in soup.find_all("div"):
        text = div.get_text(strip=True)

        if text and len(text) > 50:
            sections.append({
                "type": "unknown",
                "content": text[:200]
            })

    return sections[:10]  # limit for MVP