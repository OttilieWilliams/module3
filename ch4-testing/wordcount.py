# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:53:57 2019

@author: ottil
"""
word_counter = {}

def wordcount(words):
    for word in words.split():
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] +=1
    return(word_counter)
    
#print(wordcount(1))
        