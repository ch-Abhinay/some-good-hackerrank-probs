from bs4 import BeautifulSoup
import requests
req= requests.get('https://www.google.com/search?q='+input('search:'))
soup= BeautifulSoup(req.text,'html.parser')
link= soup.find_all('a')
available_links=[]
for i in link:
    if 'wikipedia' in i['href']:
        rawlink=i['href']
        available_links.append(rawlink[rawlink.index('=')+1:rawlink.index('&')])
if len(available_links)>0:
    req1= requests.get(available_links[0]).text
    soup1= BeautifulSoup(req1,'html.parser')
    paras= soup1.find_all('p')
    print(paras[0].text)
    print(paras[1].text)