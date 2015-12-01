__author__ = 'shengwen'

from bs4 import BeautifulSoup, NavigableString, SoupStrainer
import urllib2
import urllib
import re

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
def meijerSingleItemCrawler(link):
    req = urllib2.Request(link, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    print soup.prettify()
    # name
    name = soup(class_ =("detail-title"))[0]
    print "1.Name:" + name.text
    # price = soup(class_ = re.compile("^js-price-display"))[0].text
    # print "2.Price" + price
    unitPrice = soup(class_ = re.compile("^detail-price"))[0].div
    print "3.unit price:" + unitPrice.text.strip()
    img_src = soup(id = "product-image")[0].img['src']
    print "4.img_src:" + img_src
    print "5.About this item ==========="
    print "5.1 product details:"
    itemInfo = soup(class_ ="show-more-container")[0].text.strip()
    print itemInfo
    print "5.2 features:"
    itemFeature = soup(class_ ="map-value")[0].text.strip()
    print itemFeature
    # liItemInfo = soup(class_= "about-item-preview-text js-about-item-preview-text")[0]
    # # print liItemInfo
    # for li in liItemInfo:
    #     print "*" + li.text
    print "6. Rank ======(No rank information for Meijer)"
    # itemRank = soup(class_="Grid-col item-ranks")[0]
    # print itemRank
    # starRated = soup(class_ = "Grid mweb-snippet-stars")[0].find_all("i", class_="star star-rated")
    # print "7. star review:"
    # print "star " + str(len(starRated)) + " out of 5"
    # print starRated.div
    # itemRank = soup(class_="Grid-col item-ranks")[0].find_all('span')
    # print itemRank[0] + "in" + ""
    # print itemRank[2] + "in"
    # for spanTag in itemRank:
    #     print spanTag.string
    # print itemRank
    # for rank in itemRank:
    #     # print rank.text
    #     for li in rank.li:
    #         print li.text



meijerSingleItemCrawler("https://www.meijer.com/product/grocery/bakery/clydes-glazed-rings-6-ct/t1/t1-865/t2/t2-9972/2033715906.uts")