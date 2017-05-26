# # to make http requests, must import libraries
# import urllib2
# import json
# # import beautiful soup
# from bs4 import BeautifulSoup
# # indicate the url you want to scrap
# # getting an HTML doc that we will then parse w/ Beautiful Soup
# response = urllib2.urlopen("http://nflarrest.com/api/v1/team/arrests/free")

# # parsing the document using Beautiful Soup
# # parsing gives us a moc object of the DOM
# soup = BeautifulSoup(response, 'html.parser')


# # # will print everything from the page you just scraped
# print(soup.prettify())



# from urlparse import urljoin

# import requests
# from bs4 import BeautifulSoup


# base_url = "http://nflarrest.com/api/v1/team/arrests/"
# response = requests.get(base_url)
# soup = BeautifulSoup(response.content, "html.parser")

# for link in soup.select("a.reference.internal"):
#     url = link["href"]
#     absolute_url = urljoin(base_url, url)

# # print(url, absolute_url)
# print(soup.prettify())



# import urllib2,sys
# from urllib2 import urlopen
# from bs4 import BeautifulSoup

# for numb in ('free', 'det'):
#     address = ('http://nflarrest.com/api/v1/team/arrests/' + numb)
#     html = urllib2.urlopen(address).read()
#     # soup = BeautifulSoup(address, 'html.parser')

# soup = BeautifulSoup(urlopen(html))

#     # title = soup.find("span", {"class":"paperstitle"})
#     # date = soup.find("span", {"class":"docdate"})
#     # span = soup.find("span", {"class":"displaytext"})  # span.string gives you the first bit
#     # paras = [x for x in span.findAllNext("p")]

#     # first = title.string
#     # second = date.string
#     # start = span.string
#     # middle = "\n\n".join(["".join(x.findAll(text=True)) for x in paras[:-1]])
#     # last = paras[-1].contents[0]

# print "%s\n\n%s\n\n%s\n\n%s\n\n%s" % (soup)
# # print(soup.prettify())



import urllib2,sys
from bs4 import BeautifulSoup

for team in ('min', 'den', 'cin', 'tb', 'ten', 'ind', 'jac', 'cle', 'chi', 'kc', 'mia', 'bal', 'lac', 'sea', 'sf', 'no', 'pit', 'gb', 'was', 'ari', 'car', 'oak', 'atl', 'ne', 'nyj', 'buf', 'det', 'phi', 'la', 'dal', 'nyg', 'hou', 'free'):
    address = ('http://nflarrest.com/api/v1/team/arrests/' + team)
    html = urllib2.urlopen(address).read()
    soup = BeautifulSoup(html, 'html.parser')

# soup = BeautifulSoup(response, 'html.parser')

    print (soup)

