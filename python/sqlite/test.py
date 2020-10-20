import os
import sqlite3
conn = sqlite3.connect('/home/kunihiko/win/Desk_Original/python/sqlite3/sample_db.sqlite')
cur = conn.cursor()
cur.execute('select * from sample order by id')
res = cur.fetchone()
print(res)
conn.close()
