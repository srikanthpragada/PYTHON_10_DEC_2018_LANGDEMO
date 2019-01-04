
import sqlite3

con = sqlite3.connect(r"e:\classroom\python\dec10\library.db")
cur = con.cursor()
cur.execute("select * from books order by price")
for id,title,price,author in cur.fetchall():
    print(f"{title:50s} {author:30s}  {price:4d}")

con.close()