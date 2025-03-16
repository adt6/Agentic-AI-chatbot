from langchain_community.utilities import SQLDatabase
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_groq import ChatGroq
from langchain.chains import create_sql_query_chain
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter
from dotenv import load_dotenv
from custom_sql_tool import SQLToolkit 
import os
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize Database
db_path = "/Users/adityathakur/Desktop/Agentic AI/AI chatbot/database/Telecom.db"
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

st.title("📞 Telecom AI Chatbot")
st.write("Ask me anything about customer plans, devices, and details!")

# Fetch API key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found. Make sure it's set in the .env file.")

# Initialize LLM
llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0, api_key=groq_api_key)

sql_toolkit = SQLToolkit(llm, db)

# Wrap the SQL process query function as a LangChain tool
sql_tool = Tool(
    name="SQL Query Processor",
    func=lambda query: sql_toolkit.process_query({"input": query}),
    description="Use this tool to answer questions about customer plans, devices, or other details stored in the SQL database."
)

# Define agent tools
tools = [sql_tool]


# Initialize the agent with the custom SQL tool
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input field
user_input = st.chat_input("Ask a question about customer plans, devices, etc.")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Process query using agent
    response = agent.invoke({"input": user_input})
    bot_reply = response.get("output", "I couldn't find an answer.")

    # Display AI response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

