from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
	return 'cats rule'

@app.route('/gocatshome')
def gohome():
    return redirect('/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8088)

