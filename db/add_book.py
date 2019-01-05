
import sqlite3

con = sqlite3.connect(r"e:\classroom\python\dec10\library.db")
cur = con.cursor()
title  = input("Enter title  : ")
author = input("Enter author : ")
price =  input("Enter price  : ")
cur.execute("insert into books(title,author,price) values(?,?,?)",
               (title,author,price))
con.commit()
print(f"Added {cur.rowcount} book(s) successfully!")
con.close()