import streamlit as st
from destination_agent import destination_agent
from budget_agent import budget_agent
from itinerary_agent import itinerary_agent
from weather_agent import weather_agent

st.set_page_config(page_title="Smart Travel Planner", layout="wide")

st.title("🌍 Smart Travel Planner (Multi-Agent AI)")
st.write("AI-powered travel planning using specialized agents")

# Sidebar inputs
with st.sidebar:
    travel_type = st.selectbox(
        "Travel Type",
        ["Adventure", "Relaxation", "Cultural", "Nature"]
    )
    budget = st.number_input("Budget (INR)", min_value=5000, step=5000)
    days = st.slider("Trip Duration (Days)", 1, 10, 3)
    city = st.text_input("Preferred City / Country")
    plan_btn = st.button("Generate Travel Plan")

# Main inputs
destination = st.text_input("Choose one destination from suggestions")
details_btn = st.button("Generate Trip Details")

# Destination agent
if plan_btn:
    preferences = f"""
Travel Type: {travel_type}
Preferred Location: {city}
Budget: {budget}
Duration: {days} days
"""
    with st.spinner("🤖 Destination Agent working..."):
        st.subheader("📍 Suggested Destinations")
        st.write(destination_agent(preferences))

# Other agents
if details_btn and destination:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💸 Budget Analysis")
        st.write(budget_agent(budget, destination))

    with col2:
        st.subheader("⛅ Weather Info")
        st.write(weather_agent(destination))

    st.subheader("🗺️ Travel Itinerary")
    st.write(itinerary_agent(destination, days))