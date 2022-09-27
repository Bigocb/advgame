import pymysql.cursors


# from transformers import pipeline, set_seed, AutoTokenizer, AutoModelForCausalLM
def process(sample):
    conn = pymysql.connect(user='bigocb', password='Lscooter11',
                           host='mysql.cldevlab.shop',
                           database='advgame_01',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    # sample = "you open the door and see"
    results = cur.execute(f'select seed, sample, text, summary, id from raw_data where remove = 0 and sample = "{sample}"')
    rows = cur.fetchone()
    print(rows)
    for row in rows:
        keep = 3
        # print(row)
        print("-" * 50)
        print(f"Raw: {row['text']}")
        print(f"Summary: {row['summary']}")
        print("-" * 50)
        ans = input("Keep description? ")
        keep = 1 if ans == 'n' else 0
        print(keep)
        query = f'update raw_data set keep = {keep}, remove = 1 where id = {row["id"]}'
        print(query)
        cur.execute(query)
        conn.commit()

    return "a"


process('you are standing in a field south of a house and')