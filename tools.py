
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# =========================
# WEB SEARCH TOOL
# =========================
@tool
def web_search(query: str) -> str:
    """
    Search web using Tavily and return structured results (title, url, snippet)
    """
    try:
        results = tavily.search(query=query, max_results=5)

        if not results or "results" not in results:
            return "No results found."

        out = []

        for r in results.get("results", []):
            title = r.get("title", "No title")
            url = r.get("url", "No url")
            snippet = r.get("content", "")

            out.append(
                f"TITLE: {title}\nURL: {url}\nSNIPPET: {snippet[:300]}"
            )

        return "\n\n---\n\n".join(out)

    except Exception as e:
        return f"Search failed: {str(e)}"


# =========================
# SCRAPE TOOL
# =========================
@tool
def scrape_url(url: str) -> str:
    """
    Scrape webpage and return cleaned text
    """
    try:
        resp = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(resp.text, "html.parser")

        # remove junk
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text[:3000]

    except Exception as e:
        return f"Scraping failed: {str(e)}"




