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
            self.assertIsNotNone(personal_name_search())
            self.assertIsInstance(personal_name_search(), list)
            self.assertEqual(personal_name_search(), [('Moll', 'Menego', '72 Jenifer Trail', 'London', 'England', 'WC2H 1AF', 'United Kingdom', '0644 543 2902')])

if __name__ == '__main__':
    unittest.main()          

#    def test_personal_search(self):
#        with patch('builtins.input', return_value = "Menego"):
#            assert personal_name_search() == "[('Moll', 'Menego', '72 Jenifer Trail', 'London', 'England', 'WC2H 1AF', 'United Kingdom', '0644 543 2902')]"

#    @patch(personal_name_search.input)
#    def test_personal_search():
#        output = personal_name_search("Menego")
#        assert output == "[('Moll', 'Menego', '72 Jenifer Trail', 'London', 'England', 'WC2H 1AF', 'United Kingdom', '0644 543 2902')]"
     
