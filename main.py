# 1
import requests, sqlite3
# connection = sqlite3.connect('test.db')
# cur=connection.cursor()
# r=requests.get('https://books.toscrape.com/')
# title = r.text.split('title="')[1].split('"')[0]
# # cur.execute('CREATE TABLE first_table(name TEXT)')
# cur.execute(f"INSERT INTO first_table(name)VALUES(\"{title}\")")
# connection.commit()
# a= cur.execute(f"SELECT name FROM first_table").fetchall()
# print(a)
# connection.close()
from bs4 import BeautifulSoup
# import requests
# response = requests.get("https://
# coinmarketcap.com/")
# if response.status_code == 200:
#   soup = BeautifulSoup(response.text,
#   features="html.parser")
#   soup_list = soup.find_all("a", {"href": "/
#   currencies/bitcoin/markets/"})
# res = soup_list[0].find("span")
# print(res.text)
# 2

response=requests.get("https://books.toscrape.com/")
if response.status_code==200:
    soup =BeautifulSoup(response.text,features="html.parser")
    prices = soup.find_all("p", class_="price_color")

    for price in prices:
        print(price.text)
