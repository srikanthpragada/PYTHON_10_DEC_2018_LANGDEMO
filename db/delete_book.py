
import sqlite3

con = sqlite3.connect(r"e:\classroom\python\dec10\library.db")
cur = con.cursor()
id  = input("Enter title id  : ")
cur.execute("delete from books where id = ?",(id,))
if cur.rowcount == 1:
   con.commit()
   print(f"Deleted title with id {id} successfully!")
else:
   print(f"Could not find title with id {id}")

con.close()