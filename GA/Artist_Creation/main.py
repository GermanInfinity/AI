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
import os 

def initial_population():
    all_artists = []
    
    artist_name = "Artist1"
    Artist1 = Create_artist(artist_name)
    
    artist_name = "Artist2"
    Artist2 = Create_artist(artist_name)
    
    artist_name = "Artist3"
    Artist3 = Create_artist(artist_name)
    
    artist_name = "Artist4"
    Artist4 = Create_artist(artist_name)
    
    artist_name = "Artist5"
    Artist5 = Create_artist(artist_name)
    
    artist_name = "Artist6"
    Artist6 = Create_artist(artist_name)
    
    artist_name = "Artist7"
    Artist7 = Create_artist(artist_name)
    
    artist_name = "Artist8"
    Artist8 = Create_artist(artist_name)
    
    artist_name = "Artist9"
    Artist9 = Create_artist(artist_name)
    
    artist_name = "Artist10"
    Artist10 = Create_artist(artist_name)
    
    all_artists.append(Artist1, Artist2, Artist3, Artist4, Artist5, \
                       Artist6, Artist7, Artist8, Artist9, Artist10)
    return all_artists 

if __name__ == "__main__":
    WSK = "WSK.jpg"
    
    """ES: Initialize, Rank, Cull, Crossover"""
    """Create 10 Artists"""
    #population = initial_population()
    artist_name = "build"
    Artist10 = Create_artist(artist_name, 0)

    """Write creation to .py file creation"""
    a = Display.Display(artist_name, Artist10.script)
    
    """Run .py file"""
    script = artist_name+".py"
    call(["python3", script])
    artwork = artist_name + ".jpg"
    
    """Save generated images"""
    a = image_diff(artwork, WSK)
    a.blackened_white()
    Artist10.fitness = a.compare()
    
    """Compute fitness"""
    print (Artist10.fitness)
    

    print ("DONE")