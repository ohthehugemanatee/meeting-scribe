# coding=utf-8
import logging
from flask import Flask, request, jsonify
from gensim.summarization import summarize, keywords

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_text():
    if not request.json or not 'transcript' in request.json:
        abort(400)
    # Here we can do some processing on the text.
    summary = summarize(request.json['transcript'])
    keyword_list = keywords(request.json['transcript'])

    # For now, return a static response.

    response = {
        'summary': summary,
        'keywords': keyword_list,
    }
    return jsonify(response), 200

if __name__ == '__main__':
  app.run(debug=True)
