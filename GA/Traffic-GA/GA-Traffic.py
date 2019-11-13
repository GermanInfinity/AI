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
import operator
from Traffic_Simulation import Traffic_Simulation

SIGNS = ["Go", "Wait", "Stop"]

class Traffic_ord:
    def __init__(self, Signs, Fitness, Rank):
        self.sign = Signs
        self.fit = Fitness
        self.rank = Rank

def mutation(individual, signs):
    pos = random.randint(0,len(individual)-1)
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
        

def make_pool(pop_count, signs):
    count = 0 
    pool = []
    while count < pop_count: 
        one_indi = []
        for idx in range(5):
            a = random.choice(signs)
            one_indi.append(a)
            soln_indi = Traffic_ord(one_indi, 0, 0)
        pool.append(soln_indi)
        count += 1

    return pool
        
    
def print_pool(pool, attribute): 
    if attribute == 'sign':
        for ele in pool:
            if type(ele) == str:
                print ("")
                continue
            print (ele.sign)
            
    if attribute == 'fitness':
        for ele in pool:
            if type(ele) == str:
                print ("")
                continue
            print (ele.fit)
            
    if attribute == 'rank':
        for ele in pool:
            if type(ele) == str:
                print ("")
                continue
            print (ele.rank)
            
def rank_pool(pool):
    for ele in pool:
        ele.rank = pool.index(ele) + 1
    return pool
    
def cull(pool):
    for idx in range(len(pool)):
        if idx > len(pool) / 2: 
            pool[idx] = ""
    return pool    
        
def run():
    
    
    pool = make_pool(20, SIGNS)
    
    for child in pool: 
        trf = Traffic_Simulation(child.sign) #Fitness == Time for sim finish
        child.fit = trf.timer()
        
    #Rank
    ranked_pool = sorted(pool, key=operator.attrgetter('fit'))
    ranked_pool = rank_pool(ranked_pool)
  
    #Cull
    culled_pool = cull(ranked_pool)
    

    print_pool(culled_pool, 'rank')
    print ("End")
    
run()
