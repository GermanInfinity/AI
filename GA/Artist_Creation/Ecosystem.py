#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 03:41:40 2019

@author: ugoslight
"""

class Ecosystem:
    def __init__(self, num_of_lines, fit):
        self.no = num_of_lines
        self.fitness = fit
        
        
    def populate_ecosystem(self):
        import numpy as np 
        import random
        
        x1 = np.arange(0,480,5).tolist()
        x2 = np.arange(0,360,5).tolist()
        y1 = np.arange(0,480,5).tolist()
        y2 = np.arange(0,360,5).tolist()
        
        self.script_nums = ()
        for idx in range(self.no): 
            citizen = [random.choice(x1), 
                       random.choice(y1),
                       random.choice(x2),
                       random.choice(y2),] #line
            self.script_nums += (citizen,) #Add line
            

    def people(self):
        return (self.script_nums)