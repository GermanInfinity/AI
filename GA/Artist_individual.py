#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:58:56 2019

@author: ugoslight
"""

from graphics import *

win = GraphWin('My Circle', 100, 100)
c = Circle(Point(50,50), 10)
ca = Circle(Point(55,75), 10)
c.draw(win)
ca.draw(win)
win.getMouse()
win.close()