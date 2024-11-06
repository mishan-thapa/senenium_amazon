from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title':[], 'price':[]}

for file in os.listdir("search_result_web_scrapping_data_folder"):
    try:
        with open(f"search_result_web_scrapping_data_folder/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("h2")
        title = t.get_text()
        d['title'].append(title)
        print(title)

        p = soup.find("span", attrs={"class": 'a-price-whole'})
        price = p.get_text()
        d['price'].append(price)
        print(price)
    except Exception as e:
        print(e)

df = pd.DataFrame(data=d)
df.to_csv("search_result_scrapped.csv")