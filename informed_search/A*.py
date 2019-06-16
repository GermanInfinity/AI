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
    def __init__(self, shape, cost):
        self.shape = shape
        self.cost = cost
    
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
    

"""
    Name: flips
    Description: Flips the pancake at position specified. 
                 Flipping topmost pancake is position 1, flipping all pancakes
                 is flipping from position 5. 
    Input: Stack of pancakes and position to flip from
    Output: flipped stack
"""    
def flip(stack, pos):
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
#def A_search():
    flip_num = 5
    working_stack = [5, 2, 3, 1, 4]
    frontier = []
    visited = []
    #working_stack = [5, 4, 3, 1, 2]
    #states also
    """states = []
    for idx in range(1, flip_num+1):
        flip_return = flip(initial_stack, idx)
        backward_cost = idx        
        arg = Pancake_stack(flip_return, 
                            forward_cost(flip_return) + backward_cost)
        states.append(arg)
        
    frontier = sorted(states, key=operator.attrgetter('cost'))"""
    
    not_found = True
    count = 0
    while not_found: 
        count += 1
        
        
        for idx in range(1, flip_num+1):
            flip_return = flip(working_stack, idx)
            backward_cost = idx        
            child = Pancake_stack(flip_return, 
                                forward_cost(flip_return) + backward_cost)
            
            if child not in frontier: frontier.append(child)
            if child not in visited: frontier.append(child)
        
        if len(frontier) == 0: 
            print ("Failure")
            break 
        
        frontier = sorted(frontier, key=operator.attrgetter('cost'))
        #print (len(frontier))
        #GOAL STATE CHECK#
        working_stack = frontier[0].shape
        print (working_stack)
        visited.append(frontier[0])
        
        """Goal check: a combination that has no gaps in it and is arranged 
                   in this order: [5, 4, 3, 2, 1]"""
        result = [x for x in frontier if forward_cost(x.shape) == 0 and x.shape[0] == 5]
        if len(result) > 0: not_found = False
        
        #Delete from frontier
        del frontier[0]
        print (frontier[0].shape)
        if count == 20: break
 
        #Guac bananas stew and lentil soup
    
        #Peanut butterr hummus corn tomatoes Sandwhich
        
        
    
    if not_found == False: print (working_stack)
