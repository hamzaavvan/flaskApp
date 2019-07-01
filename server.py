from flask import Flask, render_template, request, jsonify, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return '<h1>Welcome Home </h1>'



if __name__=='__main__':
	app.run(host='0.0.0.0',port=3333,debug=True)