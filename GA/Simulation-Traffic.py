#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:49:40 2019

@author: ugoslight
    
        Timer testing the movement of object km/hr.
        Road length: 1 miles == 1.6 kilometers
        Car, 30 km/hr
        Traffic lights at 0.784 km and 0.7855
        ** Acceleration was barred to simplify simulation.

"""


LENGTH_OF_CAR = 0.0014

def light1(car_at_light, sign, secs):
    if sign == "Green":
        Car.move(car_at_light, secs)
        
    if sign == "Orange":
        Car.wait(car_at_light, secs)
        
    if sign == "Red":
        Car.stop(car_at_light, secs)
        
        
def light2(car_at_light, sign, secs):
    if sign == "Green":
        Car.move(car_at_light, secs)
        
    if sign == "Orange":
        Car.wait(car_at_light, secs)
        
    if sign == "Red":
        Car.stop(car_at_light, secs)
        
  
"""
    Description: Makes all the lane routes, and stores in a list of lists. 
    Complex: Speed 
"""
def make_lanes():
    
    lanes = []
    """ LANE 1: E -- > B """
    carEB = ""
    EB = []
    car_EB = []
    for idx in range(10):
        carEB = "carEB" + str(idx)
        EB.append(carEB)
    for ele in EB: 
        name = ele
        ele = Car(name,  LENGTH_OF_CAR * -EB.index(ele), 0.014, "Go", 'E', 'B')
        car_EB.append(ele)
        
    """ LANE 2: E -- > A """
    carEA = ""
    EA = []
    car_EA = []
    for idx in range(10):
        carEA = "carEA" + str(idx)
        EA.append(carEA)
    for ele in EA: 
        name = ele
        ele = Car(name, LENGTH_OF_CAR * -EA.index(ele), 0.014, "Go", 'E', 'A')
        car_EA.append(ele)

    """ LANE 3:  F -- > A """
    carFA = ""
    FA = []
    car_FA = []
    for idx in range(10):
        carFA = "carFA" + str(idx)
        FA.append(carFA)
    for ele in FA: 
        name = ele
        ele = Car(name,  LENGTH_OF_CAR * -FA.index(ele), 0.014, "Go", 'F', 'A')
        car_FA.append(ele)
    

    """ LANE 4:  F -- > C  """
    carFC = ""
    FC = []
    car_FC = []
    for idx in range(10):
        carFC = "carFC" + str(idx)
        FC.append(carFC)
    for ele in FC: 
        name = ele
        ele = Car(name, LENGTH_OF_CAR * -FC.index(ele), 0.014, "Go", 'F', 'C')
        car_FC.append(ele)
    
 
    """ LANE 5:  D -- > A  """
    carDA = ""
    DA = []
    car_DA = []
    for idx in range(10):
        carDA = "carDA" + str(idx)
        DA.append(carDA)
    for ele in DA: 
        name = ele
        ele = Car(name, LENGTH_OF_CAR * -DA.index(ele), 0.014, "Go", 'D', 'A')
        car_DA.append(ele)
    
    
    lanes.append(car_EB)
    lanes.append(car_EA)
    lanes.append(car_FA)
    lanes.append(car_FC)
    lanes.append(car_DA)
    return lanes

"""
    Description: This function moves all cars in lanes, a speed/second.
"""
def move(lanes):
    for line in lanes: 
        for ele in line: 
            if ele.state == "Go":
                ele.pos += ele.speed
            if ele.state == "Wait":
                ele.pos = ele.pos
            if ele.state == "Stop":
                ele.pos = ele.pos
                
    
    return lanes

"""
    Description: Switches the color of lights after number of seconds.
"""
def switch(sequence, seconds):
    if seconds % 5 != 0: return sequence
    
    for idx in range(len(sequence)): 
        if sequence[idx] == "Go": 
            sequence[idx] = "Wait"
            continue
        if sequence[idx] == "Wait": 
            sequence[idx] = "Stop"
            continue
        if sequence[idx] == "Stop": 
            sequence[idx] = "Go" 
        
    return sequence
        
    
"""
    Description: Returns position of all cars in lanes. 
"""
def pos_in_lanes(lane_list):
    lanes_pos = []
    for lane in lane_list:
        pos = []
        for ele in lane: 
            pos.append(round(ele.pos, 4))
        lanes_pos.append(pos)
    return lanes_pos
            
class Car: 
    def __init__(self, name, position, init_speed, state, origin, destination):
        self.name = name
        self.pos = position #Distance is 1.6 km
        self.speed = init_speed #0.0014 km/sec = 5km/hr
        self.state = state
        self.origin = origin
        self.dest = destination

        
        
if __name__ == "__main__":

    """Make lanes"""
    lanes = make_lanes()
    
    """Move cars in lanes"""
    lanes = move(lanes)
    for idx in range(55): 
        lanes = move(lanes)
    lanes_pos = pos_in_lanes(lanes)
    
     
    #until a car reaches 0.8km, stop lane in list
    #for ele in lanes: 
     #   if 0.8
    
    #check traffic lights for everyone
    #carry out instructions
    #INSTRUCTIONS = {TL_EB: ["Go", 5, "Wait", 5, "Stop", 5], TL_EA: ["Go", 5, "Wait", 5, "Stop", 5],
     #               TL_FA: ["Go", 5, "Wait", 5, "Stop", 5], TL_FC: ["Go", 5, "Wait", 5, "Stop", 5],
      #              TL_DA: ["Go", 5, "Wait", 5, "Stop", 5]}
    
    Seq_Instructions = ["Go", "Wait", "Stop", "Go", "Wait"]
    secs = 0
    
    while secs < 25: 
        
        for ele in lanes:
            for car in ele: 
                if car.pos >= 0.784 and car.pos <= 0.812:
                    #Find light for lane
                    light_no = lanes.index(ele)
                    
                    #Instruct cars on light in lane
                    car_no = ele.index(car)
                    for idx in range(car_no, len(ele)):
                        car.state = Seq_Instructions[light_no]
                    break
                        
        
        print (Seq_Instructions) 
        lanes_pos = pos_in_lanes(lanes)
        print (lanes_pos)
        
        lanes = move(lanes)
        Seq_Instructions = switch(Seq_Instructions, secs)
        print ("")
        secs += 1
     
                    
         
    
    
    