


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
                


def A_search():
    search_space = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    print(flip(search_space, 2))
    
    """frontier = [A, B, C]
    while goal not reached: 
        #compute priority on each node
        #sort 
        priority(frontier)
        if fronier is empty: 
            return fail
        if node is goal:
            return goal
        for child in search_space: """

A_search()