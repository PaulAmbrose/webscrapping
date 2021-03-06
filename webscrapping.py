#Web scapping - using a program to download and process content from the web

#Modules:
    #1 webbrowser - opens a browser to a specific page
    #2 requests - Downloads files and web pages from the internet - NEVER USE urllib2!
    #3 beautiful soup - parsers HTML
    #4 selenium - launches and controls a web browser, Selenium is able to fill in and simulate mouse clicks

##1 
#import webbrowser
#webbrowser.open('http://google.com')

##2
#import requests
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
##res will be a response object which can be interrogated for various functionality, for instance the status code
##of the status code is "ok" the request was successful. Raise_for_status is best way to do this, error if an issue, ignores if fine
#try:
#    res.raise_for_status()
#    print(res.text[:250])
#except Exception as exc:
#    print("There was a problem: %s" %(exc))

##Note, always raise_for_status after making a .get() request to ensure the request was successful

##Next, to write the webpage to a file...
##need to write as binary
#playFile = open('RomeoAndJuliet.txt', 'wb')

#for chunk in res.iter_content(100000):
#    playFile.write(chunk)
#iter_content is another response object attribute which allows set chunks to be passed
#this ensures not too much memory is eaten up at a time, jamming the computer

#For more on requests see http://requests.readthedocs.org/

##3
#Downloading and passing to beautiful soup object
#import requests, bs4
#res = requests.get('http://nostarch.com')
#res.raise_for_status()
#noStarchSoup = bs4.BeautifulSoup(res.text)
#print(type(noStarchSoup))

#Opening an HTML file and passing to a beautiful soup object
#exampleFile = open('C:\\Users\\pablo\\Google Drive\\1_Paul\\code\\staging\\web_scraping\\webscrapping\\example_html.html')
#exampleSoup = bs4.BeautifulSoup(exampleFile)
#print(type(exampleSoup))

#Using the Beautifulsoup Object
#Table 11-2. Examples of CSS Selectors
#Selector passed to the select() method

# soup.select('div')
# All elements named <div>
# soup.select('#author')
# The element with an id attribute of author
# soup.select('.notice')
# All elements that use a CSS class attribute named notice
# soup.select('div span')
# All elements named <span> that are within an element named <div>
# soup.select('div > span')
# All elements named <span> that are directly within an element named <div>, with no other element in between
# soup.select('input[name]')
# All elements named <input> that have a name attribute with any value
# soup.select('input[type="button"]')
# All elements named <input> that have an attribute named type with value button


#Example downloading all from a website...using the prev button
#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

""" import requests, os, bs4

url = 'http://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
while not url.endswith('#'):
    #Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    #Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         try:
             comicUrl = 'http:' + comicElem[0].get('src')
             # Download the image.
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
         except requests.exceptions.MissingSchema:
             # skip this comic
             prevLink = soup.select('a[rel="prev"]')[0]
             url = 'http://xkcd.com' + prevLink.get('href')
             continue

         imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
         for chunk in res.iter_content(100000):
            imageFile.write(chunk)
         imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.') """

#4 Running a web browser using Seleium

#>>> from selenium import webdriver
#>>> browser = webdriver.Firefox()
#>>> type(browser)
#<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
#>>> browser.get('http://inventwithpython.com')