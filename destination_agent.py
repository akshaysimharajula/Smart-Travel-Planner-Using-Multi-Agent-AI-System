from agents import call_llm

def destination_agent(preferences):
    return call_llm(
        system_prompt="You are a travel destination expert.",
        user_prompt=f"""
Suggest 3 travel destinations based on:
{preferences}
Give short reasons.
"""
    )