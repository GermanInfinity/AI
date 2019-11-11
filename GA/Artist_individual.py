#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:58:56 2019

@author: ugoslight
"""

from graphics import *

win = GraphWin('Canvas', 350, 570)

c = Circle(Point(100,50), 30)
c.draw(win)

req = Rectangle(Point(20, 560), Point(100, 10))
req.draw(win)

p = Polygon(Point(10,1), Point(50,3), Point(2,70))
p.draw(win)
    

win.getMouse()
win.close()