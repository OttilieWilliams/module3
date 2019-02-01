# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:14:40 2019

@author: ottil
"""

from search_engine import main_function, select_option, person_search_process, person_input, postcode_input, person_query

class TestEngine():
    
    def test_select_option(self):
        self.checked = select_option()
        print(self.checked)
        return self.checked
    
    def test_person_input(self):
        if self.checked == 1:
            print("Passed select option test, testing person_input.......")
            try:
                self.person_search = person_input()
                print("Passed person input test.")
                return self.person_search
            except:
                print("Failed Person INput Test..... Quiting program")
                return None
        else:

            print("Failed select option test.")
            return None
        
    def test_postcode_input(self):
        try:
            self.postcode_search = postcode_input()
            print("Passed postcode input test.")
            return self.postcode_search
        except:
            print("Failed postcode input test.")
            return None

    def test_person_query(self):
        try:
            person_query(self.person_search)
            print("Passed person query test.")
        except:
            print("Failed person query test.")
    
    def test_person_search_process(self):
        try:
            something = person_search_process()
            print("Passed person search process test.")
            return something
        except:
            print("Failed perseon search test, ending test.....")
            return None
    
    def run_tests(self):
        print(self.test_select_option())
        print(self.test_person_input())
        print(self.test_postcode_input())
        print(self.test_person_query())
        print(self.test_person_search_process())
    
if __name__ == '__main__':
    newTest = TestEngine()
    newTest.run_tests()
    
    