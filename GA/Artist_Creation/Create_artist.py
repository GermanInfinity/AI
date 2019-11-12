#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:05:09 2019

@author: ugoslight
"""

import random

HEAD_gene = ["from graphics import *", "\n", "win = GraphWin('Canvas', 350, 570)", "\n"]
TAIL_gene = ["win.getMouse()", "\n", "win.close()"]

def decider(circle_no, rec_no, poly_no):
        total_gene = {} #Figures to change/optimize
    
        circle_gene = []
        for idx in range(circle_no):
            
            circ1 = random.randint(0, 150)
            circ2 = random.randint(0, 349)
            circ_rad = random.randint(0, 349)
            
            circle_gene.append([circ1, circ2, circ_rad])
            
        
        rec_gene = []
        for idx in range(rec_no):
            
            rec1 = random.randint(0, 349)
            rec2 = random.randint(0, 569)
            rec3 = random.randint(0, 349)
            rec4 = random.randint(0, 569)
            
            rec_gene.append([rec1, rec2, rec3, rec4])
            
        poly_gene = []
        for idx in range(poly_no):
            poly1 = random.randint(0, 300)
            poly2 = random.randint(0, 300)
            
            poly3 = random.randint(0, 300)
            poly4 = random.randint(0, 300)
            
            poly5 = random.randint(0, 300)
            poly6 = random.randint(0, 300)
            
            
            poly_gene.append([poly1, poly2, poly3, poly4, poly5, poly6])
        
        total_gene = {"Circle": circle_gene, "Rectangle": rec_gene, "Polygon": poly_gene}
        return total_gene
    
    
def make_script(GENE): 
    all_lines = []
    for ele in GENE["Circle"]:
        line = "c=Circle(Point(" + str(ele[0]) + "," + str(ele[1]) + ")," + str(ele[2]) + ")"
        line2 = "c.draw(win)"
        all_lines.append(line)
        all_lines.append("\n")
        all_lines.append(line2)
        all_lines.append("\n")
        
    for ele in GENE["Rectangle"]:
        line = "r=Rectangle(Point(" + str(ele[0]) + "," + str(ele[1]) + ")," + "Point(" + str(ele[2]) + "," + str(ele[3]) + "))"
        line2 = "r.draw(win)"
        all_lines.append(line)
        all_lines.append("\n")
        all_lines.append(line2)
        all_lines.append("\n")
    
    for ele in GENE["Polygon"]:
        line = "p=Polygon(Point(" + str(ele[0]) + "," + str(ele[1])  + ")," + "Point(" + str(ele[2]) + "," + str(ele[3])  + ")," + "Point(" + str(ele[4])  + "," + str(ele[5]) + "))"  
        line2 = "p.draw(win)"
        all_lines.append(line)
        all_lines.append("\n")
        all_lines.append(line2)
        all_lines.append("\n")
        
    return all_lines
    
    
    

class Create_artist: 
    def __init__(self, name):
        self.name = name

        self.circle = random.randint(0, 20) 
        self.rec = random.randint(0, 20)
        self.poly = random.randint(0, 300)
        self.gene = decider(self.circle, self.rec, self.poly)
        self.script = HEAD_gene + make_script(self.gene) + TAIL_gene
        



    