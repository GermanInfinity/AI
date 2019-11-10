#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:18:31 2019

@author: ugoslight
"""

#Genetic Algoroithm
#population
#fitness function
#cross over
#mutation
#cull population

#Individual - ["Go", "Wait", "Stop", "Go", "Wait"]
import random

def mutation(individual, signs):
    pos = random.randint(0,len(individual)-1)
    print (pos)
    sign = random.choice(signs)
    individual[pos] = sign
    return individual

def cross_over(individual1, individual2):
    cutoff = random.randint(0,4)
    first_half = random.choice([individual1, individual2])
    if first_half == individual1: sec_half = individual2
    if first_half == individual2: sec_half = individual1
    child = first_half[0:cutoff] + sec_half[cutoff:len(individual1)]
    return child
        
signs = ["Go", "Wait", "Stop"]
def make_pool(pop_count, signs):
    count = 0 
    pool = []
    while count < pop_count: 
        one_indi = []
        for idx in range(5):
            a = random.choice(signs)
            one_indi.append(a)
        pool.append(one_indi)
        count += 1

    return pool
        
    
