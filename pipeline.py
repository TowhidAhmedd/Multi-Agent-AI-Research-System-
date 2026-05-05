
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:

    state = {}

    # =========================
    # STEP 1 - SEARCH AGENT
    # =========================
    print("\n" + "=" * 50)
    print("STEP 1 - Search agent working...")
    print("=" * 50)

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "input": f"Find recent, reliable and detailed information about: {topic}"
    })

    state["search_results"] = search_result

    print("\nSearch result:\n", state["search_results"])

    # =========================
    # STEP 2 - READER AGENT
    # =========================
    print("\n" + "=" * 50)
    print("STEP 2 - Reader agent scraping...")
    print("=" * 50)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "input": (
            f"From the search results below, extract the most relevant URL "
            f"and scrape full content.\n\n"
            f"{state['search_results'][:1000]}"
        )
    })

    state["scraped_content"] = reader_result

    print("\nScraped content:\n", state["scraped_content"])

    # =========================
    # STEP 3 - WRITER
    # =========================
    print("\n" + "=" * 50)
    print("STEP 3 - Writer generating report...")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"SCRAPED CONTENT:\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\nFinal Report:\n", state["report"])

    # =========================
    # STEP 4 - CRITIC
    # =========================
    print("\n" + "=" * 50)
    print("STEP 4 - Critic reviewing...")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nCritic feedback:\n", state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("\nEnter a research topic: ")
    run_research_pipeline(topic)



# from agents import build_reader_agent , build_search_agent , writer_chain , critic_chain

# def run_research_pipeline(topic : str) -> dict:

#     state = {}

#     #search agent working 
#     print("\n"+" ="*50)
#     print("step 1 - search agent is working ...")
#     print("="*50)

#     search_agent = build_search_agent()
#     search_result = search_agent.invoke({
#         "messages" : [("user", f"Find recent, reliable and detailed information about: {topic}")]
#     })
#     state["search_results"] = search_result['messages'][-1].content

#     print("\n search result ",state['search_results'])

#     #step 2 - reader agent 
#     print("\n"+" ="*50)
#     print("step 2 - Reader agent is scraping top resources ...")
#     print("="*50)

#     reader_agent = build_reader_agent()
#     reader_result = reader_agent.invoke({
#         "messages": [("user",
#             f"Based on the following search results about '{topic}', "
#             f"pick the most relevant URL and scrape it for deeper content.\n\n"
#             # f"Search Results:\n{state['search_results'][:800]}"
#             f"Search Results:\n{state['search_results'][:200]}"
#         )]
#     })

#     state['scraped_content'] = reader_result['messages'][-1].content

#     print("\nscraped content: \n", state['scraped_content'])

#     #step 3 - writer chain 

#     print("\n"+" ="*50)
#     print("step 3 - Writer is drafting the report ...")
#     print("="*50)

#     research_combined = (
#         f"SEARCH RESULTS : \n {state['search_results']} \n\n"
#         f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
#     )

#     state["report"] = writer_chain.invoke({
#         "topic" : topic,
#         "research" : research_combined
#     })

#     print("\n Final Report\n",state['report'])

#     #critic report 

#     print("\n"+" ="*50)
#     print("step 4 - critic is reviewing the report ")
#     print("="*50)

#     state["feedback"] = critic_chain.invoke({
#         "report":state['report']
#     })

#     print("\n critic report \n", state['feedback'])

#     return state



# if __name__ == "__main__":
#     topic = input("\n Enter a research topic : ")
#     run_research_pipeline(topic)

