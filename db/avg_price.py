
import sqlite3

con = sqlite3.connect(r"e:\classroom\python\dec10\library.db")
cur = con.cursor()
cur.execute("select avg(price) from books")
avgprice = cur.fetchone()[0]
print(f"Average price : {avgprice:6.2f}")
con.close()