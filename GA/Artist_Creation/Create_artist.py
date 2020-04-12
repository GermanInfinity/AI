s#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:05:09 2019

@author: ugoslight

    Create artist module handles developing scripts to run for image.
    Takes in an array of numbers to create script with. 
"""

import random

HEAD_gene = ["from PIL import Image, ImageDraw", "\n", "image1 = Image.new('RGB', (480, 360), '#ffffff')", "\n"]
MID_gene = ["draw = ImageDraw.Draw(image1)", "\n"]

def decider(circle_no, lin_no):
        total_gene = {} #Figures to change/optimize
    
        circle_gene = []
        for idx in range(circle_no):
            
            circx1 = random.randint(0, 480)
            circy1 = random.randint(0, 360)
            circx2 = random.randint(0, 480)
            circy2 = random.randint(0, 360)
            
            circle_gene.append([circx1, circx2, circy1, circy2])
            
        
        line_gene = []
        for idx in range(lin_no):
            
            linx1 = random.randint(0, 480)
            liny1 = random.randint(0, 360)
            linx2 = random.randint(0, 480)
            liny2 = random.randint(0, 360)
            
            line_gene.append([linx1, linx2, liny1, liny2])
            
        total_gene = {"Circle": circle_gene, "Line": line_gene}
        
        return total_gene
    
    
    

# do the PIL image/draw (in memory) drawings

def make_script(GENE): 
    all_lines = []
    for ele in GENE["Circle"]:
        line = "c=[" + str(ele[0]) + "," + str(ele[1]) + "," + str(ele[2]) + "," + str(ele[3]) + "]"
        line2 = "draw.ellipse(c,'#ffffff','#000000')"
        all_lines.append(line)
        all_lines.append("\n")
        all_lines.append(line2)
        all_lines.append("\n")
        
    for ele in GENE["Line"]:
        line = "l=[" + str(ele[0]) + "," + str(ele[1]) + "," + str(ele[2]) + "," + str(ele[3]) + "]"
        line2 = "draw.line(l,'#000000')"
        all_lines.append(line)
        all_lines.append("\n")
        all_lines.append(line2)
        all_lines.append("\n")
    return all_lines
    
    
    
def make_eco_script(Genes):
    all_lines = []
    for ele in Genes:
        line = "l=[" + str(ele[0]) + "," + str(ele[1]) + "," + str(ele[2]) + "," + str(ele[3]) + "]"
        line2 = "draw.line(l,'#000000')"
        all_lines.append(line)
        all_lines.append("\n")
        all_lines.append(line2)
        all_lines.append("\n")
    return all_lines


class Create_artist: 
    def __init__(self, name, fitness, eco_people):
        self.name = name
        self.fitness = fitness
        #self.circle = random.randint(0, 20) 
        #self.lin = random.randint(0, 20)
    
        self.gene = eco_people
        
        image_name = ["image1.save('" + str(name) + ".png')"]
        
        self.script = HEAD_gene + MID_gene + make_eco_script(self.gene) + image_name
        



    