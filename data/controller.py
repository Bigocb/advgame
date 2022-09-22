from flask import Flask, request
# import flask_cors
from flask_cors import CORS, cross_origin
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()


@app.route('/')
def main():
    print('Hello ...')
    print('... World!')


@app.route('/generate', methods=['POST'])
@cross_origin()
def generate_text():
    req = request.json
    sample = req["sample"]
    seeds = req["seedCount"]
    ins = f"INSERT INTO tasks VALUES (null, 1, '{sample}',{seeds} )"
    conn.execute(ins)
    conn.commit()
    return {'url': 'test', 'status': 200}


@app.route('/tag', methods=['POST'])
@cross_origin()
def generate_tags():
    req = request.json
    tag = req["tag"]
    ins = f"INSERT INTO tasks VALUES (null, 2, '{tag}',0 )"
    print(f"tag: {tag}")
    conn.execute(ins)
    conn.commit()
    return {'url': 'test', 'status': 200}


if __name__ == '__main__':
    app.run()
