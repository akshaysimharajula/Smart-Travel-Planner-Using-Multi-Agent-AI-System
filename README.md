### Smart Travel Planner – Multi-Agent AI System

**Smart Travel Planner** is an Agentic AI project that generates intelligent travel plans using a **Multi-Agent architecture**. The system uses multiple specialized AI agents to handle different tasks such as destination recommendation, budget analysis, weather information, and itinerary generation.

The application accepts user inputs including **travel type, preferred destination, budget, and trip duration**. Based on these inputs, different agents collaborate to create a **complete travel plan**. 

The project uses **Streamlit** to build an interactive web interface and integrates the **LLaMA 3.1** language model through the **Groq API** for fast LLM inference. 

Each AI agent performs a specific task:

* **Destination Agent** – Suggests travel destinations based on user preferences
* **Budget Agent** – Evaluates whether the destination fits the user’s budget
* **Weather Agent** – Provides weather insights for the selected destination
* **Itinerary Agent** – Generates a detailed day-wise travel plan

The system demonstrates how **multiple AI agents can collaborate to solve real-world problems** and automate travel planning efficiently.

**Tech Stack**

* Python
* Streamlit
* Groq API
* LLaMA-3.1-8B Model
* dotenv
* Requests
