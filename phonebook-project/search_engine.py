# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:15:03 2019

@author: ottil
"""

import requests
import sqlite3
import json 
import os
from math import sin, cos, atan2, sqrt
                
                
def main_function():
    choice = select_option() 
    while choice != 1 and choice != 2:
        print("Please enter a valid answer.")
        choice = select_option()
    if choice == 1:
        person_search_process()
    elif choice == 2:
        choice = type_or_name()
        while choice != 1 and choice != 2:
            print("Please enter a valid choice.")
            choice = type_or_name()
        if choice == 1:
            business_search_process_by_name()
        elif choice == 2:
            business_search_process_by_type()
          
def select_option():
    answer = input("Do you want to search for a person or business? ")
    if 'p' in answer:
        answer = 1
    elif 'b' in answer:
        answer = 2  
    return answer

def type_or_name():
    choice = ""
    while choice == "":
        choice = input("Enter name to search by business name and type to search by business type: ")
        if 'name' in choice:
            choice = 1
        elif 'type' in choice:
            choice = 2  
        else:
            choice = ""
    return choice 

        
def person_search_process():
    person_search = person_input()
    postcode_search = ""
    postcode_search = postcode_input()
    if postcode_search == "":
        result = person_query(person_search)
        if result == []:
            result_2 = person_alt_query(person_search)
            if result_2 == []:
                print("Unfortunately we could not find any matching results.")
            else:
                print("Unfortunately we could not find an exact match, but please find similar results below: ")
                print(result_2)
        else:
            print(result)
    elif postcode_search != "":
        result = person_query(person_search) 
        if len(result) == 1:
            search_lat, search_lng = convert_postcode(postcode_search)
            database_lat, database_lng = convert_database_long_lat_one(result)
            distance = distance_calculation_one_result(search_lat, search_lng, database_lat, database_lng, result)
            if determine_close(distance):
                print(result)
            else:
                print("The closest match is ", result)
        else:
            result_2 = person_alt_query(person_search)
            if len(result_2) > 0:
                search_lat, search_lng = convert_postcode(postcode_search)
                close_results = convert_database_long_lat_multiple(result_2, search_lat, search_lng)
                print("These results are close.", close_results)
            else:
                print("Unfortunately we could not find any matching results.")

def business_search_process_by_type():
    business_search = business_input()
    postcode_search = ""
    postcode_search = postcode_input()
    if postcode_search == "":
        result = business_query_type(business_search)
        if result == []:
            print("Unfortunately we could not find any matching results.")
        else:
            print(result)   
    elif postcode_search != "":
        result = business_query_type(business_search) 
        if len(result) == 1:
            search_lat, search_lng = convert_postcode(postcode_search)
            database_lat, database_lng = convert_database_long_lat_one_business(result)
            distance = distance_calculation_one_result_business(search_lat, search_lng, database_lat, database_lng, result)
            if determine_close(distance):
                print(result)
            else:
                print("No businesses found in that area, but here are some similar businesses: ", result)
        elif len(result) > 1:
            search_lat, search_lng = convert_postcode(postcode_search)
            close_results = convert_database_long_lat_multiple_business(result, search_lat, search_lng)
            if len(close_results) > 1:   
                print("These results are close.", close_results)
            else:
                print("Unfortunately we could not find any matching results.")
        else:
            print("Unfortunately we could not find any matching results.")   


def business_search_process_by_name():
    business_search = business_input()
    postcode_search = ""
    postcode_search = postcode_input()
    if postcode_search == "":
        result = business_query(business_search)
        if result == []:
            result_2 = business_alt_query(business_search)
            if result_2 == []:
                print("Unfortunately we could not find any matching results.")
            else:
                print("Unfortunately we could not find an exact match, but please find similar results below: ")
                print(result_2)
        else:
            print(result)   
    elif postcode_search != "":
        result = business_query(business_search) 
        if len(result) == 1:
            search_lat, search_lng = convert_postcode(postcode_search)
            database_lat, database_lng = convert_database_long_lat_one_business(result)
            distance = distance_calculation_one_result_business(search_lat, search_lng, database_lat, database_lng, result)
            if determine_close(distance):
                print(result)
            else:
                print("The closest match is ", result)
        else:
            result_2 = business_alt_query(business_search)
            if len(result_2) > 1:
                search_lat, search_lng = convert_postcode(postcode_search)
                close_results = convert_database_long_lat_multiple_business(result_2, search_lat, search_lng)
                print("These results are close.", close_results)
            else:
                print("Unfortunately we could not find any matching results.")    

    
def connect_database(database_name):
    try:
        conn = sqlite3.connect(database_name) 
        c = conn.cursor()
        return c
    except:
        return False

def check_db(db_path):
   if os.path.exists(db_path):
       return True
   else:
       return False

def person_input():
    search = input("Search by an individual's surname: ")
    return search 

def business_input():
    search = input("Enter business name or type of business: ")
    return search 

def postcode_input():
    postcode = input("Please enter the postcode(optional): ")
    return postcode

def person_query(person_search):
    c = connect_database("phonebook.db")
    c.execute(''' SELECT *
              FROM personal
              WHERE last_name LIKE ?''',(person_search,)
              )
    result = c.fetchall()
    c.close()
    return result

def business_query(business_search):
    c = connect_database("phonebook.db")
    c.execute(''' SELECT *
              FROM business
              WHERE business_name LIKE ?''',(business_search,)
              )
    result = c.fetchall()
    c.close()
    return result

def business_query_type(business_search):
    c = connect_database("phonebook.db")
    c.execute(''' SELECT *
              FROM business
              WHERE business_type LIKE ?''',(business_search,)
              )
    result = c.fetchall()
    c.close()
    return result

def person_alt_query(person_search):
    c = connect_database("phonebook.db")
    new_search_term = (person_search[:int(len(person_search)/2)] + "%").replace(' ', '')
    c.execute(''' SELECT *
              FROM personal
              WHERE last_name LIKE ? 
              ORDER BY last_name ASC''',(new_search_term,)
              )
    result_2 = c.fetchall()
    c.close()
    return result_2



def business_alt_query(business_search):
    c = connect_database("phonebook.db")
    new_search_term = (business_search[:int(len(business_search)/2)] + "%").replace(' ', '')
    c.execute(''' SELECT *
              FROM business
              WHERE business_name LIKE ? 
              ORDER BY business_name ASC''',(new_search_term,)
              )
    result_2 = c.fetchall()
    c.close()
    return result_2

def business_alt_query_type(business_search):
    c = connect_database("phonebook.db")
    new_search_term = (business_search[:int(len(business_search)/2)] + "%").replace(' ', '')
    c.execute(''' SELECT *
              FROM business
              WHERE business_type LIKE ? 
              ORDER BY business_type ASC''',(new_search_term,)
              )
    result_2 = c.fetchall()
    c.close()
    return result_2

def convert_postcode(search_postcode):
    endpoint_postcode = "https://api.postcodes.io/postcodes/"
    postcode = search_postcode.replace(' ', '')
    response = requests.get(endpoint_postcode + postcode)
    try:
        response.raise_for_status()
        data_postcode = response.json()
        search_lat = data_postcode['result']['latitude']
        search_lng = data_postcode['result']['longitude']
        return search_lat, search_lng
    except requests.exceptions.HTTPError as e:
        print(("Error") + str(e))
    
def convert_database_long_lat_multiple(result_2, search_lat, search_lng):
    close_results = []
    for item in result_2:
        database_long_lat = convert_postcode(item[5])
        if database_long_lat != None:
            database_lat = database_long_lat[0]
            database_lng = database_long_lat[1]
            distance_lng =  database_lng - search_lng
            distance_lat =  database_lat - search_lat
            a = (sin(distance_lat/2))**2 + cos(search_lat) * cos(database_lat) * (sin(distance_lng/2)) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1-a))
            distance = 6371 * c
            if distance < 10:
                close_results.append(item)
        else:
            pass
    return close_results

def convert_database_long_lat_multiple_business(result_2, search_lat, search_lng):
    close_results = []
    for item in result_2:
        database_long_lat = convert_postcode(item[4])
        if database_long_lat != None:
            database_lat = database_long_lat[0]
            database_lng = database_long_lat[1]
            distance_lng =  database_lng - search_lng
            distance_lat =  database_lat - search_lat
            a = (sin(distance_lat/2))**2 + cos(search_lat) * cos(database_lat) * (sin(distance_lng/2)) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1-a))
            distance = 6371 * c
            if distance < 10:
                close_results.append(item)
        else:
            pass
    return close_results
        
def convert_database_long_lat_one(result):
    endpoint_postcode = "https://api.postcodes.io/postcodes/"
    postcode = result[0][5]
    postcode = postcode.replace(' ', '')
    response = requests.get(endpoint_postcode + postcode)
    data_postcode = response.json()
    if response.status_code == 200:
        database_lat = data_postcode['result']['latitude']
        database_lng = data_postcode['result']['longitude']
        return (database_lat, database_lng)   
    
def convert_database_long_lat_one_business(result):
    endpoint_postcode = "https://api.postcodes.io/postcodes/"
    postcode = result[0][4]
    postcode = postcode.replace(' ', '')
    response = requests.get(endpoint_postcode + postcode)
    data_postcode = response.json()
    if response.status_code == 200:
        database_lat = data_postcode['result']['latitude']
        database_lng = data_postcode['result']['longitude']
        return (database_lat, database_lng)

def distance_calculation_one_result(search_lat, search_lng, database_lat, database_lng, result):
    search_postcode = result[0][5]
    database_long_lat = convert_postcode(search_postcode)
    if database_long_lat != None:
        database_lat = database_long_lat[0]
        database_lng = database_long_lat[1]
    else:
        print("Error")
    dlon = search_lng - abs(database_lng)
    dlat = search_lat - abs(database_lat)
    a = (sin(dlat/2))**2 + cos(search_lng) * cos(database_lng) * (sin(dlon/2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6371 * c
    return distance

def distance_calculation_one_result_business(search_lat, search_lng, database_lat, database_lng, result):
    search_postcode = result[0][4]
    database_long_lat = convert_postcode(search_postcode)
    if database_long_lat != None:
        database_lat = database_long_lat[0]
        database_lng = database_long_lat[1]
    else:
        print("Error")
    dlon = search_lng - abs(database_lng)
    dlat = search_lat - abs(database_lat)
    a = (sin(dlat/2))**2 + cos(search_lng) * cos(database_lng) * (sin(dlon/2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6371 * c
    return distance

def determine_close(distance):
    if distance < 5:
        return True



#main_function()

