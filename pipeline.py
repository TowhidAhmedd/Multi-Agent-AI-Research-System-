

from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain
import time

# ─────────────────────────────
# SAFE UTILS (IMPORTANT)
# ─────────────────────────────
def safe_trim(text, max_chars=1500):
    if not text:
        return ""
    return text[:max_chars]


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
        "input": f"Find recent, reliable information about: {topic}"
    })

    # 🔥 FIX: limit tokens
    search_result = str(search_result)
    search_result = safe_trim(search_result, 1500)

    state["search_results"] = search_result

    print("\nSearch result:\n", state["search_results"])

    time.sleep(0.5)  # small throttle (Groq safety)

    # =========================
    # STEP 2 - READER AGENT
    # =========================
    print("\n" + "=" * 50)
    print("STEP 2 - Reader agent scraping...")
    print("=" * 50)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "input": (
            "Extract ONE most relevant URL and summarize content briefly.\n\n"
            f"{state['search_results']}"
        )
    })

    # 🔥 FIX: limit tokens
    reader_result = str(reader_result)
    reader_result = safe_trim(reader_result, 2000)

    state["scraped_content"] = reader_result

    print("\nScraped content:\n", state["scraped_content"])

    time.sleep(0.5)

    # =========================
    # STEP 3 - WRITER (MAIN LLM)
    # =========================
    print("\n" + "=" * 50)
    print("STEP 3 - Writer generating report...")
    print("=" * 50)

    research_combined = safe_trim(
        f"SEARCH:\n{state['search_results']}\n\n"
        f"CONTENT:\n{state['scraped_content']}",
        2500  # 🔥 IMPORTANT LIMIT
    )

    report = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    report = str(report)
    report = safe_trim(report, 2000)

    state["report"] = report

    print("\nFinal Report:\n", state["report"])

    time.sleep(0.5)

    # =========================
    # STEP 4 - CRITIC (LIGHTWEIGHT)
    # =========================
    print("\n" + "=" * 50)
    print("STEP 4 - Critic reviewing...")
    print("=" * 50)

    critic_input = safe_trim(state["report"], 2000)

    feedback = critic_chain.invoke({
        "report": critic_input
    })

    feedback = str(feedback)
    feedback = safe_trim(feedback, 1000)

    state["feedback"] = feedback

    print("\nCritic feedback:\n", state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("\nEnter a research topic: ")
    result = run_research_pipeline(topic)
    print("\n\nPIPELINE COMPLETE")



# from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# def run_research_pipeline(topic: str) -> dict:

#     state = {}

#     # =========================
#     # STEP 1 - SEARCH AGENT
#     # =========================
#     print("\n" + "=" * 50)
#     print("STEP 1 - Search agent working...")
#     print("=" * 50)

#     search_agent = build_search_agent()

#     search_result = search_agent.invoke({
#         "input": f"Find recent, reliable and detailed information about: {topic}"
#     })

#     # state["search_results"] = search_result
#     state["search_results"] = search_result[:1500]

#     print("\nSearch result:\n", state["search_results"])

#     # =========================
#     # STEP 2 - READER AGENT
#     # =========================
#     print("\n" + "=" * 50)
#     print("STEP 2 - Reader agent scraping...")
#     print("=" * 50)

#     reader_agent = build_reader_agent()

#     reader_result = reader_agent.invoke({
#         "input": (
#             f"From the search results below, extract the most relevant URL "
#             f"and scrape full content.\n\n"
#             f"{state['search_results'][:1000]}"
#         )
#     })

#     # state["scraped_content"] = reader_result
#     state["scraped_content"] = reader_result[:2000]

#     print("\nScraped content:\n", state["scraped_content"])

#     # =========================
#     # STEP 3 - WRITER
#     # =========================
#     print("\n" + "=" * 50)
#     print("STEP 3 - Writer generating report...")
#     print("=" * 50)

#     research_combined = (
#         f"SEARCH RESULTS:\n{state['search_results']}\n\n"
#         f"SCRAPED CONTENT:\n{state['scraped_content']}"
#     )

#     state["report"] = writer_chain.invoke({
#         "topic": topic,
#         "research": research_combined
#     })

#     print("\nFinal Report:\n", state["report"])

#     # =========================
#     # STEP 4 - CRITIC
#     # =========================
#     print("\n" + "=" * 50)
#     print("STEP 4 - Critic reviewing...")
#     print("=" * 50)

#     state["feedback"] = critic_chain.invoke({
#         "report": state["report"]
#     })

#     print("\nCritic feedback:\n", state["feedback"])

#     return state


# if __name__ == "__main__":
#     topic = input("\nEnter a research topic: ")
#     run_research_pipeline(topic)




