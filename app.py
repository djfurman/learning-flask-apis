#!/usr/bin/env python3
"""Basic Task Application built as RESTful API
"""

from flask import Flask, make_response, jsonify
app = Flask(__name__)

@app.route('/health')
def health():
    discoverable = {'docs': 'some doc endpoint'}
    return make_response(jsonify(discoverable), 200)

if __name__ == '__main__':
    app.run(debug=True)
