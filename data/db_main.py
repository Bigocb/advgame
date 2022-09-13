import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# cursor.execute("Drop table raw_data")
# conn.commit()

# cursor.execute("CREATE TABLE raw_data (id INTEGER PRIMARY KEY,seed integer , sample varchar(255),model varchar(255), text TEXT, summary TEXT, keep integer, remove integer )")
# conn.commit()

cursor.execute("CREATE TABLE tags (id INTEGER PRIMARY KEY,rd_id integer , tag varchar(255))")
conn.commit()


# cursor.execute("Delete from raw_data where text = '' ")
# conn.commit()