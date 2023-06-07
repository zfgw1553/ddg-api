from flask import Flask, request
from duckduckgo_search import DDGS
app = Flask(__name__)


@app.route('/search')
def search():  # put application's code here
    keywords = request.args.get('q')
    print(request.args.get('max_results'))
    max_results = int(request.args.get('max_results') or "3")
    results = []
    from itertools import islice
    with DDGS() as ddgs:
        ddgs_gen = ddgs.text(keywords, safesearch='Off', timelimit='y', backend="lite")
        for r in islice(ddgs_gen, max_results):
            results.append(r)
    return results


if __name__ == '__main__':
    app.run(host='0.0.0.0')
