k#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 04:02:55 2019

@author: ugoslight
"""

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
from Ecosystem import Ecosystem
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
    Goal = "Goal_image.png"
    gen = 0 
    
    """Create Ecosystem"""
    #Ecosystem of 3 lines
    pos_solution = []
    pos_solution.append(Ecosystem(3, 0)) 
    
    #Ecosystem of 5 lines
    #pos_solution.append(Ecosystem(5, 0))
    
    #Ecosystem of 7 lines
    #pos_solution.append(Ecosystem(7, 0))

    #Populate ecosystems with random numbers
    #Fill up # lines in script
    for ele in pos_solution: 
        ele.populate_ecosystem()


    """Create artist and script"""
    count = 1
    all_scripts = []
    
    #Developing script siwth Create Artist module
    #all_scripts == pos_solution, by index
    for ele in pos_solution:
        name = "Eco" + str(count)
        all_scripts.append(Create_artist(name, 0, ele.people()))
        count += 1
    
    #Running scripts 
    for artist in all_scripts: 
        Display.Display(artist.name, artist.script)
    
        """Run .py file"""
        script = artist.name+".py"
        call(["python3", script])
        artwork = artist.name + ".png"
        
        