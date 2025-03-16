from langchain_community.utilities import SQLDatabase
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
#from sql_tool import SQLToolkit1 
import os
from langchain.tools import tool


# Load environment variables
load_dotenv()

# Initialize Database
db_path = "/Users/adityathakur/Desktop/Agentic AI/AI chatbot/database/Telecom.db"
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")



# Fetch API key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found. Make sure it's set in the .env file.")

# Initialize LLM
llm = ChatGroq(model="mistral-saba-24b", temperature=0, api_key=groq_api_key)

# sql_toolkit = SQLToolkit1()

@tool
def getPlanDevices(customer_id: int) -> int:
        """From the given customer Id, simply return the name of the plan and the device"""
        
        return f"Customer {customer_id} has Plan A and iPhone 14."
 
@tool
def getCxName(customer_id: int) -> int:
        """From the given customer Id, simply return the name of the customer"""
        
        return f"Customer name is John Smith whose Id is {customer_id}."

@tool
def getAllDevices(dummy: str = "default") ->str:
       """This is a function that does not take any parameter and it simply returns the list of all the devices."""

       return "List of all the devices are: Iphone,samsung, Moto"


# Define agent tools
# tools = sql_toolkit.get_tools() 
tools = [getPlanDevices,getCxName,getAllDevices]


# Initialize the agent with the custom SQL tool
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True,
)

# Example question
#List of questions -> 
# What is the name of the customer whose Id is 14 and what plan and the device the customer has?
# Could you give me a list of all devices?
question = "Could you give me a list of all devices?"
response = agent.invoke({"input": question})

print("Agent Response:", response)