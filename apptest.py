from flask import Flask, request

#init the app
app = Flask(__name__, static_url_path='/static/')

@app.route('/')
def index():
	return app.send_static_file('index.html')
	
@app.route('/python/')
def python():
	return app.send_static_file('python.html')
	
@app.route('/flask/')
def flask():
	return app.send_static_file('flask.html')
	
if __name__ == '__main__':
	app.run(debug=True)