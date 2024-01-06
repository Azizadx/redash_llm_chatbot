import asyncio
import json
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

from bigquery_utils import execute_function_call
from openai_utils import get_gpt_response, chat_completion_request
from utils import count_token, pretty_print_conversation, load_prompts, load_tools
from google.cloud import bigquery

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = bigquery.Client.from_service_account_json(
    "service_account.json")
# Initialize Flask app
app = Flask(__name__)


# Route for handling user messages
@app.route('/chat', methods=['POST'])
def main():
    data = request.json
    system_message = f"""
    <prompts>
    {load_prompts()}
    </prompts>
    """

    system_message = system_message
    user_message = data.get("user_message", "")

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    gpt_response = get_gpt_response(system_message, user_message)
    messages.append({"role": "assistant", "content": gpt_response})
    chat_response = chat_completion_request(
        messages, load_tools(client=client))
    assistant_message = chat_response.json()["choices"][0]["message"]
    results = None
    # Execute the tool function call
    if assistant_message.get("tool_calls"):
        results = execute_function_call(assistant_message, client)
        messages.append({
            "role": "tool",
            "tool_call_id": assistant_message["tool_calls"][0]['id'],
            "name": assistant_message["tool_calls"][0]["function"]["name"],
            "content": results
        })

    # pretty_print_conversation(messages)

    if results is not None:
        return jsonify({"sql_query": assistant_message["tool_calls"][0]['id']}, {"assistant_response": results})
    else:
        return jsonify({"assistant_response": """I'm sorry, but as an AI language model, I don't have access to personal data about individuals unless it has been shared with me in the course of our conversation. I am designed to respect privacy and confidentiality. If "Aziza" refers to a public figure or a concept that is widely known and within my training data, I might be able to provide information. Otherwise, I would need more context to understand who or what "Aziza" refers to. Can you provide more details or clarify your question?"""})


# Run the application
if __name__ == '__main__':
    app.run()  # Set debug=True for development
