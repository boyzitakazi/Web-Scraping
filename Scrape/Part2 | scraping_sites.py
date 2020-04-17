# import library
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from requests import get

# grabing the sites
my_url = get('http://www.theparanormalguide.com/blog')
page   = soup(my_url.text, 'html.parser')

# grabing the containers
containers = page.find(id="115210324294380097-blog")

# grabing the article
contain = containers.find_all("div", {"class":"blog-post"})

# save to csv file
filename = "datafile.csv"
# open file | create file with mode 'w' it's mean write
f = open(filename, "w")
# title in csv file, use coma to give column
headers = "title_article, date_article\n"
# write out to file
f.write(headers)

#looping for all artocle
for article in contain:
	title = article.find('h2')
	date  = article.find('p')
	
	# convert to string
	title_mod = title.text.strip()
	date_mod = date.find("span").text.strip()

	# print to console
	print(title.text.strip())
	print(date.find("span").text.strip())

	# export to csv file & close
	f.write(title_mod.replace(",", "") + "," + date_mod + "\n")

f.close()