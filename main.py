from bs4 import BeautifulSoup

with open("website.html", mode="r") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

print(soup.text)
print(soup.prettify())
print(soup.ul.li.text)

print(soup.find(name="h3", class_="heading").get_text())
print(soup.select_one(selector=".heading"))

print(soup.title)
print(soup.title.text)
print(soup.title.get_text())
print(soup.title.name)

print(soup.find_all("a"))

for i in soup.find_all("a"):
    print(i.get_text())
    print(i.get("href"))

print(soup.h1)
print(soup.h1["id"])
print(soup.h1.get_text())

print(soup.find(name="h1", id="name"))

print(soup.h3)
print(soup.find(name="h3", class_="heading"))
print(soup.h3["class"])

print(soup.body.p.em.a.get("href"))

print(soup.select_one(selector="p a"))
print(soup.select_one(selector="p a").get("href"))
print(soup.select_one(selector="p a").get_text())

print(soup.select(".heading"))