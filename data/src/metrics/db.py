import pymysql.cursors

def mets():

        conn = pymysql.connect(user='bigocb', password='Lscooter11',
                               host='mysql.cldevlab.shop',
                               database='advgame_01',
                               cursorclass=pymysql.cursors.DictCursor)

        metrics = {}

        cur = conn.cursor()
        # cur.execute(("select sample, count(keep) from raw_data where keep = 0 and remove = 1 group by sample"))
        # rows = cur.fetchone()
        # if rows:
        #     print("-"*50)
        #     print("Keep:")
        #     for i in rows:
        #         print(i)
        #     print("-"*50)

        cur.execute("select sample,model, count(case when keep = 0 then keep end) as keep ,count(case when keep = 1 then keep end) as remove, count(keep) as total, round(count(case when keep = 0 then keep end)/count(keep)*100,2) as per from raw_data where remove = 1 group by sample, model order by round(count(case when keep = 0 then keep end)/count(keep)*100,2) desc")
        rows = cur.fetchall()
        if rows:
            samples = []
            for t in rows:
                sample = {}
                sample['sample'] = t['sample']
                sample['keep'] = t['keep']
                sample['remove'] = t['remove']
                sample['total'] = t['total']
                sample['model'] = t['model']
                sample['per'] = str(t['per'])
                samples.append(sample)
            metrics['samples'] = samples



        # cur.execute(("select sample, model, count(keep) from raw_data where keep = 0 and remove = 0 group by sample, model"))
        # rows = cur.fetchall()
        #
        # if rows:
        #     print("To be processed:")
        #     for x in rows:
        #         print(x['sample'] + ": " + str(x['count(keep)']))
        #     print("-"*50)
        cur.execute(("select count(summary) from raw_data"))
        rows = cur.fetchone()
        if rows:
            metrics['total'] = rows['count(summary)']

        cur.execute(("select count(summary) from raw_data where keep = 0 and remove = 0"))
        rows = cur.fetchone()
        if rows:
            print(f"all:")
            print(rows['count(summary)'])
            metrics['tbp'] = rows['count(summary)']
            # for x in rows:
            #     print(x['count(summary)'])
            # print("-"*50)

        cur.execute(("select count(summary) from raw_data where keep = 0 and remove = 1"))
        rows = cur.fetchone()
        if rows:
            metrics['keep'] = rows['count(summary)']

        cur.execute(("select count(summary) from raw_data where keep = 1 and remove = 1 "))
        rows = cur.fetchone()
        if rows:
            metrics['Remove'] = rows['count(summary)']

        return metrics

        # cur.execute((f'select tag, count(tag) from tags group by tag'))
        # rows = cur.fetchall()
        # if rows:
        #     print("print tags")
        #     for h in rows:
        #         print(h)
        #     print("-" * 50)

# if __name__ == '__main__':
#     main()