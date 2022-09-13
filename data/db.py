import sqlite3
import textgeneration_transformers_pythoncodetutorial as generator
import process
import tagging


def main():

    print("-"*50)
    print("Choose a task: ")
    print("a) Process ")
    print("b) Generate ")
    print("c) Review")
    print("d) Tagging")
    anst = input("Choice ? ")

    anss = input(f"What is your sample? ")
    if anss == None or anss == '':
        sample = "the young elf"
    else:
        sample = anss

    if anst == 'b' or anst == 'a' or anst == 'd':
        # sample
        if anst == 'b':
            ansc = input("How many seeds ? ")

            seeds = 0
            if ansc == None or ansc == '':
                seeds = 2
            else:
                seeds = ansc
            generator.generate(sample, seeds)
        elif anst == 'a':
            process.process(sample)
        elif anst == 'd':
            print(tagging)
            tagging.tagging()
    else:

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        # cursor.execute("Drop table raw_data")
        # conn.commit()
        # cursor.execute("CREATE TABLE raw_data (seed integer , sample varchar(255),model varchar(255), text TEXT, summary TEXT, keep integer, remove integer )")
        # conn.commit()
        #t = cursor.execute("select * from raw_data")
        t = cursor.execute(("select sample, count(keep) from raw_data where keep = 0 and remove = 1 group by sample"))
        print("-"*50)
        print("Keep:")
        for i in t:
            print(i)
        print("-"*50)

        x = cursor.execute(("select sample, count(keep) from raw_data where keep = 1 and remove = 1 group by sample"))
        print("-"*50)
        print("Removed:")
        for t in x:
            print(t)
        print("-"*50)

        print("To be processed:")
        c = cursor.execute(("select sample, model, count(keep) from raw_data where keep = 0 and remove = 0 group by sample, model"))
        for x in c:
            print(x)
        print("-"*50)

        print(f"all:")
        c = cursor.execute(("select count(summary) from raw_data where keep = 0 and remove = 0"))
        for x in c:
            print(x)
        print("-"*50)

        print(f"count seeds")
        p = cursor.execute((f'select count(distinct seed) from raw_data where sample = "{sample}"'))
        for o in p:
            print(o)
        print("-"*50)

        print(f"count seeds")
        p = cursor.execute((f'select sample, count(sample) from raw_data where sample = "{sample}"'))
        for o in p:
            print(o)
        print("-"*50)

        print("print tags")
        g = cursor.execute((f'select tag, count(tag) from tags group by tag'))
        for h in g:
            print(h)
        print("-" * 50)

if __name__ == '__main__':
    main()