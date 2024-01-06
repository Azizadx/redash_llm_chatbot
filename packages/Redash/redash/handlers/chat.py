from flask import request, jsonify
import requests
from redash.handlers.base import (
    BaseResource
)
import os
from openai import OpenAI
VARIABLE_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
    api_key=VARIABLE_KEY
)


class ChatResource(BaseResource):
    def post(self):
        try:
            value = request.get_json()
            user_question = value.get('question')
            backend_answer = requests.post(
                'http://127.0.0.1:6001/chat',
                json={"user_message": user_question
                      })
            response_data = backend_answer
            return response_data
        except Exception as error:
            print(error)
            return jsonify({"error": "An error occurred"}), 500
