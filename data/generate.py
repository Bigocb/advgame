import random
import sqlite3
import sched, time
conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()
s = sched.scheduler(time.time, time.sleep)
from transformers import pipeline, set_seed


# models:
# huggingtweets/alice_lbl-lotrbookquotes-theprincess_lbl
# mindwrapped/gpt2-lotr-fellowship
# huggingtweets/alice_lbl-lotrbookquotes
# gyre/200wordrpgmodel
# EleutherAI/gpt-neo-1.3B
# PatrickTyBrown/GPT-Neo_DnD_Control
def random_exclude(range_start, range_end, excludes):
    r = random.randint(range_start, range_end)
    if r in excludes:
        return random_exclude(range_start, range_end, excludes)
    return r


def check_entries():
    cur.execute("select sample, seed_count from tasks where type = 1")
    rows = cur.fetchone()

    if rows:
        print(f"i: {rows}")
        generate(rows[0], rows[1])

    s.enter(10, 1, check_entries)


def generate(sample, seed_cnt):

    models = ['huggingtweets/alice_lbl-lotrbookquotes']
    for i in models:
        model = i
        summarization = pipeline("summarization", model="facebook/bart-large-cnn", max_length=512)

        gpt_j_generator = pipeline('text-generation', model=model)
        keys = cur.execute(f'select distinct seed from raw_data where sample = "{sample}"')
        rows = cur.fetchall()

        seeds = []
        for row in rows:
            seeds.append(row[0])

        print(f"seed_cnt: {seed_cnt}")
        seed_cnt = int(seed_cnt)
        for i in range(seed_cnt):

            t = random_exclude(0, 6111000, seeds)

            set_seed(t)

            # generate sentences with TOP-K sampling
            sentences = gpt_j_generator(sample, do_sample=True,
                                        top_k=50, temperature=0.6, max_length=512,
                                        num_return_sequences=1)
            test = []
            test.append({'seed' : t, 'sample' : sample, 'model' : model})
            for sentence in sentences:

              sentence['seed'] = t
              sentence['sample'] = sample
              text = sentence['generated_text']
              text = str(text).replace(",","%2C")
              text = str(text).replace('"', "&quot;")
              text = str(text).replace("'", "&apos;")
              text = str(text).replace("!", "&exl;")
              summary_text = summarization(text)[0]['summary_text']
              summary_text = str(summary_text).replace(",", "%2C")
              summary_text = str(summary_text).replace('"', "&quot;")
              summary_text = str(summary_text).replace("'", "&apos;")
              summary_text = str(summary_text).replace("!", "&exl;")
              query_2 = f'Insert into raw_data values (null, {t}, "{sample}","{model}","{text}","{summary_text}",0,0)'
              # print(f"query: {query_2}")
              conn.execute(query_2)
              conn.commit()

    deletes = f"delete from tasks where sample = '{sample}' and seed_count = {seed_cnt}"
    print(f"deletes: {deletes}")
    conn.execute(deletes)
    conn.commit()

    return "done"


s.enter(10, 1, check_entries)
s.run()
