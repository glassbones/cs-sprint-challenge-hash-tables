def solve(a,b,target):
    if a + b == target: return True
    else: return False

def get_indices_of_item_weights(weights, length, limit):
    d = {k: v for v, k in enumerate(weights)}
    w = sorted(frozenset([item for item in weights if item <= limit]))
    mid = int(len(w)/2)
    pair = []
    
    print(f'weights = {weights}')
    print(f'target = {limit}')
    print('')
    print(f'w = {w}')
    print(f'len = {len(w)}')
    print(f'mid = {mid}')
    print(f'list 1 = {w[:mid]}')
    print(f'list 2 = {w[mid:]}')

    if len(w) < 2 and w[0]*2 != limit: return None
    if len(w) < 2 and w[0]*2 == limit:
        solution = []
        for idx, val in enumerate(weights):
            if val == w[0]: 
                solution.append(idx)
        return sorted(solution, reverse=True)

    if w[-1] == limit:
        if 0 not in w: return None

    for a in w[:mid]:
        for b in w[mid:]:
            if solve(a,b,limit):
                print(f'a = {a} b = {b}')
                pair = [a,b]
                return sorted([d[a], d[b]], reverse=True)
    else: return None


    

"""
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
"""
#print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21))