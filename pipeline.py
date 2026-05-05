
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




