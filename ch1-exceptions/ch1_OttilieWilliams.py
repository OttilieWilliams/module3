# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:21:19 2019

@author: ottil
"""
import math

# CHAPTER 1: EXCEPTIONS AND VALIDATIONS

f = open('testfile') # This gives the error: 'No such file or directory'

## Use 'try' or 'except' to give a clear error message:

try: # Within the try block you are trying some code.
    f = open('testfile')
except Exception: # If it is incorrect the code will go to the exception block.
    print('This file does not exist, or the file name is wrong. Please try again.')

# Distinguishing between errors
    
try:
    f = open('testfile.txt')
    s1 = not_exists
except FileNotFoundError:
    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')

# Using a more specific exception like FileNotFoundError
# means that the undefined variable issue is spotted. 
    
# Examples of different error types:
    
 print(math.sqrt(-1)) # ValueError
 1 + 2 + 'three' # TypeError 
 1/0 # ZeroDivisionError
 For i in range(5) #SyntaxError
    
try:
     f = open('testfile.txt')
     s1 = not_exists
except FileNotFoundError:
    print('Sorry, this file does not exist, or the file name is wrong.')
except Exception:
    print('Sorry. Something is wrong after opening Function. ')
    
# TASK 1: Exception as e

try:
    f = open('testfile.txt')
    s1 = not_exists
except Exception as e:
    print(e) # e is a variable that represents anything wrong. 

# TASK 2: the ELSE clause

# the else clause will be printed if the try block does not raise an exception.

try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
    
# TASK 3: the FINALLY clause

# The finally block will run regardless of whether the try block is successful.

try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally...')

try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally...')
    
# Manually raising an exception

try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
except Exception as e:
    print('File names are the same')









    
    

    
    
