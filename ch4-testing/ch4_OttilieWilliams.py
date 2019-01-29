# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:41:24 2019

@author: ottil
"""

# TASK 1: PRIME FUNCTIONS

## Return true if the number is prime
#def is_prime(number):
#    for num in range(number):
#        if number % num == 0:
#            return False
#    return True
#
#
## Print the closest prime number larger than *number*
#def print_next_prime(number):
#    index = number
#    while True:
#        index += 1
#        if is_prime(index):
#            print(index)

# TASK 3: FINAL VERSION OF PRIME FUNCTIONS

# Return true if the number is prime
def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True
#
## Print the closest prime number larger than *number*
def print_next_prime(number):
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
            break


        