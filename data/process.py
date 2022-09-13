import ast
import json
import sqlite3
# from transformers import pipeline, set_seed, AutoTokenizer, AutoModelForCausalLM

def process(sample):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        # sample = "you open the door and see"
        results = cur.execute(f'select seed, sample, text, summary from raw_data where remove = 0 and sample = "{sample}"')
        rows = cur.fetchall()
        for row in rows:
                keep = 3
                # print(row)
                print("-"*50)
                print(f"Raw: {row[2]}")
                print(f"Summary: {row[3]}")
                print("-" * 50)
                ans = input("Keep description? ")
                keep = 1 if ans == 'n' else 0
                print(keep)
                cur.execute(f'update raw_data set (keep, remove) = ({keep},1 ) where seed = {row[0]} and sample = "{row[1]}" and text = "{row[2]}"')
                conn.commit()

        return "a"

