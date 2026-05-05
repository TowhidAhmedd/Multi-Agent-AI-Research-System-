
from langchain.agents import initialize_agent, AgentType
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from tools import web_search, scrape_url
from dotenv import load_dotenv
import os

load_dotenv()

# LLM (Groq)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# 🔥 Search Agent
def build_search_agent():
    return initialize_agent(
        tools=[web_search],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

# 🔥 Reader Agent
def build_reader_agent():
    return initialize_agent(
        tools=[scrape_url],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

# Writer Chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report.

Topic: {topic}

Research:
{research}

Format:
- Introduction
- Key Findings (min 3)
- Conclusion
- Sources
"""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic Chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict research critic."),
    ("human", """Evaluate this report:

{report}

Format:
Score: X/10
Strengths:
- ...
Areas to Improve:
- ...
Verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()



# # from langchain.agents import create_agent
# from langchain.agents import initialize_agent, AgentType
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from tools import web_search , scrape_url 
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# import os

# load_dotenv()

# # Paid model setup 
# # llm = ChatOpenAI(model = "gpt-4o-mini",temperature=0)

# # Paid model setup 

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",  # free & fast
#     temperature=0,
#     api_key=os.getenv("GROQ_API_KEY")
# )


# #1st agent

# def build_search_agent():
#     return initialize_agent(
#         tools=[web_search],
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True
#     )

# def build_reader_agent():
#     return initialize_agent(
#         tools=[scrape_url],
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True
#     )

# # def build_search_agent():
# #     return create_agent(
# #         model = llm,
# #         tools= [web_search]
# #     )

# # #2nd agent 

# # def build_reader_agent():
# #     return create_agent(
# #         model = llm,
# #         tools = [scrape_url]
# #     )


# #writer chain 

# writer_prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
#     ("human", """Write a detailed research report on the topic below.

# Topic: {topic}

# Research Gathered:
# {research}

# Structure the report as:
# - Introduction
# - Key Findings (minimum 3 well-explained points)
# - Conclusion
# - Sources (list all URLs found in the research)

# Be detailed, factual and professional."""),
# ])

# writer_chain = writer_prompt | llm | StrOutputParser()

# #critic_chain 

# critic_prompt = ChatPromptTemplate.from_messages([
#      ("system", "You are a sharp and constructive research critic. Be honest and specific."),
#     ("human", """Review the research report below and evaluate it strictly.

# Report:
# {report}

# Respond in this exact format:

# Score: X/10

# Strengths:
# - ...
# - ...

# Areas to Improve:
# - ...
# - ...

# One line verdict:
# ..."""),
# ])

# critic_chain = critic_prompt | llm | StrOutputParser()

