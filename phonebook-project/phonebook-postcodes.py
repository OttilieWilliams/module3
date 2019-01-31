# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:52:12 2019

@author: ottil
"""

import sqlite3
import json 
import requests


conn = sqlite3.connect('phonebook.db') 
# This connects to the database.

c = conn.cursor()
# link your database with cursor.


# CREATING THE POSTCODE DATABASE

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS postcodes (postcode TEXT, longitude REAL, latitude REAL)''')
    

# ADDING ALL THE POSTCODES FROM THE PERSONAL DATABASE
def personal_postcode_data_entry():
    c.execute('''SELECT postcode FROM personal''')
    for row in c.fetchall():
        current_postcode = row[0]
        c.execute('''SELECT * FROM postcodes WHERE postcode = ? ''', (current_postcode,))
        results = c.fetchall()
        if len(results) < 1:
            endpoint_postcode = "https://api.postcodes.io/postcodes/"
            postcode = current_postcode.replace(' ', '')
            response = requests.get(endpoint_postcode + postcode)
            data_postcode = response.json()
            if response.status_code == 200:
                print(data_postcode['result']['longitude'], data_postcode['result']['latitude'])
                lat = data_postcode['result']['latitude']
                lng = data_postcode['result']['longitude']
                c.execute('''INSERT INTO postcodes (postcode, longitude, latitude) VALUES(?, ?, ?)''', (current_postcode, lng, lat, ))
                conn.commit()
        else:
            print('got it already')
    
# ADDING ALL THE POSTCODES FROM THE BUSINESS DATABASE

def business_postcode_data_entry():
    c.execute('''SELECT postcode FROM business''')
    for row in c.fetchall():
        current_postcode = row[0]
        c.execute('''SELECT * FROM postcodes WHERE postcode = ? ''', (current_postcode,))
        results = c.fetchall()
        if len(results) < 1:
            endpoint_postcode = "https://api.postcodes.io/postcodes/"
            postcode = current_postcode.replace(' ', '')
            response = requests.get(endpoint_postcode + postcode)
            data_postcode = response.json()
            if response.status_code == 200:
                print(data_postcode['result']['longitude'], data_postcode['result']['latitude'])
                lat = data_postcode['result']['latitude']
                lng = data_postcode['result']['longitude']
                c.execute('''INSERT INTO postcodes (postcode, longitude, latitude) VALUES(?, ?, ?)''', (current_postcode, lng, lat, ))
                conn.commit()
        else:
            print('got it already')
    
    


              
              
              


