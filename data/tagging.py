import sqlite3
from transformers import pipeline
import sched, time

conn = sqlite3.connect('data.db')
cur = conn.cursor()

s = sched.scheduler(time.time, time.sleep)


def check_tags():
    cur.execute("select sample from tasks where type = 2 and sample is not null")
    rows = cur.fetchone()

    if rows:
        print(f"i: {rows}")
        tagging(rows[0])

    s.enter(10, 1, check_tags)


def get_existing_tags():
    results = cur.execute(
        f'select distinct tag from tags')

    rows = cur.fetchall()

    tags_results = []
    for i in rows:
        print(i[0])
        tags_results.append(i[0])

    return tags_results


def tagging(tag=None):
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

                emotion_labels = classifier(str(row[0]), candidate_labels, hypothesis_template=hypothesis_template)

                res = {}
                for key in emotion_labels['labels']:
                    for value in emotion_labels['scores']:
                        res[key] = "%.2f" % value
                        emotion_labels['scores'].remove(value)
                        break
                for tag in res:
                    if float(res[tag]) > .75:
                        query_2 = f'Insert into tags values (null, {row[1]}, "{tag}")'
                        conn.execute(query_2)
                        conn.commit()

    deletes = f"delete from tasks where sample = '{tag}' and seed_count = 0 and type = 2"
    print(f"deletes: {deletes}")
    conn.execute(deletes)
    conn.commit()

s.enter(10, 1, check_tags)
s.run()