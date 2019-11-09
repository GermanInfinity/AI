import operator 
"""
    Problem: Implementation of A* Search
    Assignment: The Pancake problem
    Author: Ugo Nwachuku
"""

"""As a searching problem: 
   Forward Heuristic: Number of gaps
   Backward Heuristic: Number of pancakes to flip 
def backward_cost(stack):
"""  
class Pancake_stack:
    def __init__(self, stack, cost, backward_cost):
        self.stack = stack
        self.cost = cost
        self.backward_cost = backward_cost
    
"""
    Name: forward_cost
    Description: Calculates the forward cost of a state. 
    Input: Stack of pancakes
    Output: Cost function score
"""
def forward_cost(stack):
    gaps = 0
    for idx in range(len(stack)):
        if abs(stack[idx + 1] - stack[idx]) > 1: gaps += 1
        if idx == len(stack) - 2: return gaps #This prevents from goign out of range
        
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
    #start_stack = Pancake_stack([4, 2, 3, 1, 5], 0, 0)
    """Test: test algorithm works with different arrangements of stacks."""
    #start_stack = Pancake_stack([1, 5, 2, 4, 3], 0, 0)
    #start_stack = Pancake_stack([1, 5, 2, 4, 3], 0, 0)
    
    frontier = []
    visited = [] 
    frontier.append(start_stack)
    #frontier.append({"child": initial_state, "cost": forward_cost(initial_state) + 0,
                      #"backward_cost": 0})

    not_found = True
    count = 0
    
    """    Start search    """
    while not_found: 
        
        if len(frontier) == 0: 
            print ("Failure")
            break 
        
        working_stack = frontier[0]
        visited.append(frontier[0])
        del frontier[0]
        
        
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
        for idx in range(2, 6):
            #On next iteration start from 2. 
            
            """ Generate children by flipping """
            flip_return = flip(working_stack.stack, idx)
            child = flip_return
            
            backward_cost = working_stack.backward_cost + idx   #keep track of backward costs
            cost = forward_cost(child) + backward_cost
            
            expanded_node = Pancake_stack(child, cost, backward_cost)
            
            child_in_frontier = False
            child_in_visited = False
            
            """ Do checks """
            """If child is not in frontier or visited """
            for ele in frontier: 
                if ele.stack == expanded_node.stack: 
                    child_in_frontier = True
            if child_in_frontier == False: 
                frontier.append(expanded_node)
                
            for ele in visited: 
                if ele.stack == expanded_node.stack: 
                    child_in_visited == True
            if child_in_visited == False and child_in_frontier == False:
                frontier.append(expanded_node)
                
            """If child in frontier with higher cost """
            for ele in frontier: 
                if ele.stack == expanded_node.stack and ele.cost > expanded_node.cost:
                    frontier[frontier.index(ele)] = expanded_node

                    
        count += 1
        
        
        #frontier = sorted(frontier, key = lambda i:i['cost'])

        
        #break
        #if count == 5: break
 
        
        

    if not_found == False:
        solution = "Pancakes found. " + str(working_stack.stack)
        print (solution)
        print (count)