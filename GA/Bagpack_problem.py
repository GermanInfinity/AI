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
GENERATION_X = 400
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
    
    if (type(individual) == int): 
        print ("Sorry, there's no individual here.")
        return

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
def fitness(indi):
    if (type(indi) == int): return
    size_of_individual = len(indi.items)
    total_weight = 0
    total_value = 0
    normalizer = 10
    for idx in range(size_of_individual):
        if (type(individual.items[idx]) == int): continue
        #print (type (indi.items[idx]))
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
    
    border = int(len(population) * percent * 0.01)

    for member in population: 
        if population.index(member) > border: 
            population[population.index(member)] = 0
            
   
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
    
    for item in individual_a.items:
        offspring_items.append(item)
        if counter == idx_swap - 1:
            break
        counter += 1;
        
    for item in individual_b.items:
        if counter < end:
            offspring_items.append(item)
        counter += 1;
    
    offspring = Individual(offspring_items, 0, 0)
    return offspring
   
"""
    Name: mutation
    Description: if total weight is greater than 120, take out an item
                 if total weight is less than 120, find difference and add 
                 the most suitable item
    Returns: new offspring
"""
def mutation(member):
    
    weight = 0
    weight_list = []
    
    if (type(member) == int): return
    
    for idx in range(len(member.items)):
        if (type(member.items[idx]) == int): continue
        weight += member.items[idx].weight
        weight_list.append(member.items[idx].weight)
        

    if len(weight_list) == 0: 
        member.items[random.choice(ITEMS_IDX)] =  random.choice(ALL_ITEMS)
        return
    
    max_weight = max(weight_list)

    if weight > 120: #Discard heaviest item
        rem_idx = weight_list.index(max_weight)
        member.items[rem_idx] = 0
        
    else:
        
        fill = WEIGHT_THRESHOLD - weight
        #Check distance from threshold, to select item to add. 
        
        if fill <= 20:
            
            fill_index = member.items.index(0)
            item_to_add = ALL_ITEMS[0]
            member.items[fill_index] =  item_to_add
            
            
        elif fill > 20 and fill <= 30:
            
            fill_index = member.items.index(0)
            
            possible_items = [1, 6] #Random choice between 2 items of weight = 30
            item_no = random.choice(possible_items)
            item_to_add = ALL_ITEMS[item_no]
            member.items[fill_index] = item_to_add
            
            
        elif fill >= 50 and fill < 60:
            
            fill_index = member.items.index(0)
            item_to_add = ALL_ITEMS[4]
            member.items[fill_index] = item_to_add
            
            
        elif fill >= 60 and fill < 70:
            
            fill_index = member.items.index(0)
            item_to_add = ALL_ITEMS[2]
            member.items[fill_index] = item_to_add
            
            
        elif fill >= 70 and fill < 90:
            
            fill_index = member.items.index(0)
            item_to_add = ALL_ITEMS[5]
            member.items[fill_index] = item_to_add
            
        elif fill >= 90:
            
            fill_index = member.items.index(0)
            item_to_add = ALL_ITEMS[3]
            member.items[fill_index] = item_to_add
            
    

    
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
    search_space = [] #Randomly selects 40 individuals from global_space
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
                    
            member = Individual(item_list, 0, 0)#Put member in global_space
            global_space.append(member)
    
    for idx in range(SIZE_OF_SEARCH_SPACE):
        search_space.append(random.choice(global_space))

        
        
    """Mutation test"""
    #print_individual(global_space[6])
    #mutation(global_space[6])
    #print ("After MUTATION")
    #print_individual(global_space[6])
    """Cross-over test"""
    #child = cross_over(global_space[30], global_space[4])
    #print ("Parent 1")
    #print_individual (global_space[3])
    #print ("Parent 2")
    #print_individual (global_space[4])
    #print ("Offspring")
    #print_individual (child)
    generation = 0 
    evolving = True
    while evolving and generation != GENERATION_X: 
        #All boxes are unique 
        """Assign fitness to population"""
        for individual in search_space: 
            if (type(individual) == int): continue
            individual.fitness = fitness(individual)
            
        #print_individual(global_space[6])
        """Sort by order of fitness"""    
        search_space = sorted(search_space, key=operator.attrgetter('fitness'))
        
        """Rank population"""
        for idx in range(len(search_space)):
            search_space[idx].rank = len(search_space) - idx
        #Population now ordered from fittest to weakest
        search_space.reverse()
        
        """{Print Fittest individual}"""
        print_individual(search_space[0])


 
        """Cull lower half of population"""
        cull_rate = 50
        cull(search_space, cull_rate)
        
        
        """Reproduction - 
                    Crossover 100% of the time. 
                    Mutate all the time and only 30% of population.
        """
     
        to_cross = random.choice([1,2,3,4,5,6,7,8,9,10])
        if to_cross <= 10:
            while True:
                try: search_space.index(0)
                except ValueError: break
                parenta_idx = random.randint(0, 20)
                parentb_idx = random.randint(0, 20)
                offspring = cross_over(search_space[parenta_idx], search_space[parentb_idx])
                search_space[search_space.index(0)] = offspring
                
        #print ("First of zeros:" + str(search_space.index(0)))
        #Mutation
        mutation_population = []
        portion_to_mutate = int(len(search_space) * 0.3)
        for idx in range(portion_to_mutate):
            mut_idx = random.randint(0, len(search_space)-1)
            mutation_population.append(mut_idx)
        for index in mutation_population: 
            mutation(search_space[index])
         
        #Pruning repetated items individuals
        for idx in range(SIZE_OF_SEARCH_SPACE):
            individuals_items = search_space[idx].items
            for ele in individuals_items:
                if ele == 0 :continue
                if individuals_items.count(ele) > 1 and ele != 0:
                    num_repeats = individuals_items.count(ele)
                    for y in range(num_repeats - 1):
                        individuals_items[individuals_items.index(ele)] = 0
                           
    
        
      
        generation += 1