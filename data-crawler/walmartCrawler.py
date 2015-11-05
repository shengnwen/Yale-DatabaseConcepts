__author__ = 'shengwen'

from bs4 import BeautifulSoup, NavigableString, SoupStrainer
import urllib2
import urllib
import re


link = "http://www.walmart.com/cp/food/976759"
soup = BeautifulSoup(urllib2.urlopen(link), 'html.parser')
print soup.prettify()
linksToFoodType = soup.find_all("a", class_='lhn-menu-toggle lhn-menu-arrow')
print "This is all type from Walmart"
foodSubType = {}
for foodType in linksToFoodType:
    print foodType['data-name'] + ", href:" + foodType['href']
    subTypes = soup.find_all("a", attrs={"data-uid": re.compile("^" + foodType['data-target-id'] + "")})
    #print 'subtypes:'+"data-uid=" + foodType['data-target-id']
    #print subTypes[0]['data-name']
    foodSubType[foodType['data-name']] = []
    for sub in subTypes:
        foodSubType[foodType['data-name']].append(sub['data-name'])
for key in foodSubType.keys():
    print "====Type:" + key + ":========"
    subs = foodSubType[key]
    for sub in subs:
        print sub

