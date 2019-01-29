# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:17:16 2019

@author: ottil
"""

import unittest
from ch4_OttilieWilliams import is_prime
import sys 

    
class prime_test(unittest.TestCase): #Testcase is a function in unittest.
    def test_prime(self):
        self.assertTrue(is_prime(sys.argv[1]))
    
if __name__ == '__main__':
    unittest.main()
        
