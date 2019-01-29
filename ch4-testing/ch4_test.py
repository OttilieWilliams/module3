# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:51:19 2019

@author: ottil
"""

import unittest
from ch4_OttilieWilliams import is_prime
import sys 

# TASK 2 AND 3: TESTING THE PRIME FUNCTIONS
    
class prime_test(unittest.TestCase): #Testcase is a function in unittest.
        
    def test_is_prime(self):
        self.assertTrue(is_prime(5)) # Check if the function returns True
        self.assertFalse(is_prime(4)) # Check if the function returns False
        
    def test_is_zero_not_prime(self):
        self.assertFalse(is_prime(0)) # Check if 0 returns False
 
    # Is a negative number correctly determined not to be prime?     
    def test_negative_number(self):
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))
          
     # Check if the function returns the value specified in the second argument
    def test_checkPrime(self):
        self.assertEqual(is_prime(3), True)
        
    def test_checkPrime3(self):
        # Check that providing a string input produces an error
        with self.assertRaises(TypeError):
            is_prime('1')

if __name__ == '__main__':
    unittest.main()
    
    


        
