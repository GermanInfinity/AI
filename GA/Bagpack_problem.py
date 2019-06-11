#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 00:11:05 2019

@author: ugoslight

Goal: Make 7 individuals
Because we are culling by 50% we need find a balance between corss over and mutation
So that the population does not run extinct before we reach an optimal solution.

Keep going until we get optimal solution or we get pop == mating_pool

"""
"""Include in README and here, to make things fair, we consider all the 
   possible combinations of items in bagpack as our search space. 
   
   Mutation happens 100% of the time Crossover 80%
"""

from itertools import combinations
import random
import operator 

NUM_ITEMS = 7
WEIGHT_THRESHOLD = 120
BASE_SCORE = 10


class item: 
    def __init__(self, name, weight, value):
        self.weight = weight
        self.value = value
        self.name =  name + ";     " + "Weight: " + str(self.weight) + " Value: " + str(self.value)

class individual: 
    def __init__(self, items, rank, fitness):
        self.items = items
        self.rank = rank
        self.fitness = fitness
        
        
        
item_1 = item("Item_1", 20, 6)
item_2 = item("Item_2", 30, 5)
item_3 = item("Item_3", 60, 8)
item_4 = item("Item_4", 90, 7)
item_5 = item("Item_5", 50, 6)
item_6 = item("Item_6", 70, 9)
item_7 = item("Item_7", 30, 4)

ITEMS_IDX = [0, 1, 2, 3, 4, 5, 6]
ALL_ITEMS = [item_1, item_2, item_3, item_4, item_5, item_6, item_7]
#Even number of chromosomes even number of items per individual 
#Mutating don't replace with random item, instead give a good check 
#Number of individuals has to stay constant 

"""
    Name: print_individual
    
    Description: Individuals are collection of items in a tuple.
                 Prints out all item weights and values.

    Arguements: Takes an individual - (item_1, item_2)
                Individual is a tuple of objects
"""
def print_individual(individual):
    print (" ---- This is an individual ----")
    ans = "\n"
    size_of_individual = len(individual.items)
    print ("Fitness:  " + str(individual.fitness) + "      Rank:  " + str(individual.rank))
    for i in range(size_of_individual):
        if (type(individual.items[i]) == int): continue
        ans += individual.items[i].name 
        ans += "\n"
    print (ans)
    
#test_individual = individual((item_1, item_2), 0, 23)
#print (print_individual(test_individual))


"""A Population     
    is made up of a collection of individuals."""
#A population is a collection of individuals
#An individual is a collection of items in a tuple
#Individuals are of different sizes.
    


        
"""
    Name: fitness
    
    Description: Evaluates fitness of population; 
                by evaluating closeness of an individuals value to
                120. Values that equal 120 receive a score of ten, 
                Values that equal 0 receive a score of zero; negative
                numbers signify very unfit individuals. 
                The further a number is away from 120 the more negative
                the score. 
                
                i.e Individuals_value = 130
                    Fitness = 130 / 120 * 10 = 10.83
                    actul_fitness = 10 - (fitness - 10) = 9.17
                    
    Arguements: Takes an individual - global_space[10]
                Individual is a tuple of objects
"""
def fitness(individual):
    size_of_individual = len(individual.items)
    total_value = 0
    for idx in range(size_of_individual):
        total_value += individual.items[idx].value
        
    score = BASE_SCORE * total_value / GOAL_VALUE
    
    if score < BASE_SCORE:
        score = BASE_SCORE - (score - BASE_SCORE)
        
    return score

"""
    Name: cross_over
    Description: swaps out half of an individuals genes with another individuals
                 the swap takes place from a random location in the chromosome
    Returns: new offspring
"""
def cross_over(individual_a, individual_b):
    #idx_swap is the position chosen to swap the genes, out of 7 positions
    idx_swap = random.choice(ITEMS_IDX) + 1
    offspring_items = []
    counter = 0
    end = 7
    
    for ele in individual_a.items:
        offspring_items.append(individual_a.items)
        if counter == idx_swap - 1:
            break
        counter += 0;
        
    for ele in individual_b.items:
        if counter < end:
            offspring_items.append(individual_b.items)
        counter += 1;
    
    offspring = individual(offspring_items, 0, 0)
    return offspring
   
"""
    Name: mutation
    Description: if total weight is greater than 120, take out an item
                 if total weight is less than 120, find difference and add 
                 the most suitable item
    Returns: new offspring
"""
def mutation(individual):

    weight = 0
    weight_list = []
    for idx in range(len(individual.items)):
        weight += individual.items[idx].weight
        weight_list.append(individual.items[idx].weight)
    max_weight = max(weight_list)
    
    if weight > 120: 
        rem_idx = weight_list.index(max_weight)
        individual.items[rem_idx] = 0
    else:
        fill = WEIGHT_THRESHOLD - weight
        if fill <= 20:
            fill_index = individual.items.index(0)
            
            member = individual(ALL_ITEMS[0], 0, 0)
            individual.items[fill_index] = member
            
        elif fill > 20 and fill <= 30:
            fill_index = individual.items.index(0)
            possible_items = [1, 6]
            member = individual(ALL_ITEMS[random.choice(possible_items)], 0, 0)
            individual.items[fill_index] = member
            
        elif fill >= 50 and fill < 60:
            fill_index = individual.items.index(0)
            
            member = individual(ALL_ITEMS[4], 0, 0)
            individual.items[fill_index] = member
            
        elif fill >= 60 and fill < 70:
            fill_index = individual.items.index(0)
            
            member = individual(ALL_ITEMS[2], 0, 0)
            individual.items[fill_index] = member
            
        elif fill >= 70 and fill < 90:
            fill_index = individual.items.index(0)
            
            member = individual(ALL_ITEMS[5], 0, 0)
            individual.items[fill_index] = member
            
        elif fill >= 90:
            fill_index = individual.items.index(0)
            
            member = individual(ALL_ITEMS[3], 0, 0)
            individual.items[fill_index] = member
            
        
    
    
"""Global space - 
            Initial base to pick individuals for evolution for.
            Initial start of population history. 
            First generation.
   Description: global_space is a list of tuples; 
                a tuple is an individual
                global_space gets updated as the generations progress. 
"""
if __name__ == "__main__":
    global_space = [] #Search_space, gets updated 
    
    """Initial population"""
    
    for i in range(1, NUM_ITEMS+1):
        for idx in range(len(list(combinations(ITEMS_IDX, i)))):
            idx_items = list(combinations(ITEMS_IDX, i))[idx] #Making combination of indexs
            items_idx_list = [0,0,0,0,0,0,0]
            
            for ele in idx_items: 
                items_idx_list[ele] = 1 #Storing index of items that are there
            
            item_list = [0,0,0,0,0,0,0] #Actual item list
            for j in range(len(items_idx_list)): #Placing items in list for individual
                if items_idx_list[j] > 0:
                    item_list[j] = ALL_ITEMS[j]
                    
            member = individual(item_list, 0, 0)#Put member in global_space
            global_space.append(member)
            break
    print_individual(global_space[6])
    mutation(global_space[6])
    #evolving = True
    
    
        
        #"""Cross-over"""
        
       # """Mutation"""

    
        #pop_fitness = [] #Population in order of descending fitness
        #for individual in global_space:
            
       #     
       # """Cull population"""
    #
    #print(fitness(test_individual))
    


