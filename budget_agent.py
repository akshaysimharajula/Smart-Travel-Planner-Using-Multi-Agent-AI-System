from agents import call_llm

def budget_agent(budget, destination):
    return call_llm(
        system_prompt="You are a budget travel advisor.",
        user_prompt=f"""
Check whether {destination} is suitable for a budget of {budget} INR.
Mention affordability and travel style.
"""
    )