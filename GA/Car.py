#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:49:40 2019

@author: ugoslight
    
        Timer testing the movement of object km/hr.
        Road length: 1 miles == 1.6 kilometers
        Car, 30 km/hr

"""

import time
import threading

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
        
    
def this_print_here(ans, ans2):
        print (ans)
        #x.stop()
        
def tester2():
   # time.sleep(1)
    while True:
        print ("Hey first")
    
    
def move(self):
        
        timePoint = time.time()
        curr_timePoint = timePoint
        
        while True:
            curr_timePoint += 1
            self.speed += self.acc
            self.pos = self.speed * (curr_timePoint - timePoint)
            
            
class Car: 
    def __init__(self, position, init_speed, acceleration, origin, destination):
        self.pos = position #Distance is 1.6 km
        self.speed = init_speed 
        self.acc = acceleration #0.00138889 km/sec2  = 5 km/hr2
        self.origin = origin
        self.dest = destination
        self.car_thread = threading.Thread(target=move, args=(self))
        
        
    def start(self, secs):
        def move(self, secs):
        
            timePoint = time.time()
            curr_timePoint = timePoint
           
            while True :    
                curr_timePoint += 1
                self.speed += self.acc
                self.pos = self.speed * (curr_timePoint - timePoint)
            
        self.car_thread = threading.Thread(target=move, args=(self, "HFHF"))
        
        """i = 0 
        while i < secs: 
            self.car_thread.start()
            i += 1"""
            #car_thread.start()
        
                    
        
    def road_stop(self, secs): 
        i = 0
        while i < secs:
            self.car_thread._stop()
            i += 1
        
            
    #def stop(self, secs):
        #time.sleep(secs)
        
        
            
        
if __name__ == "__main__":

    timePoint = time.time()
    car1 = Car(0, 0, 0.00138889, 'E', 'A')
    #car2 = Car(0, 0, 0.00138889, 'E', 'B')

    print ("Before intersection")
    print (car1.pos)
    #print (car2.pos)
    
    #Car.start(car1)
    print ("Start")
    Car.road_stop(car1, 5)
    print (car1.pos)
    Car.start(car1, 3)
    print (car1.pos)
    print ("Stop")
    """Intersection"""
    #Genetic Algo gives us light colors and speed. 
    
    #Light 1 - F -> A
    #Light 2 - F -> B and F -> C
    #Light 3 - E -> A and E -> B
    #Light 4 - D -> A
    
    
    #Light 1 - Green, 30 seconds
    #Light 2 - Red, 20 seconds
    #Light 3 - Red, 10 seconds
    #Light 4 - Green, 20 seconds
    
    #Loop through list of cars, find conditions

    """
    x = threading.Thread(target=light1, args=(car1, "Green", 10))
    x.start()
    
    y = threading.Thread(target=light2, args=(car2, "Red", 5))
    y.start()
    
    
    z = threading.Thread(target=light3, args=(car3, "Green", 10))
    z.start()
    
    w = threading.Thread(target=light4, args=(car4, "Stop", 20))
    w.start()"""

    print ("After intersection")
    print (car1.pos)
    #print (car2.pos)
