1
import requests, sqlite3
connection = sqlite3.connect('test.db')
cur=connection.cursor()
r=requests.get('https://books.toscrape.com/')
title = r.text.split('title="')[1].split('"')[0]
# cur.execute('CREATE TABLE first_table(name TEXT)')
cur.execute(f"INSERT INTO first_table(name)VALUES(\"{title}\")")
connection.commit()
a= cur.execute(f"SELECT name FROM first_table").fetchall()
print(a)
connection.close()

