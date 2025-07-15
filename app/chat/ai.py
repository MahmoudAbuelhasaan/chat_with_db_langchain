import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent , SQLDatabaseToolkit
from sqlalchemy import create_engine,inspect
from app import db
from config import Config

# Load environment variables from .env file
load_dotenv()


def intialize_sql_agent(user_role=None):
    # Initialize the SQL database
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    # create inspector: db schema and tables validation 
    inspector = inspect(engine)

    # get the list of tables in the database
    tables = inspector.get_table_names()
    avliable_tables = tables

    # create the langchain SQLdatabase 
    sql_db = SQLDatabase.for_uri(
        Config.SQLALCHEMY_DATABASE_URI,
        sample_rows_in_table_info=2, # number of sample rows to fetch for each table
        include_tables=tables,
        )
    # create llm 
    model_name = os.environ.get("MODEL")
    if not model_name:
        raise EnvironmentError("The environment variable 'MODEL' is not set. Please set it to the name of the model to use with ChatOllama.")
    llm = ChatOllama(model=model_name)

    # create the SQL database toolkit
    toolkit = SQLDatabaseToolkit(db=sql_db, llm=llm)

    # create prompt 
    # create prompt
    system_prompt = f""" you are a business analyst providing isights about data in database

CRITICAL INSTRUCTIONS:
1. NEVER mention SQL , queries , tables or database operators
2. Give Only final business insights with professional formatting
3. Never give any technical details about database or queries
4. Use emojis and clear structure
5. Format numbers with comma and currency symbol
6. Do NOT assume or imagine any data — only use what is explicitly available
7. If no relevant result is found, respond with: **No data found.**

AVAILABLE DATA:{avliable_tables}

RESPONSE TEMPLATES:
- for counts: **Metric**: [Number] [context]
- for percentages: **Metric**: [Number]%
- for ratios: **Metric**: [Number] : [context]
- for values: **Metric**: [Number]
- for revenu: **Revenue**: [Amount] [time/context]
- for profit: **Profit**: [Amount]
    """
    # create the SQL agent
    sql_agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        system_prompt=system_prompt,
        verbose=True,
        # agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    return sql_agent

        

        
