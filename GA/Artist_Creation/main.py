#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 05:06:18 2019

@author: ugoslight

GA - Artist optimizer
"""

from Create_artist import Create_artist
from subprocess import call 
from Display import Display
from image_diff import image_diff
import os, random, operator


def mutate(artist):

    for idx in range(len(artist.gene["Circle"])):
        num1 = artist.gene["Circle"][idx][1]
        num0 = artist.gene["Circle"][idx][0]
        num3 = artist.gene["Circle"][idx][3]
        num2 = artist.gene["Circle"][idx][2]
        artist.gene["Circle"][idx][0] = num1
        artist.gene["Circle"][idx][1] = num0
        artist.gene["Circle"][idx][2] = num3
        artist.gene["Circle"][idx][3] = num2
        
    for idx in range(len(artist.gene["Line"])):
        num1 = artist.gene["Line"][idx][1]
        num0 = artist.gene["Line"][idx][0]
        num3 = artist.gene["Line"][idx][3]
        num2 = artist.gene["Line"][idx][2]
        artist.gene["Line"][idx][0] = num1
        artist.gene["Line"][idx][1] = num0
        artist.gene["Line"][idx][2] = num3
        artist.gene["Line"][idx][3] = num2

    return artist
        
def crossover(artist1, artist2): 
    gene = {"Circle":"", "Line":""}
    pick = [artist1, artist2]
    artist_name = "Artist" + artist1.name[-1] + artist2.name[-1] 
    artist_offspring = Create_artist(artist_name, 0)
    num = random.randint(0,1)
    
    if num == 0:
        artist_offspring.circle = pick[num].circle
        artist_offspring.lin = pick[1].lin
        gene["Circle"] = pick[num].gene["Circle"]
        gene["Line"] = pick[1].gene["Line"]
        
    else: 
        artist_offspring.circle = pick[num].circle
        artist_offspring.lin = pick[0].lin
        gene["Circle"] = pick[num].gene["Circle"]
        gene["Line"] = pick[0].gene["Line"]
        
    artist_offspring.gene = gene
    
    return artist_offspring

def initial_population():
    all_artists = []
    
    artist_name = "Artist0"
    Artist1 = Create_artist(artist_name, 0)
    
    artist_name = "Artist1"
    Artist2 = Create_artist(artist_name, 0)
    
    artist_name = "Artist2"
    Artist3 = Create_artist(artist_name, 0)
    
    artist_name = "Artist3"
    Artist4 = Create_artist(artist_name, 0)
    
    artist_name = "Artist4"
    Artist5 = Create_artist(artist_name, 0)
    
    artist_name = "Artist5"
    Artist6 = Create_artist(artist_name, 0)
    
    artist_name = "Artist6"
    Artist7 = Create_artist(artist_name, 0)
    
    artist_name = "Artist7"
    Artist8 = Create_artist(artist_name, 0)
    
    artist_name = "Artist8"
    Artist9 = Create_artist(artist_name, 0)
    
    artist_name = "Artist9"
    Artist10 = Create_artist(artist_name, 0)
    
    all_artists.extend((Artist1, Artist2, Artist3, Artist4, Artist5, \
                       Artist6, Artist7, Artist8, Artist9, Artist10))
    return all_artists 


if __name__ == "__main__":
    WSK = "Artist00.png"
    gen = 0 
    
    """Create 10 Artists"""
    population = initial_population()

    while gen < 5: 
        """Evaluating fitness in population"""
        for artist in population: 
            Display.Display(artist.name, artist.script)
        
            """Run .py file"""
            script = artist.name+".py"
            call(["python3", script])
            artwork = artist.name + ".png"
        
            """Save generated images"""
            a = image_diff(artwork, artist.name, WSK, "WSK")
            a.blackened_white()
        
            """Compute fitness"""
            artist.fitness = a.compare()
        
        """Organized top to bottom, fittest at top"""    
        population = sorted(population, key=operator.attrgetter('fitness'))
        
        #Pick ten fittest 
        pool = population[:10]
        mating_seq = random.sample(range(0,10), 10)
        
        #Reproduce offspring, Keep offspring, Mutate offspring
    
        offspring1 = crossover(pool[mating_seq[0]], pool[mating_seq[1]])
        offspring2 = crossover(pool[mating_seq[2]], pool[mating_seq[3]])
        offspring3 = crossover(pool[mating_seq[4]], pool[mating_seq[5]])
        offspring4 = crossover(pool[mating_seq[6]], pool[mating_seq[7]])
        offspring5 = crossover(pool[mating_seq[8]], pool[mating_seq[9]])
    
        mut_spring1 = mutate(offspring1)
        mut_spring2 = mutate(offspring2)
        mut_spring3 = mutate(offspring3)
        mut_spring4 = mutate(offspring4)
        mut_spring5 = mutate(offspring5)
        
        population.extend((offspring1, offspring2, offspring3, offspring4, offspring5, \
                           mut_spring1, mut_spring2, mut_spring3, mut_spring4, mut_spring5))
        
        print ("Generation " + str(gen) + " has concluded.")
        gen += 1