from bs4 import BeautifulSoup
import requests
from sklearn.decomposition import sparse_encode

verb_req = input("What verb do you want to conjugate? ")

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = f"https://de.pons.com/%C3%BCbersetzung/deutsch-englisch/{verb_req.lower()}"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

spans_content = []

for td in soup.find_all("td"):
    spans_content.append(td.string)

ich = []
du = []
es = []
wir = []
ihr = []
sie = []

pronomen = [ich, du, es, wir, ihr, sie]

if len(spans_content) > 12:
    for p in pronomen:
        p.append(spans_content[0])
        p.append(spans_content[1])
        p.append(spans_content[2])
        spans_content.pop(2)
        spans_content.pop(1)
        spans_content.pop(0)
else:
    for p in pronomen:
        p.append(spans_content[0])
        p.append(spans_content[1])
        spans_content.pop(1)
        spans_content.pop(0)

for n in pronomen:
    print(n)

