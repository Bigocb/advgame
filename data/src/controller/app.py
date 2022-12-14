import os
import json
import cryptography
from flask import Flask, request
from flask_cors import CORS, cross_origin
import pymysql.cursors
import sys
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '.')
from data.src.metrics.db import mets as metmain

app = Flask('controller')


@app.route('/')
def main():
    print('Hello ...')
    print('... World!')


@app.route('/generate', methods=['POST'])
@cross_origin()
def generate_text():
    cnx = pymysql.connect(user='bigocb', password='Lscooter11',
                          host='mysql.cldevlab.shop',
                          database='advgame_01',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor2 = cnx.cursor()
    req = request.json
    print(req)
    sample = req["sample"]
    seeds = req["seedCount"]
    ins = f"INSERT INTO tasks VALUES (null, 1, '{sample}',{seeds} )"
    cursor2.execute(ins)
    cnx.commit()
    cursor2.close()
    cnx.close()
    return {'url': 'test', 'status': 200}


@app.route('/tag', methods=['POST'])
@cross_origin()
def generate_tags():
    cnx = pymysql.connect(user='bigocb', password='Lscooter11',
                          host='mysql.cldevlab.shop',
                          database='advgame_01',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor2 = cnx.cursor()
    req = request.json
    tag = req["tag"]
    ins = f"INSERT INTO tasks VALUES (null, 2, '{tag}',0 )"
    print(f"tag: {tag}")
    cursor2.execute(ins)
    cnx.commit()
    cursor2.close()
    cnx.close()
    return {'url': 'test', 'status': 200}

@app.route('/metrics', methods=['GET'])
@cross_origin()
def generate_metrics():
    metrics = metmain()
    response = json.dumps(metrics)
    return response

@app.route('/process', methods=['GET'])
@cross_origin()
def generate_entry():
    cnx = pymysql.connect(user='bigocb', password='Lscooter11',
                          host='mysql.cldevlab.shop',
                          database='advgame_01',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor2 = cnx.cursor()
    results = cursor2.execute(f'select seed, sample, text, summary, id from raw_data where remove = 0')
    rows = cursor2.fetchone()
    response = json.dumps(rows)
    cursor2.close()
    cnx.close()
    return response

@app.route('/entries', methods=['GET'])
@cross_origin()
def get_entries():
    cnx = pymysql.connect(user='bigocb', password='Lscooter11',
                          host='mysql.cldevlab.shop',
                          database='advgame_01',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor2 = cnx.cursor()
    results = cursor2.execute(f'select seed, sample, text, id from raw_data where keep = 0 and remove = 1 and edited = 0')
    rows = cursor2.fetchall()
    response = json.dumps(rows)
    cursor2.close()
    cnx.close()
    return response

@app.route('/delete', methods=['POST'])
@cross_origin()
def delete():
    cnx = pymysql.connect(user='bigocb', password='Lscooter11',
                          host='mysql.cldevlab.shop',
                          database='advgame_01',
                          cursorclass=pymysql.cursors.DictCursor)
    req = request.json
    idx = req["id"]["id"]
    cursor2 = cnx.cursor()
    query = f'delete from raw_data where id = {idx}'
    cursor2.execute(query)
    cnx.commit()
    cursor2.close()
    cnx.close()
    return {'url': 'test', 'status': 200}

@app.route('/keep', methods=['POST'])
@cross_origin()
def keep_entry():
    cnx = pymysql.connect(user='bigocb', password='Lscooter11',
                          host='mysql.cldevlab.shop',
                          database='advgame_01',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor2 = cnx.cursor()

    req = request.json
    keep = req["keep"]
    print(keep)
    id = req["id"]["id"]

    if keep:
        query = f'update raw_data set keep = 0, remove = 1 where id = {id}'
    else:
        query = f'update raw_data set keep = 1, remove = 1 where id = {id}'
        print(query)
    cursor2.execute(query)
    cnx.commit()
    cursor2.close()
    cnx.close()
    return {'url': 'test', 'status': 200}

@app.route('/edit', methods=['POST'])
@cross_origin()
def update_entry():
    cnx = pymysql.connect(user='bigocb', password='Lscooter11',
                          host='mysql.cldevlab.shop',
                          database='advgame_01',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor2 = cnx.cursor()
    req = request.json
    text = req["text"]
    id = req["id"]["id"]
    query = f'update raw_data set text = "{text}", edited = 1 where id = {id}'

    cursor2.execute(query)
    cnx.commit()
    cursor2.close()
    cnx.close()

port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)
