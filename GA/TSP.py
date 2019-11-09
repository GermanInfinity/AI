import numpy
import itertools
import random 
"""Genetic algorithm: 
    Chromosome/Individual; 
                        is a path, in this problem of length n number of cities
                        to ensure we visit cities only once.
    Gene; a city in path
    Fitness
    Rank
    Operations: Cross-over, Mutation
    Cull
    Goal"""
    
    
class City:
    def __init__(self, name, distance_list):
        self.name = name
        self.distance_list = distance_list #distance to other cities
 
class Citizen: 
    def __init__(self, city, path):
        self.city = city #Actua city
        self.path = path #list of cities
        
        
"""
    Description: Permutes cities other than start. Thus creating all 
                 possible paths. 
"""
def space_init(start_individual, all_individuals):
    
    """An individual is a path"""
    build = []
    for ele in all_individuals:
        if ele == start_individual: continue
        build.append(ele)
        
    build_list = list(itertools.permutations(build))
    global_space = []
    
    for ele in build_list:
        transfer = list(ele)
        path = [start_individual]
        for ele in transfer:
            path.append(ele)
        global_space.append(path)

    return global_space
            

def individual_init(path):
    initial_city = path[0]
    """Permute all possible paths to other cities"""
    build = []
    for ele in initial_city.distance_list:
        if ele == path[0].name: continue
        build.append(ele + ": " + str(initial_city.distance_list[ele])) 
    build_list = list(itertools.permutations(build))
    all_citizens = []
    for ele in build_list:
        citizen_path = ([path[0].name] + list(ele))
        all_citizens.append(Citizen(path[0], citizen_path))
        
    return all_citizens
    
def fitness(individual): 
    """Make algorithm fast. 
        Possible solutions could be evaluating the number of unique cities in a path, if
        they are all unique, assign a high score, meaning we've reached all the paths. 
        When calculating the fitness of the population this would take aboutt 
        20 * n^c; where c is the number of cities on the path and n is every city on 
        the path. 
        
    """
    """
        We should try a faster algorithm, but first it would be interesting to see how this
        works. 
    """
    unique_cities = []
    for city in individual.city_collection: 
        unique_cities.append(individual.city_collection.count(city))
    
    print (unique_cities)
    
    
""" Swaps out the city on the path of an individual for another random one """
#def mutation(individual):
    
"""
    name: GA_search
    Description: Does genetic algorithm on Travelling salesman problem.
    Inputs: state node, or start city and entire space to search for individuals. 
    Outputs:
"""
def GA_search(initial, space):
    """Make global space, and trim search space ot include 20 individuals"""
    search_space_range = len(space)
    pop = []
    for idx in range(int(search_space_range / 3)):
        citizen_batch = individual_init(space[random.randint(0, search_space_range-1)])
        for ele in citizen_batch: 
            pop.append(ele)
    print (type(pop[0]))
    """ Since we can have n! possible paths(individuals), 
        we choose only n/3 of those possible paths for the population.
    """
                             
    
    
    
    

    
def TSP(start_city, list_of_cities):
    #origin = citizen(total_citizens)
    ordered_path_search_space = space_init(start_city, list_of_cities)
    
    GA_search(start_city, ordered_path_search_space)
    
    
    """start_population = [idx for idx in range(len(global_space))]
    indexes = len(list_of_citizens)
    pick = len(space) / 2
    for ele in pick:
        if random.randint(0, pick)
        start_population.append(random.randint"""
    #all_cities = list_of_cities
    #GA_search(origin, all_cities)
    
    
if __name__ == "__main__":
    cityA = City("cityA", {"cityA": 0, "cityB": 10, "cityC": 15, "cityD": 20})
    cityB = City("cityB", {"cityA": 10, "cityB": 0, "cityC": 35, "cityD": 25})
    cityC = City("cityC", {"cityA": 10, "cityB": 0, "cityC": 35, "cityD": 25})
    cityD = City("cityD", {"cityA": 20, "cityB": 25, "cityC": 30, "cityD": 0})
    
    total_cities = [cityA, cityB, cityC, cityD]
    #Permutation - 3 * 2 * 1 
    #              2 * 3 * 1 
    #              2 * 1 * 3
    
    TSP(cityA, total_cities)