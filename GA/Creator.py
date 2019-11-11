#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:05:09 2019

@author: ugoslight
"""

with open("out.py", "w") as f1: 

    f1.writelines("from graphics import *")
    f1.writelines("\n")
    f1.writelines("win = GraphWin('My Circle', 100, 100)")
    f1.writelines("\n")
    f1.writelines("c = Circle(Point(50,50), 10)")
    f1.writelines("\n")
    f1.writelines("ca = Circle(Point(55,75), 10)")
    f1.writelines("\n")
    f1.writelines("c.draw(win)")
    f1.writelines("\n")
    f1.writelines("ca.draw(win)")
    f1.writelines("\n")
    f1.writelines("win.getMouse()")
    f1.writelines("\n")
    f1.writelines("win.close() ")
    f1.writelines("\n")
    f1.writelines("main()")