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
