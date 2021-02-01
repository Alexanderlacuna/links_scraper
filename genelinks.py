import re
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup  as soup





def test_link(link):
	print(f"link testing {link}")
	results = None
	try:

		results= requests.get(link, verify=False, timeout=10)

	except Exception as e:
		print(f"failed for request {link}")

	# print(results.status_code)

	status_code = results.status_code if results is not None else  "404"
 
	print(f'the link {link}--->{status_code}')
html_page =uReq("https://www.genenetwork.org/")
# html_page.close()
soup =  soup(html_page,"html.parser")
for link in soup.findAll("a",attrs={'href': re.compile("^http://")}):
	# print(link.get('href'))
	test_link(link.get("href"))




def scraper_for_webpage(page_url):
	html_page = uReq("https://www.genenetwork.org/")
	parsed_page = soup(html_page,"html.parser")

	for link in parsed_page.findAll("a",attrs={"href":re.compile("^http://")}):
		print(link)
		test_link(link.get("href"))

