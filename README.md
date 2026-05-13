# Multi-Agent-AI-Research-System-
ResearchMind is a sophisticated, multi-agent pipeline designed to automate deep research. By orchestrating four specialized AI agents, the system transforms a simple topic into a structured, peer-reviewed research report in seconds.

Built with LangChain, powered by Groq (Llama 3.1) for lightning-fast inference, and wrapped in a modern Streamlit interface.

🚀 Key Features
Multi-Agent Orchestration: Uses a specialized pipeline where agents handle Search, Reading, Writing, and Critiquing.

Real-time Web Intelligence: Integrated with Tavily AI for high-quality, noise-free web searches.

Deep Content Extraction: Automated scraping using BeautifulSoup4 to parse and clean relevant technical data.

Automated Quality Assurance: A "Critic" agent evaluates the report, providing a score and actionable feedback.

Optimized Performance: Leverages Llama-3.1-8b-instant on Groq for sub-second response times.

Modern UI: A custom-styled Streamlit dashboard with real-time pipeline tracking and Markdown export.


Architecture & Pipeline
The system follows a linear state-managed pipeline:

Search Agent: Queries the web and retrieves the top 5 most relevant sources.

Reader Agent: Analyzes search results, selects the most pertinent URL, and scrapes its full content.

Writer Agent: Synthesizes the search data and scraped content into a structured 3-point report.

Critic Agent: Performs a final audit, scoring the report out of 10 and suggesting improvements.


Tech Stack
Category          Tools

Orchestration   	LangChain, LangChain-Core
LLM	              Groq (Llama-3.1-8b-instant)
Search API	      Tavily AI
UI/UX            	Streamlit + Custom CSS
Scraping        	BeautifulSoup4, Requests
Environment	      Python 3.9+, Dotenv




Getting Started
1. Clone the Repository
Bash
git clone https://github.com/yourusername/research-mind.git
cd research-mind
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory:

Code snippet
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
4. Run the Application
To launch the Web UI:

Bash
streamlit run app.py
To run the CLI Pipeline:

Getting Started
1. Clone the Repository
Bash
git clone https://github.com/TowhidAhmedd/Multi-Agent-AI-Research-System-
cd research-mind

3. Install Dependencies
Bash
pip install -r requirements.txt

5. Configure Environment Variables
Create a .env file in the root directory:

Code snippet
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

4. Run the Application
To launch the Web UI:

Bash
streamlit run app.py
To run the CLI Pipeline:

Bash
python pipeline.py

Bash
python pipeline.py
Project Structure
app.py: The Streamlit frontend featuring custom CSS and state management.

agents.py: Configuration for the four AI agents and their respective prompt templates.

pipeline.py: The core logic that handles data flow between agents.

tools.py: Custom LangChain tools for web searching and scraping.

requirements.txt: List of all necessary Python libraries.





