# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:04:06 2019

@author: ottil
"""

class Person(object):
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def getDetails(self):
        print(self.name, self.age, self.gender)
        
    def changeName(self, newName):
        self.name = newName
    
    def tenpercentless(self, salary):
        newSalary = salary - (salary*0.9)

if __name__=='__main__':
    aminat = Person('Aminat', 23, 'female')
    aminat.getDetails()
    aminat.changeName("Aminat2")
    aminat.getDetails()