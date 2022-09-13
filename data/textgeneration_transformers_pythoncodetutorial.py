import random
import json
import sqlite3
import unicodedata
import re
from string import *
conn = sqlite3.connect('data.db')
cur = conn.cursor()

from transformers import pipeline, set_seed, AutoTokenizer, AutoModelForCausalLM



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

def generate(sample, seed_cnt):

    models = ['huggingtweets/alice_lbl-lotrbookquotes']
    for i in models:
        model = i
        summarization = pipeline("summarization", model="facebook/bart-large-cnn", max_length=512)

        gpt_j_generator = pipeline('text-generation', model=model)
        # count = cur.execute('select count(distinct seed) from raw_data where sample = "{sample}"')
        # cnt = cur.fetchone()
        # # print(cnt)

        # sample = "you open the door and see"
        keys = cur.execute(f'select distinct seed from raw_data where sample = "{sample}"')
        rows = cur.fetchall()

        seeds = []
        for row in rows:
            seeds.append(row[0])
            # print(row[0])

        seed_cnt = int(seed_cnt)
        for i in range(seed_cnt):

            t = random_exclude(0, 6111000, seeds)
            # test_text = summarization(sample)[0]['summary_text']
            # print(test_text)
            # test_text = str(test_text).replace(",", "%2C")
            # test_text = str(test_text).replace('"', "&quot;")
            # test_text = str(test_text).replace("'", "&apos;")
            # test_text = str(test_text).replace("!", "&exl;")
            # query_1 = f'Insert into raw_data values ({t}, "{sample}","{model}","","{test_text}",0,0)'
            # conn.execute(query_1)
            # conn.commit()


            # t = 6102750
            set_seed(t)

            # generate sentences with TOP-K sampling
            sentences = gpt_j_generator(sample, do_sample=True,
                                        top_k=50, temperature=0.6, max_length=512,
                                        num_return_sequences=5)
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

            # print("="*50)
