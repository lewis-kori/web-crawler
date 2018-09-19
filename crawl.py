import requests 
from bs4 import BeautifulSoup 

def crawler(max_pages):
    pages=1
    while pages<=max_pages:
        url='http://quotes.toscrape.com/'
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,features="html5lib")
        for link in soup.findAll('a',{'class':'tag'}):
            href='http://quotes.toscrape.com/'+link.get('href')
            title=link.string
            #print(href)
            #print(title)
            page_info(href)
        pages+=1
def page_info(page_url):
    source_code=requests.get(page_url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,features="html5lib")
    for item in soup.findAll('span',{'class':'text'}):
        print(item.string)
    for author in soup.findAll('small',{'class':'author'}):
        print('by '+author.string)
crawler(1)
