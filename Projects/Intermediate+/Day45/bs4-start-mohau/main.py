from bs4 import BeautifulSoup

with open("website.html",encoding="utf8") as web_file:
    contents=web_file.read()

soup=BeautifulSoup(contents,"html.parser")

# all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading=soup.find(name="h1",id="name")
# print(heading)

# section_heading=soup.find(name="h3",class_="heading")
# print(section_heading)
# print(section_heading.getText())

# company_url=soup.select_one(selector="p a")
# print(company_url)

headings=soup.select(".heading")
print(headings)
   