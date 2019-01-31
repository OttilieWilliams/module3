# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:01:01 2019

@author: ottil
"""

# TASK 1: Calculator version 1

#class Calculator(object):
#    def add(self, x, y):
#        total = float(x + y)
#        return total

# Calculator version 2
        
#class Calculator(object):
#    def add(self, x, y):
#        number_types = (int, float, complex)
#        if isinstance(x, number_types) and isinstance (y, number_types):
#            return x + y
#        else:
#            raise ValueError  
            
# Calculator version 3

class Calculator(object):
    def add(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance (y, number_types):
            return x + y
        else:
            raise ValueError  

calc = Calculator()
result = calc.add(2, 2)
print(result)
