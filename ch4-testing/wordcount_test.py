# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:54:25 2019

@author: ottil
"""

from wordcount import wordcount
import unittest

class TestUnit(unittest.TestCase):
    def test_wordcount(self):
        self.assertDictEqual(
                {'foo':2, 'bar': 1}, wordcount('foo bar foo')
                )
        
    def test_check_wordcount(self): 
        with self.assertRaises(AttributeError):
            wordcount(1)

if __name__ == '__main__':
    unittest.main()
    
# Check that providing a string input produces an error