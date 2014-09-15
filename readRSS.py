# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 17:11:51 2014

@author: Regi John
"""

import feedparser

class SafewaySaleItem:
    pass
#    def __init__(self):
#        itemName = "" # Identified by title
#        itemThumbnail = "" # Identified by vertis_itemthumbimage
#        itemPrice = "" # Identified by vertis_price     
#        itemSaleStart = "" # Identified by vertis_psdate
#        itemSaleEnd = "" # Identified by vertis_edate       
    

# Get the RSS feed
rssFeed = feedparser.parse("http://weeklyspecials.safeway.com/rss.jsp?drpStoreID=1600&categories=all")

# Store the various categories on sale
# The structure used is {category:[saleitems]}
itemsOnSaleByCategory = dict()

# Extract each item and its details and insert into
# the appropriate category
for entry in rssFeed.entries:
    print entry
    # The category is stored in the "tags" field which is a list of dicts
    # The meaningful category is the first item in the list
    category = entry.tags[0]['term']
    if category not in itemsOnSaleByCategory:
        itemsOnSaleByCategory[category] = []
    
    # Create a new SafeSaleItem object, and fill in the fields
    newSaleItem = SafewaySaleItem()
    newSaleItem.itemName = entry.title # Identified by title
    newSaleItem.itemThumbnail = entry.vertis_itemthumbimage # Identified by vertis_itemthumbimage
    newSaleItem.itemPrice = entry.vertis_price # Identified by vertis_price     
    newSaleItem.itemSaleStart = entry.vertis_psdate # Identified by vertis_psdate
    newSaleItem.itemSaleEnd = entry.vertis_edate # Identified by vertis_edate
    newSaleItem.itemHTML_URL = entry.link # Typically something like http://weeklyspecials.safeway.com/rss/rssfeed/1600/55670/42952631
    itemsOnSaleByCategory[category].append(newSaleItem)
    
    print "***************\n"
    
for category, saleItems in itemsOnSaleByCategory.iteritems():
    print "CATEGORY", category, len(saleItems)
    for saleItem in saleItems:
        print repr(saleItem.itemName)
        # saleItem.itemThumbnail, saleItem.itemPrice, saleItem.itemSaleStart, saleItem.itemSaleEnd, saleItem.itemHTML_URL
            
