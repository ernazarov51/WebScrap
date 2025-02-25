import json

import requests
from bs4 import BeautifulSoup

cookies = {
    "COOKIE_TY.Anonym": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cm46dHJlbmR5b2w6YW5vbmlkIjoiNzA4Njg4MjhmMjhhMTFlZmFhNGI5ZWZhZjRiODRhYjQiLCJyb2xlIjoiYW5vbiIsImF0d3J0bWsiOiI3MDg2ODgyNC1mMjhhLTExZWYtYWE0Yi05ZWZhZjRiODRhYjQiLCJhcHBOYW1lIjoidHkiLCJhdWQiOiJzYkF5ell0WCtqaGVMNGlmVld5NXR5TU9MUEpXQnJrYSIsImV4cCI6MTg5ODE3NDE4NywiaXNzIjoiYXV0aC50cmVuZHlvbC5jb20iLCJuYmYiOjE3NDAzODYxODd9.GlxVrlGYQuqh7k5GRgMCvXR5ZyjFPfyN9MLL0jxos2Y",
    "COOKIE_TY.IsUserAgentMobileOrTablet": "false",
    "FirstSession": "0",
    "OptanonAlertBoxClosed": "2025-02-24T08:31:00.135Z",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Mon+Feb+24+2025+...",
    "SearchMode": "1",
    "VisitCount": "1",
    "__cf_bm": "YQ60smEL.bc8lhECTcjOas573J44QJ6OM7qpTIIhtEI...",
    "__cflb": "0H28vSBxxmVRpbspyL7N4hbiBY4yBgWctuY68552Wpm",
    "_cfuvid": "sgH6RHW3w9qUxzNH7IxBar9cOLvM1YQQymqphPqMlw0...",
    "anonUserId": "37f3f170-f289-11ef-8be1-039da3ed4716",
    "countryCode": "TR",
    "functionalConsent": "false",
    "hvtb": "1",
    "language": "tr",
    "performanceConsent": "false",
    "platform": "web",
    "storefrontId": "1",
    "targetingConsent": "false",
    "userid": "undefined"
}

session = requests.Session()
session.cookies.update(cookies)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive"
}

url = "https://www.trendyol.com"

response = session.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
data = []
products = soup.find_all("a", class_="item")
print("categories")
for product in products:
    tmp = {}
    title = product["aria-label"]
    image = product.find("img")["src"]
    link = product["href"]
    tmp["title"] = title
    tmp["image"] = image
    tmp["link"] = link
    data.append(tmp)

with open("categories.json", "w") as f:
    json.dump(data, f, indent=4)
