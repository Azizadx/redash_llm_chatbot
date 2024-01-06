from flask import jsonify
import requests
res = requests.post(
    'http://127.0.0.1:6001/chat',
    json={"user_message": 'who is aziza?'
          })
print(jsonify(res))
