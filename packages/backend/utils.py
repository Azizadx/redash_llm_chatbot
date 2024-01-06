import json
from termcolor import colored

from bigquery_utils import get_database_info


def count_token(input, model_name="gpt-4-1106-preview", debug=False):
    import tiktoken
    encoding = tiktoken.encoding_for_model(model_name)
    codex = " ".join(input.splitlines())  # Join lines into a single string
    num_tokens = len(encoding.encode(codex))
    return num_tokens


def pretty_print_conversation(messages):
    role_to_color = {
        "system": "red",
        "user": "green",
        "assistant": "blue",
        "tool": "magenta",
    }

    for message in messages:
        if message["role"] == "system":
            print(
                colored(f"system: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "user":
            print(
                colored(f"user: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and message.get("function_call"):
            print(colored(
                f"assistant: {message['function_call']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and not message.get("function_call"):
            print(colored(
                f"assistant: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "tool":
            print(colored(
                f"function ({message['name']}): {message['content']}\n", role_to_color[message["role"]]))


def load_prompts():
    # Load prompts from a file or database here
    prompts = """
    # General Analysis Queries
    1. "What are the most significant trends in viewership data over the past month? Consider views, watch time, and average view duration across different tables."
    2. "Identify the top-performing videos in the last quarter based on data from the dim_top10 table."
    ...

    # Specific Data Requests
    3. "Provide a breakdown of views, watch time, and average view duration by device type for the past week, using data from raw_total and raw_gender tables."
    4. "Show me the top 5 traffic sources driving the most views to the channel based on available data."
    ...

    # SQL Query Generation
    5. "Generate an SQL query to retrieve specific data points from specified tables. Clearly state the desired data points and conditions."
    6. "Translate this natural language question into an SQL query: [Ask your question in plain English, specifying relevant tables]."
    ...

    # Data Clarification
    7. "Could you please clarify what you mean by X, and which tables or columns are relevant to your query?"
    8. "Provide an example of what you're looking for, specifying the tables and columns you'd like to focus on."
    ...

    # Uncertainty Handling
    9. "I'm not confident in providing an accurate answer to that question based on available data. Would you like me to generate an approximate response or seek further input?"
    10. "I'm unable to generate a query for that question due to ambiguity or potential data limitations. Could you please rephrase it or provide more specific details, including relevant tables and columns?"
    ...

    # Additional Tables and Descriptions
    - youtube.dim_dail_view_7day: Daily Views Trend (7-Day Rolling Average)
    Columns: Date, RollingAverageViews
    Example Table Data: 2020-09-02 18.857142857142858

    - youtube.dim_top10: Top 10 Days by Views
    Columns: Date, TotalViews
    Example Table Data: 2022-08-09 311

    - youtube.raw_cities: List of all cities
    Columns: Cities, City_name, Geography, Geography_3, Views, Watch_time__hours_, Average_view_duration
    Example Table Data:
        - 0x164b85cef5ab402d:0x8467b6b Addis Ababa, ET, ET-AA, 1252, 127.5042, 00:06:06

    - youtube.raw_total: Total views by daily Date column is in this format yyy-mm-dd
    Columns: Date, Views
    Example Table Data: 2020-07-10 0
    """
    return prompts


def load_tools(client):
    tools = [
        {
            "type": "function",
            "function": {
                "name": "ask_database",
                "description": "Use this function to answer user questions about youtube. Input should be a fully formed SQL query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": f"""

                                SQL query extracting info to answer the user's question.
                                SQL should be written using this database schema:
                                {get_database_info(client,'youtube')}
                                The query should be returned in plain text, not in JSON.
                                """,
                        }
                    },
                    "required": ["query"],
                },
            }
        }
    ]
    return tools
