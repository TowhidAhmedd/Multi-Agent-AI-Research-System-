# Multi-Agent AI Research System

A professional AI research platform built with Python, LangChain, Groq, and Streamlit.

This repository contains a multi-agent pipeline that performs web search, content scraping, structured research writing, and report critique. It is designed to demonstrate an end-to-end AI research assistant for generating high-quality research briefs from live web data.

## Key Features

- **Search Agent**: Finds relevant web content using the Tavily search API.
- **Reader Agent**: Scrapes and extracts text from web pages with BeautifulSoup.
- **Writer Chain**: Produces a structured research report using a language model prompt.
- **Critic Chain**: Reviews and scores the generated report for quality improvements.
- **Streamlit UI**: A modern web interface for exploring the research pipeline.

## Project Structure

- `app.py` - Streamlit application shell with custom UI styling and user interface components.
- `agents.py` - Agent builders and chained prompt workflows for search, reading, writing, and critique.
- `pipeline.py` - End-to-end CLI pipeline that executes the research workflow for a given topic.
- `tools.py` - Custom tool implementations for web search and URL scraping.
- `requirements.txt` - Python package dependencies for LangChain, Groq, Tavily, Streamlit, and web scraping.

## Technologies Used

- Python
- LangChain
- Groq (`langchain-groq`) for LLM interaction
- Tavily search API for web results
- BeautifulSoup for HTML content extraction
- Streamlit for the user interface
- dotenv for environment configuration

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

### Streamlit UI

Run the app with:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

### CLI Pipeline

Run the pipeline directly for a research topic:

```bash
python pipeline.py
```

Enter a topic when prompted to execute the full research workflow.

## How It Works

1. `pipeline.py` uses `build_search_agent()` to gather relevant web search results.
2. `build_reader_agent()` scrapes the selected web resource for detailed content.
3. The writer chain formats the aggregated research into a structured report.
4. The critic chain evaluates the report, returning scores and improvement advice.

## Notes

- Ensure both `GROQ_API_KEY` and `TAVILY_API_KEY` are available in the environment before running the app.
- The system currently limits scraped text to the first 3000 characters for safety and speed.
- The project is intended as a professional research assistant showcase for AI-driven multi-agent workflows.

## Future Enhancements

- Add advanced agent orchestration and tool selection.
- Improve source citation extraction and report provenance.
- Add support for multi-topic research sessions and report export.
- Add unit tests and automated evaluation.
