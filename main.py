import timeit
from requests import get
from qhttp import get as qget
import bs4
import re
from bs4 import BeautifulSoup

def get2():
    rq = get("https://google.com")
    with open("out1.html", "wb") as f:
        f.write(rq.content)
  

def get1():
    rq = qget("https://google.com")
    with open("out2.html", "wb") as f:
        f.write(rq.content)



print(timeit.timeit(get2, number=5))
print(timeit.timeit(get1, number=5))

orig_prettify = bs4.BeautifulSoup.prettify
r = re.compile(r'^(\s*)', re.MULTILINE)
def prettify(self, encoding=None, formatter="minimal", indent_width=4):
    return r.sub(r'\1' * indent_width, orig_prettify(self, encoding, formatter))
bs4.BeautifulSoup.prettify = prettify

with open("out1.html", "rb") as f:
    html = f.read()
bs = BeautifulSoup(html, 'html.parser')
with open("out1.html", "w") as f:
    f.write(bs.prettify(indent_width=4))
with open("out2.html", "rb") as f:
    html = f.read()
bs = BeautifulSoup(html, 'html.parser')
with open("out2.html", "w") as f:
    f.write(bs.prettify(indent_width=4))