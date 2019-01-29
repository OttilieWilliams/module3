# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:15:38 2019

@author: ottil
"""

import sqlite3

def getdb():
    conn = pysqlite3.connect('')
    cursor = conn.cursor()
    return cursor

# Ruth's code

# returns all businesses in the database
def getBusinesses():
    db = getdb()
    query = "SELECT businessName, businessType, postcode, telephone FROM business"
    # execute the query
    db.execute(query)
    results = db.fetchall()
    # returns results
    return results   

# Code from our project

#def findBusiness(businessName, businessType, location):
#    search = input("Search by an individual's surname: ")
#    c.execute(''' SELECT *
#          FROM personal
#          WHERE last_name LIKE ?''',(search,)
#          )
#    result = c.fetchall()
#    if result != []:
#        print(result)
#    else:
#        new_search_term = (search[:int(len(search)/2)] + "%").replace(' ', '')
#        c.execute(''' SELECT *
#          FROM personal
#          WHERE last_name LIKE ? ''',(new_search_term,)
#          )
#        result_2 = c.fetchall()
#        print("We couldn't find anything matching your exact search, but here are some similar businesses:\n", result_2)
  
    