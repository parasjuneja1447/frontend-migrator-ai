# app/main.py
from fastapi import FastAPI
from app.agents.reader import read_page
from app.agents.parser import parse_html
from app.agents.analyzer import analyze_sections
from app.utils.removeDuplicates import remove_duplicates

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Migration Agent Running 🚀"}

@app.get("/analyze")
async def analyze(url: str):
    html = await read_page(url)
    sections = parse_html(html)
    components = analyze_sections(sections)

    return {
        "sections": sections,
        "components": remove_duplicates(components)
    }