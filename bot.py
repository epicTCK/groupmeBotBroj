from flask import Flask, request
import requests
import os
import json

app = Flask(__name__)

@app.route('/post', methods = ['POST'])
def post():
	responseInput = request.get_json()
	if responseInput['name'] != 'testBot':
		requests.post("https://api.groupme.com/v3/bots/post",{"text" : responseInput['text'], "bot_id" : "475117f0e94dd02bd7c7e380fc"})
	return ''

app.run(host='0.0.0.0', port=os.environ.get('PORT'))
