# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:14:30 2019

@author: ottil
"""

import sqlite3
import json 

conn = sqlite3.connect('phonebook.db') 
# This connects to the database.

c = conn.cursor()
# link your database with cursor.

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS business (business_name TEXT, addressline1 TEXT, addressline2 TEXT, addressline3 TEXT, postcode TEXT, country TEXT, telephone_number REAL, business_type TEXT)')
 

def business_data_entry():
    with open('business_database_json.js') as f:
        data = json.load(f)
        for item in data:
            values_list = list(item.values())
            c.execute('''INSERT INTO business(business_name, addressline1, addressline2, addressline3, postcode, country, telephone_number, business_type)
                      VALUES(?,?,?,?,?,?,?,?)''', (values_list))
            conn.commit()

def find_data_for_business_name_and_location():
    business_name = input('Please search by business name: ')
    addressline2 = input('Please search by city, town or village: ')
    c.execute('SELECT * FROM business WHERE business_name = ? and addressline2 = ? ', (business_name.title(),addressline2.title(),))

    results = c.fetchall()
    if results: # (means if results == true)
        print(len(results), 'result found')
        # to do: create 2 lists - results exact and results almost. Then work out a way to return results and sort
        
        for row in results: # For each row in results (that fulfil if statement), print the following data:
            print(row[0], row[1] + '\n' + row[2] + '\n' + row[3] + '\n' + row[5] + '\n' + row[6])
    else:
        print('Business not found.')


find_data_for_business_name_and_location()

#create_table()
#business_data_entry()
















#c.execute(
#        '''INSERT INTO phonebook
#        (name, addressline1, city, postcode, telephone_number, business_type, xcoordinate, ycoordinate)
#        VALUES 
#        ('Smith', '1 London Rd', 'London', 'L1 123', 0123, 'Tech', 1, 1),
#        ('Williams', '1 London Rd', 'London', 'L1 123', 0123, 'Tech', 1, 1);
#        '''
#        )    
#conn.commit() # similar to git, commit after inserting values


#create_table()
#data_entry(1,2,3,4,5,6,7,8)
#data_entry('Smith', '1 Smith St', 'London', 'L1 123', '0123456789', 'Florist', '1', '1')



#c.close() # close the table 
#conn.close() # close the connection to the database




