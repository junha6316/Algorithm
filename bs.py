import requests
import bs4

req = requests.get("https://www.naver.com")
html = req.text
print(html)

bs_obj = bs4.BeautifulSoup(html, 'html.parser')

ul = bs_obj.find("ul", {"class" : "an_l"})
lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    span = a_tag("span")