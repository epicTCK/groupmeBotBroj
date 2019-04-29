from flask import Flask, request
import requests
import os
app = Flask(__name__)

@app.route('/post', methods = ['POST'])
def post():
	requests.post("https://api.groupme.com/v3/bots/post",{"text" : requests.data, "bot_id" : "475117f0e94dd02bd7c7e380fc"})
	print(request.data)
	return ''

app.run(host='0.0.0.0', port=os.environ.get('PORT'))
