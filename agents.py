
from langchain.agents import initialize_agent, AgentType
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from tools import web_search, scrape_url
from dotenv import load_dotenv
import os

load_dotenv()

# ─────────────────────────────
# GROQ LLM (OPTIMIZED)
# ─────────────────────────────
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),
    # max_tokens=1024 
    max_tokens=400
)

# ─────────────────────────────
# SEARCH AGENT (LIGHTWEIGHT)
# ─────────────────────────────
def build_search_agent():
    return initialize_agent(
        tools=[web_search],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,  # 🔥 reduce token/log noise
        handle_parsing_errors=True,
        max_iterations=2  # 🔥 IMPORTANT FIX
    )

# ─────────────────────────────
# READER AGENT (LIGHTWEIGHT)
# ─────────────────────────────
def build_reader_agent():
    return initialize_agent(
        tools=[scrape_url],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True,
        max_iterations=2  # 🔥 IMPORTANT FIX
    )

# ─────────────────────────────
# WRITER (MAIN LLM)
# ─────────────────────────────
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Keep responses concise and structured."),
    ("human", """Write a research report.

Topic: {topic}

Research:
{research}

Format:
- Introduction
- Key Findings (3 points max)
- Conclusion
"""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# ─────────────────────────────
# CRITIC (LIGHTWEIGHT OUTPUT)
# ─────────────────────────────
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict research critic."),
    ("human", """Evaluate this report concisely:

{report}

Format:
Score: X/10
Strengths:
- max 2 points
Improvements:
- max 2 points
"""),
])

critic_chain = critic_prompt | llm | StrOutputParser()


# from langchain.agents import initialize_agent, AgentType
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_groq import ChatGroq
# from tools import web_search, scrape_url
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # LLM (Groq)
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0,
#     api_key=os.getenv("GROQ_API_KEY")
# )

# # 🔥 Search Agent
# def build_search_agent():
#     return initialize_agent(
#         tools=[web_search],
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True,
#         handle_parsing_errors=True
#     )

# # 🔥 Reader Agent
# def build_reader_agent():
#     return initialize_agent(
#         tools=[scrape_url],
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True,
#         handle_parsing_errors=True
#     )

# # Writer Chain
# writer_prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
#     ("human", """Write a detailed research report.

# Topic: {topic}

# Research:
# {research}

# Format:
# - Introduction
# - Key Findings (min 3)
# - Conclusion
# - Sources
# """),
# ])

# writer_chain = writer_prompt | llm | StrOutputParser()

# # Critic Chain
# critic_prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a strict research critic."),
#     ("human", """Evaluate this report:

# {report}

# Format:
# Score: X/10
# Strengths:
# - ...
# Areas to Improve:
# - ...
# Verdict:
# ..."""),
# ])

# critic_chain = critic_prompt | llm | StrOutputParser()




