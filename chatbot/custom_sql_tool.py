# custom_tools.py
from langchain_core.runnables import RunnablePassthrough
from langchain_community.tools import QuerySQLDatabaseTool
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from operator import itemgetter

class SQLToolkit:
    def __init__(self, llm, db):
        self.llm = llm
        self.db = db
    
        self.generate_query = create_sql_query_chain(llm, db)
        self.execute_query = QuerySQLDatabaseTool(db=db, return_direct=True)

        
        
        # Define prompt for natural language responses
        self.answer_prompt = PromptTemplate.from_template(
            """Based on the following SQL result, provide a **concise and direct** answer using the exact customer's name, plan's name and device'name associated with their ID's from the SQL result.
    
            Question: {question}
            SQL Result: {result}
    
            Provide a **short, final answer** without explaining the SQL query. Example answers: "John Smith has 2 devices", "Mike Tyson is on a 'premium plan'".
    
            Answer: """
        )

        self.rephrase_answer = self.answer_prompt | llm | StrOutputParser()

        # Define the chaining process
        self.chain = (
            RunnablePassthrough.assign(query=lambda x: self.clean_query(self.generate_query.invoke(x)))
            .assign(result=itemgetter("query") | self.execute_query)
            | self.rephrase_answer
        )

    def clean_query(self, query):
        """Removes escape characters like backslashes from generated SQL queries."""
        return query.replace("\\", "")

    def process_query(self, input_data: dict) -> str:
        """Executes the entire chain and returns a human-readable answer."""
        question = input_data.get("question") or input_data.get("input")

        print(f"Input Question: {question}")


        return self.chain.invoke({"question": question})


