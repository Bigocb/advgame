import sqlite3
from transformers import pipeline
import sched, time
import pymysql.cursors


s = sched.scheduler(time.time, time.sleep)

def check_tags():
    conn = pymysql.connect(user='bigocb', password='Lscooter11',
                           host='mysql.cldevlab.shop',
                           database='advgame_01',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()


    cur.execute("select sample from tasks where type = 2 and sample is not null")
    rows = cur.fetchone()

    if rows:
        print(f"i: {rows}")
        tagging(rows['sample'])

    s.enter(10, 1, check_tags)
    cur.close()
    conn.close()


def get_existing_tags():
    conn = pymysql.connect(user='bigocb', password='Lscooter11',
                           host='mysql.cldevlab.shop',
                           database='advgame_01',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()

    results = cur.execute(
        f'select distinct tag from tags')

    rows = cur.fetchall()

    tags_results = []
    for i in rows:
        print(i['tag'])
        tags_results.append(i['tag'])
    cur.close()
    conn.close()
    return tags_results


def tagging(tag=None):
    conn = pymysql.connect(user='bigocb', password='Lscooter11',
                           host='mysql.cldevlab.shop',
                           database='advgame_01',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    if tag == 'reprocess' or not tag:
        existing_tags = get_existing_tags()
        user_tag = existing_tags
    else:
        user_tag = [tag]

    tag_list = user_tag

    classifier = pipeline('zero-shot-classification', model='roberta-large-mnli')

    hypothesis_template = "This text speaks about a {}."

    emotion = pipeline('sentiment-analysis',
                       model='Kamuuung/autonlp-lessons_tagging-606217261')

    for i in tag_list:
        print(f"i: {i}")
        candidate_labels = [f'{i}']
        f = 1
        while f > 0:
            results = cur.execute(
                f'select raw_data.text, raw_data.id, tags.id from raw_data left join tags on raw_data.id = tags.rd_id and tags.tag = "{i}" '
                f' where tags.id is null')

            rows = cur.fetchall()
            print(f"rows: {rows}")
            if len(rows) == 0:
                break
            for row in rows:
                f = f - 1

                emotion_labels = classifier(str(row['text']), candidate_labels, hypothesis_template=hypothesis_template)

                res = {}
                for key in emotion_labels['labels']:
                    for value in emotion_labels['scores']:
                        res[key] = "%.2f" % value
                        emotion_labels['scores'].remove(value)
                        break
                for tag in res:
                    if float(res[tag]) > .75:
                        query_2 = f'Insert into tags values (null, {row["id"]}, "{tag}")'
                        cur.execute(query_2)
                        conn.commit()

    deletes = f"delete from tasks where sample = '{tag}' and seed_count = 0 and type = 2"
    print(f"deletes: {deletes}")
    cur.execute(deletes)
    conn.commit()
    cur.close()
    conn.close()

s.enter(10, 1, check_tags)
s.run()