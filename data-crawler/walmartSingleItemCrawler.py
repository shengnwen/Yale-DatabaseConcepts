__author__ = 'shengwen'

from bs4 import BeautifulSoup, NavigableString, SoupStrainer
import urllib2
import urllib
import re

def walmartSingleItemCrawler(link):
    soup = BeautifulSoup(urllib2.urlopen(link), 'html.parser')
    print soup.prettify()
    # name
    name = soup(class_ = re.compile("^js-product-heading"))[0].span
    print "1.Name:" + name.text
    price = soup(class_ = re.compile("^js-price-display"))[0].text
    print "2.Price" + price
    unitPrice = soup(class_ = re.compile("^unit-price-display"))[0].text
    print "3.unit price" + unitPrice
    img_src = soup(class_ = "product-image js-product-image js-product-primary-image")[0]['src']
    print "4.img_src:" + img_src
    print "5.About this item ==========="
    itemInfo = soup(class_ ="product-description-disclaimer-mweb")[0].text
    print itemInfo
    liItemInfo = soup(class_= "about-item-preview-text js-about-item-preview-text")[0]
    # print liItemInfo
    for li in liItemInfo:
        print "*" + li.text
    print "6. Rank ======"
    itemRank = soup(class_="Grid-col item-ranks")[0]
    print itemRank
    starRated = soup(class_ = "Grid mweb-snippet-stars")[0].find_all("i", class_="star star-rated")
    print "7. star review:"
    print "star " + str(len(starRated)) + " out of 5"
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



walmartSingleItemCrawler("http://www.walmart.com/ip/Senseo-Espresso-Roast-Ground-Coffee-Pods-16-count-3.92-oz/34111434?action=product_interest&action_type=title&item_id=34111434&placement_id=irs-2-m3&strategy=PWVAV&visitor_id&category=&client_guid=583b8fdd-ad11-49e9-b7c5-b0e055b65dc3&customer_id_enc&config_id=2&parent_item_id=16532763&parent_anchor_item_id=16532763&guid=29f4b942-ec8c-4e42-aec3-73718e3fb42a&bucket_id=irsbucketdefault&beacon_version=1.0.1&findingMethod=p13n")