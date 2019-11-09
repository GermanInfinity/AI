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
from itertools import combinations

colors = ["Go", "Wait", "Stop"]
a = list(combinations(colors, 5))