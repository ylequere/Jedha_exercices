# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
class Math():
    def __init__(self):
        pass

    def square_root(self, number):
        return math.sqrt(number)
    
    def average(self, number_list):
        if not type(number_list) is list:
            print('Variable is not a list')
            return
        try:
            return (sum(number_list) / len(number_list))
        except:
            print('Values are wrong !')
            
    def even_odd(self, number):
        if not type(number) is int:
            print('Variable is not an int')
            return
        return 'even' if number % 2 == 0 else 'odd'
        
    def sum(self, number_list):
        if not type(number_list) is list:
            print('Variable is not a list')
            return
        try:
            return sum(number_list)
        except:
            print('Values are wrong !')
    
import statistics
class Imputer():
    
    def __init__(self, alist):
        self.alist = alist

    def avg(self):
        l = self.alist.copy()
        while None in l:
            l.remove(None)
        avg = sum(l) / len(l)
        
        l = self.alist.copy()
        for i in range(len(l)):
            if l[i] == None:
                l[i] = avg
        return l
    
    def median(self):
        l = self.alist.copy()
        while None in l:
            l.remove(None)
        med = statistics.median(l)
        l = self.alist.copy()
        for i in range(len(l)):
            if l[i] == None:
                l[i] = med
        return l
        