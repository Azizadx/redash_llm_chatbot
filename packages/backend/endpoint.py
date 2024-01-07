import json
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, Blueprint

from bigquery_utils import execute_function_call
from ai_utils import get_gpt_response, chat_completion_request
from utils import count_token, pretty_print_conversation, load_prompts, load_tools
from google.cloud import bigquery

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = bigquery.Client.from_service_account_json(
    "service_account.json")
# Initialize Flask app
main_app = Blueprint('main', __name__)


# Route for handling user messages
@main_app.route('/chat', methods=['POST'])
def main():
    print('in')
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
        return jsonify(json.loads(assistant_message["tool_calls"][0]["function"]["arguments"])["query"], results)
    else:
        return jsonify("""am sorry i couldn't do the task ;(""")
