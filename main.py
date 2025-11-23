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

# 2

# response=requests.get("https://books.toscrape.com/")
# if response.status_code==200:
#     soup =BeautifulSoup(response.text,features="html.parser")
#     prices = soup.find_all("p", class_="price_color")
#
#     for price in prices:
#         print(price.text)
# 3
response=requests.get("https://books.toscrape.com/")
if response.status_code== 200:
    soup=BeautifulSoup(response.text, "html.parser")
    title = soup.find_all("h3")
    prices= soup.find_all("p", class_="price_color")
    availability=soup.find_all("p", class_="instock availability")
    for a in availability:
        availability_text=a.text.strip()
        print(availability_text)

    for t in title:
        title_text = t.find("a")["title"]

        print(title_text)
    for p in prices:
        price_text = p.text.strip()

        print(price_text)

