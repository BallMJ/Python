""" Webscraper which takes URL input and scrapes all links
within the webpage, then writes them to a text file for using/editing"""

import urllib
import sys
from bs4 import BeautifulSoup

# Creates and opens txt file to write wbescrape output to
x = open("links.txt", "w")

url = raw_input("Enter URL for link scraping: ")

# Checks is url contains the hypertext transfer protocol, and adds it if it doesn't 
if url[0] != "http://":
    url="http://"+url

# Assigning variables for scraping
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

# Running through all urls in webpage, and writing each one to txt file
for i in links:
    print >>x, i

print "Web Scraping complete! Output can be found in links.txt"
    
