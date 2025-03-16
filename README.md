# Agentic-AI-chatbot
###Overview:
This project is an basic Agentic AI chatbot designed for a telecom service provider, capable of answering customer-related queries by interacting with a SQL database. It integrates LangChain, Groq’s LLM (Mixtral-8x7B), and function-calling models to retrieve real-time data from structured sources.

###🔹 Key Features:

Natural Language Query Execution: Converts user queries into SQL and fetches relevant results.
Tool-Calling Capabilities: Uses function-calling models to execute database queries.
Multi-Agent Architecture: (Potential transition to Agency Swarm for better AI workflow management).
UI Integration: Streamlit-based chatbot UI for user interaction.
Authentication & Security: Secure API key management using .env files.

###🔹 Tech Stack:

- LangChain (Agentic AI)
- Groq’s LLM (Mixtral-8x7B)
- SQLite Database
- Python, Streamlit (UI)

# Chatbot Testing - README

###Overview:
This project serves as a testing environment to analyze how an agent selects the appropriate tool based on the user's input. The goal is to observe, debug, and optimize tool selection logic in LangChain's agent framework before applying it to the main chatbot.

###🔹 Key Focus Areas:

- 🛠 Agent Tool Selection: How the agent decides which function to execute.
- 📊 Handling Different Input Types: Testing function calls with and without parameters.
- 🔄 Automatic Error Handling: Ensuring smooth execution using handle_parsing_errors=True.


