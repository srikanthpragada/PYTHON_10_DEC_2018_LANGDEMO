import sqlite3

try:
   con = sqlite3.connect(r"e:\classroom\python\dec10\library.db")
   cur = con.cursor()
   id = input("Enter title id  : ")
   price = input("Enter new price  : ")
   cur.execute("update books set price = ? where id = ?", (price, id))
   if cur.rowcount == 1:
      con.commit()
      print(f"Updated title with id {id} successfully!")
   else:
      print(f"Could not find title with id {id}")
except Exception as ex:
   print("Error : ", ex)
finally:
   con.close()
