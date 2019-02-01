# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:02:57 2019

@author: ottil
"""

import os
from sqlite3 import OperationalError
import unittest
from search_engine import *
from unittest.mock import patch 

class search_engine_test(unittest.TestCase): #Testcase is a function in unittest.
    def test_valid_path(self):
       self.assertTrue(check_db("phonebook.db"))
    
    def test_database_connection(self):
        self.assertIsNotNone(connect_database("phonebook.db"))
        
    def test_personal_search(self):
        with patch('builtins.input', return_value = "Menego"):
            self.assertIsNotNone(person_query("Menego"))
            self.assertIsInstance(person_query("Menego"), list)
            self.assertEqual(person_query("Menego"), [('Moll', 'Menego', '72 Jenifer Trail', 'London', 'England', 'WC2H 1AF', 'United Kingdom', '0644 543 2902')])
    
    def test_person_alt_query(self):
        with patch('builtins.input', return_value = "Men"):
            self.assertIsNotNone(person_query("Men"))
            self.assertIsInstance(person_query("Men"), list)
            self.assertEqual(person_alt_query("Men"), [('Geralda', 'MacGaughey', '28099 Grayhawk Alley', 'Brampton', 'England', 'NR34 0ND', 'United Kingdom', '0852 100 5874'), ('Maurine', 'MacPeice', '703 Lerdahl Place', 'Milton', 'England', 'NG22 0AN', 'United Kingdom', '0205 942 9228'), ('Denni', 'Mattia', '133 Westport Hill', 'Belfast', 'Northern Ireland', 'BT20 3AF', 'United Kingdom', '0389 178 8306'), ('Elton', 'McGunley', '80059 Northwestern Street', 'Edinburgh', 'Scotland', 'EH91 5AF', 'United Kingdom', '0303 738 7203'), ('Salomi', 'McGurk', '43777 Michigan Crossing', 'Bristol', 'England', 'BS41 8JF', 'United Kingdom', '0761 875 5654'), ('Eve', 'McHardy', '81630 Gina Place', 'Brampton', 'England', 'NR34 0ND', 'United Kingdom', '0879 946 5358'), ('Moll', 'Menego', '72 Jenifer Trail', 'London', 'England', 'WC2H 1AF', 'United Kingdom', '0644 543 2902')])
    
    def test_convert_postcode(self):
        self.assertEqual(convert_postcode("EC1A 7AJ"), (51.515524, -0.097917))
        self.assertRaises(requests.exceptions.HTTPError, convert_postcode("hello"), "hello")
    
if __name__ == '__main__':
    unittest.main()          

#    def test_personal_search(self):
#        with patch('builtins.input', return_value = "Menego"):
#            assert personal_name_search() == "[('Moll', 'Menego', '72 Jenifer Trail', 'London', 'England', 'WC2H 1AF', 'United Kingdom', '0644 543 2902')]"

#    @patch(personal_name_search.input)
#    def test_personal_search():
#        output = personal_name_search("Menego")
#        assert output == "[('Moll', 'Menego', '72 Jenifer Trail', 'London', 'England', 'WC2H 1AF', 'United Kingdom', '0644 543 2902')]"
     
