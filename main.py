import json

from flask import Flask, request

from analyzer.tokenizer import Tokenizer
from analyzer.filter import Filter
from cache.handler import CacheHandler
from api.response import build_status, build_hateoas

app = Flask(__name__)

file_tokenizer = Tokenizer()
stream_filter = Filter()
cache_handler = CacheHandler()


@app.route("/files", methods=["GET", "POST"])
def files():

    if request.method == "GET":
        payload = request.json
        result = cache_handler.search(payload["token"])
        status = build_status(200, "search complete")
        response = build_hateoas(None, status, result, None)
        return json.dumps(response, indent=4)

    elif request.method == "POST":
        payload = request.json
        tokens = file_tokenizer.load(payload["file"]).tokenize_by_blank().extract()
        tokens = stream_filter.load(tokens).filter_ascii().extract()
        cache_handler.apply(payload["file"], tokens)
        status = build_status(201, "resource created")
        response = build_hateoas(None, status, tokens, None)
        return json.dumps(response, indent=4)


if __name__ == '__main__':
    app.run()
