#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:05:09 2019

@author: ugoslight
"""

import random

def decider(circ_no, circ_rad, circ_cen1, circ_cen2, rec_no, recp1, recp2, recp3, recp4,
         pol_no, polp1, polp2, polp3, polp4, polp5, polp6):
        
        circle_line = []
        for idx in range(circ_no):
            line = "c=Circle(Point(" + str(circ_cen1) + "," + str(circ_cen2) + ")," + str(circ_rad) + ")"
            line2 = "c.draw(win)"
            circle_line.append(line)
            circle_line.append("\n")
            circle_line.append(line2)
            circle_line.append("\n")
            
        rec_line = []
        for idx in range(rec_no):
            line = "r=Rectangle(Point(" + str(recp1) + "," + str(recp2) + ")," + "Point(" + str(recp3) + "," + str(recp4) + "))"
            line2 = "r.draw(win)"
            rec_line.append(line)
            rec_line.append("\n")
            rec_line.append(line2)
            rec_line.append("\n")
            
        poly_line = []
        for idx in range(pol_no):
            line = "p=Polygon(Point(" + str(polp1) + "," + str(polp2) + ")," + "Point(" + str(polp3) + "," + str(polp4) + ")," + "Point(" + str(polp5) + "," + str(polp6) + "))"  
            line2 = "p.draw(win)"
            poly_line.append(line)
            poly_line.append("\n")
            poly_line.append(line2)
            poly_line.append("\n")
            
            
        return circle_line + rec_line + poly_line
    
def gene(circ_no, circ_rad, circ_cen1, circ_cen2, rec_no, recp1, recp2, recp3, recp4,
         pol_no, polp1, polp2, polp3, polp4, polp5, polp6):
        
        head_gene = ["from graphics import *", "\n", "win = GraphWin('Canvas', 350, 570)", "\n"]
        tail_gene = ["win.getMouse()", "\n", "win.close()"]
        body = decider(circ_no, circ_rad, circ_cen1, circ_cen2, rec_no, recp1, recp2, recp3, recp4,
         pol_no, polp1, polp2, polp3, polp4, polp5, polp6)
        
        return head_gene + body + tail_gene
    
class Create_artist: 
    def __init__(self, name):
        self.name = name
        self.circ_no = random.randint(0, 20)
        self.circ_rad = random.randint(0, 150)
        self.circ_cen1 = random.randint(0, 349)
        self.circ_cen2 = random.randint(0, 569)
        self.rec_no = random.randint(0, 20)
        self.recp1 = random.randint(0, 349)
        self.recp2 = random.randint(0, 569)
        self.recp3 = random.randint(0, 349)
        self.recp4 = random.randint(0, 569)
        self.pol_no = random.randint(0, 20)
        self.polp1 = random.randint(0, 300)
        self.polp2 = random.randint(0, 300)
        self.polp3 = random.randint(0, 300)
        self.polp4 = random.randint(0, 300)
        self.polp5 = random.randint(0, 300)
        self.polp6 = random.randint(0, 300)
        
        self.script = gene(self.circ_no, self.circ_rad, self.circ_cen1, self.circ_cen2,
                    self.rec_no, self.recp1, self.recp2, self.recp3, self.recp4,
                    self.pol_no, self.polp1, self.polp2, self.polp3, self.polp4, 
                    self.polp5, self.polp6)
        
        
    