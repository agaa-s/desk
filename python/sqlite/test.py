import os
import sqlite3

DB_PATH = 'sample_db.sqlite'

### __file__ : 実行している .py のパス
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

con = sqlite3.connect(DB_PATH)
cur = con.cursor()
cur.execute('select * from sample order by id')
res = cur.fetchall()
con.close()

"""
fetchall() の返り値は
tuple () の list []
"""
print(type(res))
print(res)
for r in res:
    print(type(r))
    print(r)
    for f in r:
        print(type(f))
        print(f)
