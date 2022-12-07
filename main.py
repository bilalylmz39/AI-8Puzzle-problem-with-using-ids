#Depth first search in search of target - Using Recursion
def dfs(src,target, limit,visited_states):
    if src == target:
        return True
    if limit <= 0:
        return False
    visited_states.append(src)

    ad = possible_moves(src,visited_states)

    for move in ad:
        if dfs(move,target,limit -1,visited_states):
            return True
    return False

def possible_moves(state,visited_states):
    #Find index of empty spot and assign it to b

    indx = state.index(-1)

    #'d' for down, 'u' for up, 'r' for right, 'l' for left - directions array
    d = []

    #Add all possible direction into directions array -Hint using if statements

    if indx +3 in range(9):
        d.append('d')
    if indx -3 in range(9):
        d.append('u')
    if indx not in [0,3,6]:
        d.append('l')
    if indx not in [2,5,8]:
        d.append('r')

    # If direction is possible then add state to move
    posi_moves = []

    #for all possible directions find the state if that move is played
    ### Jump to gen function to generate all possible moves in the given directions
    for move in d:
        posi_moves.append(gen(state,move,indx))
    #return all possible moves only if the move not in visited_states
    return [move for move in posi_moves
            if move not in visited_states]

def gen(state,m,b): # m(move) is direction to slide, b(blank) is index of empty
    # create a copy of current state to test the move
    tmp = state.copy()

    # if move is to slide empty spot to the left and so on

    if m == 'd':
        a = tmp[b+3]
        tmp[b+3] = tmp[b]
        tmp[b] = a
    elif m == 'u':
        a = tmp[b - 3]
        tmp[b - 3] = tmp[b]
        tmp[b] = a
    elif m == 'l':
        a = tmp[b - 1]
        tmp[b - 1] = tmp[b]
        tmp[b] = a
    elif m == 'r':
        a = tmp[b + 1]
        tmp[b + 1] = tmp[b]
        tmp[b] = a

    return tmp

def ids(src,target,depth):
    visited_states = []
    # Return Min depth at which the target was found
    for x in range(1,depth+1):
        if dfs(src,target,x,visited_states): return True
    return False

# Test 1
src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, -1, 6, 7, 8]

depth = 2
ids(src, target, depth)  # Minimum depth should be 2
print(ids([1, 2, 3, -1, 4, 5, 6, 7, 8],[1, 2, 3, 4, 5, -1, 6, 7, 8],2))
print("*******************************")
# Test 2
src = [1,2,3,-1,4,5,6,7,8]
target=[1,2,3,6,4,5,-1,7,8]

depth = 1
ids(src, target, depth) # Minimum depth is 1
print(ids([1,2,3,-1,4,5,6,9,8],[1,2,3,6,4,5,-1,7,8],1))
print("*******************************")
# Test 3
# Try to create a source and target that reaches large minimum required depth
src = None
target = None

ids(src, target, depth)

print(ids(None,None,2))
