# Multi-Agent-AI-Research-System-

<div align="center">

# 🔬 ResearchMind
### *Next-Gen Multi-Agent AI Research Pipeline*

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-Llama_3.1-orange?style=for-the-badge)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

<p align="center">
    <b>ResearchMind</b> is a sophisticated multi-agent system that automates the transition from "curiosity" to "comprehensive report." By orchestrating specialized AI agents, it delivers peer-reviewed-quality research in a matter of seconds.
</p>

[Explore Features](#-key-features) • [Architecture](#%EF%B8%8F-architecture--pipeline) • [Quick Start](#-getting-started) • [CLI Usage](#4-run-the-application)

</div>

---

## 🚀 Key Features

<table>
  <tr>
    <td width="50%">
      <h4>🤖 Multi-Agent Orchestration</h4>
      <p>Coordinated workflow between four distinct agents: <b>Search, Reader, Writer, and Critic</b>, ensuring a separation of concerns and high-quality output.</p>
    </td>
    <td width="50%">
      <h4>⚡ Extreme Inference Speed</h4>
      <p>Powered by <b>Groq's Llama-3.1-8b-instant</b> model, achieving sub-second token generation for near-instant research drafting.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h4>🌐 Real-time Web Intelligence</h4>
      <p>Deep integration with <b>Tavily AI</b> for noise-free, optimized search results specifically curated for LLM consumption.</p>
    </td>
    <td width="50%">
      <h4>🔍 Deep Content Extraction</h4>
      <p>Automated <b>BeautifulSoup4</b> scraping logic that cleans HTML, removes junk tags (nav/footer), and extracts the core knowledge base.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h4>⚖️ Automated Quality Audit</h4>
      <p>A dedicated <b>Critic Agent</b> that performs rigorous QA, scoring reports and providing actionable feedback to ensure academic-level integrity.</p>
    </td>
    <td width="50%">
      <h4>🎨 Modern UI/UX</h4>
      <p>A custom-themed <b>Streamlit</b> dashboard featuring real-time pipeline status tracking and one-click Markdown exports.</p>
    </td>
  </tr>
</table>

---

## 🏗️ Architecture & Pipeline

ResearchMind utilizes a **linear state-managed pipeline** to ensure data integrity across the research lifecycle:

1.  **Search Agent** ➔ Scans the global web via Tavily to identify high-authority sources.
2.  **Reader Agent** ➔ Evaluates links, selects the primary source, and performs deep-tissue scraping.
3.  **Writer Agent** ➔ Synthesizes raw data into a structured, concise research report.
4.  **Critic Agent** ➔ Reviews the draft, provides a 1-10 score, and highlights areas for improvement.

---

## 🛠️ Tech Stack

<div align="center">

| Component | Technology |
| :--- | :--- |
| **Framework** | LangChain / LangChain-Core |
| **LLM Engine** | Llama 3.1 (8B Instant) via Groq |
| **Search Engine** | Tavily AI |
| **Web Interface** | Streamlit + Custom CSS |
| **Parsing** | BeautifulSoup4 / LXML |
| **Environment** | Python 3.9+ / Dotenv |

</div>

---

## 🚦 Getting Started

### 1. Clone the Repository
bash
git clone https://github.com/TowhidAhmedd/Multi-Agent-AI-Research-System-
cd research-mind

2. Install Dependencies
Bash
pip install -r requirements.txt

3. Configuration
Create a .env file in the root directory and add your API keys:

Ini, TOML
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here



Usage
Launch the Web Experience
The Streamlit UI provides a visual tracker for the agent pipeline.

Bash
streamlit run app.py
Run the CLI Pipeline
Perfect for quick, terminal-based research tasks.

Bash
python pipeline.py
Project Structure
Plaintext
├── app.py              # Streamlit frontend with custom CSS & state handling
├── agents.py           # Logic for Agent initialization & Prompt Templates
├── pipeline.py         # Sequential execution logic & token management
├── tools.py            # Tavily Search & BeautifulSoup Scraping tools
├── requirements.txt    # Project dependencies
└── .env                # (Local only) API Key storage







