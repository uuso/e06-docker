#!/usr/bin/python3.7 -u

from os import getenv
from flask import Flask, request
from flask_caching import Cache


app = Flask(__name__)

config = {
        "DEBUG": True,          # some Flask specific configs
        "CACHE_TYPE": "memcached", # Flask-Caching related configs
        "CACHE_DEFAULT_TIMEOUT": 300,
        "CACHE_MEMCACHED_SERVERS": [getenv("CACHESRV"),],
        "CACHE_KEY_PREFIX": "flask-hw-e06:"
}
app.config.from_mapping(config)
cache = Cache(app)


@cache.memoize(timeout=50)
def fibo_nth(nth):
        print("in %d" % nth)
        if nth <= 1:
                return 0
        if nth <= 3:
                return 1
        return fibo_nth(nth-2) + fibo_nth(nth-1)

@app.route("/")
def index():
        nth = 0
        if request.method == "GET":
                nth = request.args.get('k', 0)
                try:
                        nth = int(nth)
                except:
                        nth = 0
        return str(fibo_nth(nth))

if __name__ == "__main__":
        app.run(debug=True, port=getenv("PORT"), host="0.0.0.0")