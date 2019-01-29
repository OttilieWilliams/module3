# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:14:43 2019

@author: ottil
"""

# CHAPTER 2 - DATA VALIDATION
# the process of ensuring a programme operates on clean, correct, useful data.

# Whatever the user enters, it is always classed as int. 

# TASK 1: ASKING THE USER FOR INPUT

#age = input("What's your age? ")
#print(type(age))

## TASK 2: Use int to cast the age variable into an integer.

#age_int = int(input("What's your age? "))
#print(type(age_int))

## TASK 3: VALIDATING STRING CONTENT

#option = input("please input yes or no ").lower()
#print(option)

## TASK 4: VALIDATING STRING LENGTH

name = input("What is your name? ")

while len(name) > 5:    
    name = input("What is your name? ")
print("Your name is short enough to pass.")
#
## TASK 5: ARRANGING CODE INTO A LOGICAL ORDER

#print("***Choice***")
#print("1.Display my name")
#print("2.Display my age")
#print("3.Display my city")
#
#choice = int(input('What is your choice? '))
#
#while choice < 1 or choice > 3:
#    choice = int(input('What is your choice? '))    
#if choice == 1:
#    print("Ms Wu")
#elif choice == 2:
#    print("5 years old")
#elif choice == 3:
#    print("London")


## TASK 6: WHILE TRUE INPUT VALIDATION
   
## while True means until the user gives the right answer, 
## there will be an infinite loop
    
print("***Choice***")
print("1.Display my name")
print("2.Display my age")
print("3.Display my city")

choice = 0 

while True:
    try:
        while choice < 1 or choice > 3:
            choice = int(input("What is your choice? "))
        break
    except ValueError:
        print("Please type a number!")
if choice == 1:
    print("Ms Wu")
elif choice == 2:
    print("5 years old")
elif choice == 3:
    print("London")
        
# TASK 7: OOP USER INPUT VALIDATION

class Spam(object):
    def __init__(self, description, value):
        if not description or value <= 0:
            raise ValueError
        self.description = description 
        self.value = value

s = Spam('s', 1)
print(s.value)
    
class Spam(object):
    def __init__(self, description, value):
        assert description != ""
        assert value > 0
        self.description = description
        self.value = value

s = Spam('s  ', 1)
print(s.value)      
    
