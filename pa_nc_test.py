#! python3

# lucky.py - Opens several Google search results.
import requests, sys, webbrowser, bs4

print('NC lookup...') # display text while downloading
res = requests.get('https://www.bbc.co.uk/sport/football/teams/norwich-city')
res.raise_for_status()

# Retrieve top search result links.
results_page = bs4.BeautifulSoup(res.text)

#Find the score element
test = results_page.select('#live-scores-index-container')
print(test)