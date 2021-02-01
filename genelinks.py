import re
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.parse import urljoin

def test_link(link):
    print(f"link testing {link}")
    results = None
    try:

        results = requests.get(link, verify=False, timeout=10)

    except Exception as e:
        print(f"failed for request {link}")

    status_code = results.status_code if results is not None else "404"

    print(f'the link {link} ---> {status_code}')
def call_links_recursively(page_url,visited=set()):

    '''modified function to call internal links recursively '''
    internal_links = set()
    html_page = uReq(page_url)
    parsed_page = soup(html_page,"html.parser")

    for link in parsed_page.findAll("a"):
        link_url = link.attrs.get("href")

        if re.match(r"^/",link_url):
            # means it's an internal link

            full_path = urljoin('https://www.genenetwork.org/',link_url)
            if link not in visited:

                internal_links.add(full_path)

        elif  re.match(r'^http://',link_url):
            # external link
            full_path= link_url

        if link not in visited:
            visited.add(link)
            test_link(full_path)


    for link in internal_links:

        call_links_recursively(link,visited=visited)




def scraper_for_webpage(page_url):

    '''function for only links that starts with http '''
    html_page = uReq(page_url)
    parsed_page = soup(html_page, "html.parser")

    for link in parsed_page.findAll("a", attrs={"href": re.compile("^http://")}):
        print("calling internal_links")
        test_link(link.get("href"))


call_links_recursively("https://www.genenetwork.org/")