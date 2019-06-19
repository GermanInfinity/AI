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
    flip_num = 5
    working_stack = [4, 2, 3, 1, 5]
    frontier = []
    visited = []
    frontier.append({"child": working_stack, "cost": forward_cost(working_stack)})
    visited.append({"child": working_stack, "cost": forward_cost(working_stack)})

    

    
    not_found = True
    count = 0
    while not_found: 
        count += 1
        
        
        for idx in range(1, flip_num+1):
            flip_return = flip(working_stack, idx)
            backward_cost = idx  
            
            child = flip_return
            cost = forward_cost(flip_return) + backward_cost
            
            
            child_in_frontier = False
            child_in_visited = False
            
            for idx in range(len(frontier)): #Checking all of frontier for child  
                if frontier[idx]['child'] == child:
                    child_in_frontier = True

                if idx == len(frontier)-1 and child_in_frontier == False: 
                    frontier.append({"child": flip_return, "cost": cost})
                    
            for idx in range(len(visited)): #Checking all of visited for child  
                if visited[idx]['child'] == child:
                    child_in_visited = True

                if idx == len(visited)-1 and child_in_visited == False: 
                    frontier.append({"child": flip_return, "cost": cost})
                                
            for element in frontier: 
                if element['child'] == child and element['cost'] > cost:
                    replace_child = {"child": flip_return, "cost": cost}
                    frontier[frontier.index(element)] = {"child": flip_return, "cost": cost}
                    
        if count == 1: del frontier[0] #Delete the initial state
                    
        if len(frontier) == 0: 
            print ("Failure")
            break 

        #print (frontier)
        frontier = sorted(frontier, key = lambda i:i['cost'])
        
        #print (frontier)
        #print ("in")
        #print (frontier[0]['child'])
        #GOAL STATE CHECK#
        working_stack = frontier[0]['child']
        visited.append(frontier[0]) #We go here now. 
        
        """Goal check: a combination that has no gaps in it and is arranged 
                   in this order: [5, 4, 3, 2, 1]"""
        result = [x for x in frontier if forward_cost(x['child']) == 0 and x['child'][0] == 5]
        if len(result) > 0: not_found = False
        
        #Delete from frontier
        del frontier[0]

        if count == 40: break
 
        
        
        
    print ('End')
    print (working_stack)
    if not_found == False: print (working_stack)
