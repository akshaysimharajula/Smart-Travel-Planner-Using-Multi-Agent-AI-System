from agents import call_llm

def itinerary_agent(destination, days):
    return call_llm(
        system_prompt="You are a professional travel itinerary planner.",
        user_prompt=f"""
Create a {days}-day detailed itinerary for {destination}.
Include attractions and activities.
""",
        max_tokens=900
    )