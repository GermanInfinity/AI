#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 05:52:59 2019

@author: ugoslight
    Module that compiles artist script.
"""

class Display: 
    def Display(name, script):
        with open(name + ".py", "w") as f1: 
            for line in script:
                f1.writelines(line)
        



