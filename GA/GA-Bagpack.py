#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 00:11:05 2019

@author: Akwarandu Ugo Nwachuku

Assignment: Genetic Algorithm, Bagpack problem

Artificial Intelligence COMP 131
"""


from itertools import combinations
from random import shuffle 
import random
import operator 

NUM_ITEMS = 7
WEIGHT_THRESHOLD = 120
BASE_SCORE = 10
#GENERATION_X = 10
SIZE_OF_SEARCH_SPACE = 40


class item: 
    def __init__(self, name, weight, value):
        self.weight = weight
        self.value = value
        self.name =  name + ";     " + "Weight: " + str(self.weight) + " Value: " + str(self.value)

class Individual: 
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

"""
    Name: print_individual
    
    Description: Individuals are collection of items in a tuple.
                 Prints out all item weights and values.

    Arguements: Takes an individual - (item_1, item_2)
                Individual is a tuple of objects
"""
def print_individual(individual):
    
    if (type(individual) == int): 
        print ("Sorry, there's no individual here.")
        return

    print (" ---- This is an individual ----")
    ans = "\n"
    size_of_individual = len(individual.items)
    print ("Fitness:  " + str(individual.fitness) + "      Rank:  " + 
                                                          str(individual.rank))
    for i in range(size_of_individual):
        if (type(individual.items[i]) == int): continue
        ans += individual.items[i].name 
        ans += "\n"
    print (ans)
    
        
"""
    Name: fitness
    
    Description: Normalizes value of an individual
                 assigns a score of 0 to overweight individuals
                 assigns a score of 5 to individuals within accepted weight 
                 range
                 sums score plus normalized value to return total score
                    
    Arguements: Takes an individual - global_space[10]
    Returns:    Fitness score
"""
def fitness(indi):
    if (type(indi) == int): return
    size_of_individual = len(indi.items)
    total_weight = 0
    total_value = 0
    normalizer = 10
    for idx in range(size_of_individual):
        if (type(individual.items[idx]) == int): continue
        total_weight += (indi.items)[idx].weight
        total_value += indi.items[idx].value
      
    if total_weight > WEIGHT_THRESHOLD:
        score = 0
    else: 
        score = 5
      
    return score + (total_value/normalizer)


""" Name: cull
    Description: Culls population by given percentage
    Returns: New population
""" 
def cull(population, percent):
    
    border = int(len(population) * percent)

    for member in population: 
        if population.index(member) > border: 
            population[population.index(member)] = 0
            
   
"""
    Name: cross_over
    Description: combines an individuals genes with another individuals
                 the swap takes place from a random location in the chromosome
    Returns: new offspring
"""
def cross_over(individual_a, individual_b):
    #idx_swap is the position chosen to swap the genes, out of 7 positions
    idx_swap = random.choice(ITEMS_IDX) + 1
    offspring_items = []
    counter = 0
    end = 7
    
    for item in individual_a.items:
        if item == 0: 
            offspring_items.append(0)
        else: 
            offspring_items.append(1)
        if counter == idx_swap - 1:
            break
        counter += 1;
        
    for item in individual_b.items:
        if counter < end: 
            if item == 0: 
                offspring_items.append(0)
            else: 
                offspring_items.append(1)
        counter += 1;
        
    new_list = [0,0,0,0,0,0,0]
    for idx in range(7): 
        if offspring_items[idx] == 0: 
            new_list[idx] = offspring_items[idx]
        else: 
            new_list[idx] = ALL_ITEMS[idx]
            
    offspring = Individual(new_list, 0, 0)

    return offspring
   
"""
    Name: mutation
    Description: randomly flips on or off a gene in an individual
    Returns: mutated invidividual
"""
def mutation(member):
    
    if (type(member) == int): return
    
    mutate_gene = random.choice(ITEMS_IDX)
    
    if member.items[mutate_gene] == 0:
        member.items[mutate_gene] = ALL_ITEMS[mutate_gene]
    else: 
        member.items[mutate_gene] = 0
        


def strong_CV(population):
    size_of_pop = len(population)
    cross_lis = []
    for idx in range(size_of_pop/2):
        cross_lis.append(idx)
    shuffle(cross_lis)
    
    parenta_idx = random.randint(0, size_of_pop/2)
    parentb_idx = random.randint(0, 20)
    offspring = cross_over(search_space[parenta_idx], 
                                   search_space[parentb_idx])
    search_space[search_space.index(0)] = offspring
    
    
"""Global space - 
            Initial base to pick individuals for evolution for.
            Initial start of population history. 
            First generation.
   Search space - 
            Random selection of 40 individuals from global space
            
   Description: global_space is a list of tuples; 
                a tuple is an individual

"""
if __name__ == "__main__":
    global_space = [] #Search_space, gets updated 
    search_space = [] #Randomly selects 40 individuals from global_space
    """Initial population"""
    
    for i in range(1, NUM_ITEMS+1):
        for idx in range(len(list(combinations(ITEMS_IDX, i)))):
            if i == 3: continue #We don't collect 7 combination 3. 
            idx_items = list(combinations(ITEMS_IDX, i))[idx] #Making combination of indexs
            items_idx_list = [0,0,0,0,0,0,0]
            
            for ele in idx_items: 
                items_idx_list[ele] = 1 #Storing index of items that are there
            
            item_list = [0,0,0,0,0,0,0] #Actual item list
            for j in range(len(items_idx_list)): #Placing items in list for individual
                if items_idx_list[j] > 0:
                    item_list[j] = ALL_ITEMS[j]
                    
            member = Individual(item_list, 0, 0)#Put member in global_space
            global_space.append(member)
    
    for idx in range(SIZE_OF_SEARCH_SPACE):
        search_space.append(random.choice(global_space))
        
        
    print ("Please enter the number of search generations: ")
    GENERATION_X = int(input()) + 1
        
    generation = 1

    while generation != GENERATION_X: 
        #All boxes are unique 
        """Assign fitness to population"""
        for individual in search_space: 
            if (type(individual) == int): continue
            individual.fitness = fitness(individual)
            
        """Sort by order of fitness"""    
        search_space = sorted(search_space, key=operator.attrgetter('fitness'))
        
        """Rank population"""
        for idx in range(len(search_space)):
            search_space[idx].rank = len(search_space) - idx
        #Population now ordered from fittest to weakest
        search_space.reverse()
        
        """{Print Fittest individual}"""
        print ("The fittest individual after generation: " + str(generation))
        print_individual(search_space[0])
        print_individual(search_space[-1])
         
        generation += 1

    
