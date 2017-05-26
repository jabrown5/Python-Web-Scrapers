# to make http requests, must import libraries
import urllib2
# import beautiful soup
from bs4 import BeautifulSoup
# indicate the url you want to scrap
# getting an HTML doc that we will then parse w/ Beautiful Soup
response = urllib2.urlopen("https://www.poemhunter.com/poem/the-lily-2/")

# parsing the document using Beautiful Soup
# parsing gives us a moc object of the DOM
soup = BeautifulSoup(response, 'html.parser')


# # ------------------------
# # will print everything from the page you just scraped
# # print(soup.prettify())

# # will return an array of all the p tags
# pTags = soup.select('p')
# finalPoem = []

# for poem in pTags:
# 	print poem
# 	p = poem.getText() #will take out the text between the tags
# 	finalPoem.append(p)

# print finalPoem[1]

# # for poem in range(0,3):
# # 	finalPoem.append(poem)

# # run it in the terminal by typing command 'python nameOfFile.py'
# # ------------------------



# GET ALL THE LINKS

links = soup.select('a[href]')
allLinks = []

# loop through the links to get what you want
for l in links:
	link = l.get('href')
	allLinks.append(link)

print allLinks

