import json

import requests
from bs4 import BeautifulSoup

cookies = {
    "language": "tr"
}

session = requests.Session()
session.cookies.update(cookies)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive"
}

url = "https://www.trendyol.com/avva-x-b257"

response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="p-card-chldrn-cntnr")
data=[]

for product in products:
    tmp={}
    title_tag = product.find("span", class_="prdct-desc-cntnr-name")
    desc_tag = product.find("div", class_="product-desc-sub-text")
    image_tag = product.find("img", class_="p-card-img")
    price_tag = product.find("div", class_="price-item")

    if title_tag and image_tag and price_tag:
        title = title_tag.text.strip()
        description = desc_tag.text.strip() if desc_tag else "No description"
        image = image_tag["src"] if image_tag.has_attr("src") else image_tag["data-src"]
        price = price_tag.text.strip()
        tmp['title']=title
        tmp['description']=description
        tmp['image']=image
        tmp['price']=price
        data.append(tmp)

with open('products.json', 'w') as f:
    json.dump(data, f, indent=4)
