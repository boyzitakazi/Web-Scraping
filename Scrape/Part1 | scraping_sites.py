from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.jobs.id/lowongan-kerja?kata-kunci=It+Development')
soup = BeautifulSoup(page.text, 'html.parser')
if page.status_code == 200:
	div  = soup.find(id='job-ads-container')

article = div.findAll('h3')
for a in article:
	print("NAMA PERUSAHAAN : ", a.text,'\n')




