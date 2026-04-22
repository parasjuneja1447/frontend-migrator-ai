# app/agents/reader.py
from playwright.async_api import async_playwright

async def read_page(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto(url, wait_until="domcontentloaded", timeout=60000)

        html = await page.content()
        await page.screenshot(path="page.png", full_page=True)

        await browser.close()

        return html