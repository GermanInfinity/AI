#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 23:28:31 2019

@author: ugoslight
"""

import operator 
"""
    Problem: Implementation of the UCS algorithm on the pancake problem
    Assignment: The Pancake problem
    Author: Ugo Nwachuku
    Date: 21st July, 2019
"""

class Pancake_stack:
    def __init__(self, stack, cost, backward_cost, pos):
        self.stack = stack
        self.cost = cost
        self.backward_cost = backward_cost
        self.pos = pos

    
"""
    Name: forward_cost
    Description: Calculates the forward cost of a state. (Number of gaps)
    Input: Stack of pancakes
    Output: Cost function score
"""
def forward_cost(stack):
    gaps = 0
    for idx in range(len(stack)):
        if abs(stack[idx + 1] - stack[idx]) > 1: gaps += 1
        if idx == len(stack) - 2: return gaps #This prevents from going out of range
        
    """ CHECK SHAPE OF STACK  add 1 to cost if not in right order. """
    

"""
    Name: flips
    Description: Flips the pancake at position specified. 
                 Flipping topmost pancake is position 1, flipping all pancakes
                 is flipping from position 5. 
    Input: Stack of pancakes and position to flip from
    Output: flipped stack
"""    
def flip(stack, pos):
    
    if pos > 5: 
        print ("No flip")
        return
    if pos < 1: 
        print ("No flip")
        return 
    
    size_of_stack = len(stack)
    rotate = []
 
    for idx in range(size_of_stack - pos, size_of_stack):
        rotate.append(stack[idx])
    
    flipped = rotate[::-1]    
    final_stack = []
    
    for idx in range(0, size_of_stack - pos):
        final_stack.append(stack[idx])
        
    for idx in range(0, len(flipped)):
        final_stack.append(flipped[idx])
    
    return final_stack
                


if __name__ == "__main__":
    
    """origin = []
    while len(origin) != 5:
        print ("Please input pancake at position", + (len(origin) + 1))
        inp = int(input())
        if inp in origin: 
            print ("That pancake is already in the list, please try again.")
            continue
        if inp > 5 or inp < 1: 
            print ("We don't have pancakes that size. Sorry!")
            continue
        origin.append(inp)"""
    

    solution = []
    origin = [3, 2, 1, 4, 5]
    start_stack = Pancake_stack(origin, 0, 0, 0)
    solution.append(start_stack)
    """Test: test algorithm works with different arrangements of stacks."""
    
    frontier = []
    visited = [] 
    frontier.append(start_stack)
    #visited.append(start_stack)


    not_found = True
    count = 0
    
    """    Start search    """
    while not_found: 
        count += 1
        if len(frontier) == 0: 
            print ("Failure")
            break 
        
        working_stack = frontier[0]
        visited.append(frontier[0])
        del frontier[0]
        
        #if len(frontier) > 1: 
         #   print (frontier[0].stack)
  
        """Goal check: a combination that has no gaps in it and is arranged 
                   in this order: [5, 4, 3, 2, 1]"""
        if forward_cost(working_stack.stack) == 0 and working_stack.stack[0] == 5:
            not_found = False
            break

        
        """ Node Expansion 
            Description: A pancake stack arranged in this order; 
                                     [5, 4, 3, 2, 1] 
                         has the biggest pancake(5) in the 0th index.
                         Flips occur between pancakes, the first flip 
                         occuring between index 4 and 3 of the pancake list
                         (spatula below topmost pancake). 
                         
                         Starts flipping from the second position, to avoid
                         creating an identical stack.
        """
        frontier = []
        for idx in range(2, 6):
            """ Generate children by flipping """
            flip_return = flip(working_stack.stack, idx)
            child = flip_return
            
            """This assigns greater backward costs to flipping only few pancakes"""
            """So reward flipping more pancakes."""
            if idx == 2: bc = 4
            if idx == 3: bc = 3
            if idx == 4: bc = 2
            if idx == 5: bc = 1
            
            backward_cost = working_stack.backward_cost + bc
            cost = backward_cost
            
            expanded_node = Pancake_stack(child, cost, backward_cost, idx)
            
            child_in_frontier = False
            child_in_visited = False
            

            """ Do checks """
                    
            """If child is not in frontier or visited """
            for ele in frontier: 
                if ele.stack == expanded_node.stack: 
                    child_in_frontier = True
                    if ele.cost > expanded_node.cost:
                        frontier[frontier.index(ele)] = expanded_node
                    
            for ele in visited: 
                if ele.stack == expanded_node.stack: 
                    child_in_visited = True

                    

            if (child_in_frontier == False) and (child_in_visited == False):
                frontier.append(expanded_node)
                child_in_frontier = True
                 

        """  Arrange frontier in order of cost """
        frontier.sort(key=operator.attrgetter('cost'))
        solution.append(frontier[0])
        

    if not_found == False:
        soln = "Pancake stack found. " + str(working_stack.stack)
        for idx in range(1, len(solution)):
            print ("Flip " + str(solution[idx - 1].stack) + " at position " + str(solution[idx].pos))
        print ("After the final flip, we end up with: " + str(solution[-1].stack))
        print (count)
 
        
    