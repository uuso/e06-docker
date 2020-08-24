from flask import Flask
from os import getenv
import json 

app = Flask(__name__)

def fibo_nth(nth):
	if nth <= 1:
		return 0
	if nth <= 3:
		return 1
	return fibo_nth(nth-2)+fibo_nth(nth-1)


@app.route('/<int:nth>')
def get_fib(nth):
	return json.dumps({nth:fibo_nth(nth)})

if __name__ == '__main__':
	app.run(port = getenv("PORT"))