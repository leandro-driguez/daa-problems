from logging import exception
from typing import List, Tuple
from solution import solve
import random


# brute force
def solve2(n : int, edges : List[Tuple[int,int,int]], Q : List[Tuple[int,int,int]]):
    
    #TODO
    
    pass


def check(a: List[int], k: int) -> int:
    N = len(a)

    # precalculation of the array with the accumulated sum
    accum_sum = [0 for _ in range(N+1)]
    for i, item in enumerate(a):
        accum_sum[i+1] = item + accum_sum[i]
    # check if any subarray of size K, has non-positive sum
    l = 0; r = k
    while r <= N:
        if accum_sum[r] - accum_sum[l] <= 0:
            break
        l += 1; r += 1
    else:
        return True

    return False

def random_graph(n, prob):
    edges = []
    
    for i in range(n):
        for j in range(n):
            if random.random() < prob:
                edges.append((i,j, random.randint(0,500)))
                
    return edges


def tester(amount_tests: int, max_nodes: int):
    
    for case in range(amount_tests):
        
        n = random.randint(1, max_nodes)
        
        edges = random_graph(n, 0.5) #TODO: adjust p value
        Q = random_graph(n, 0.2) #TODO: adjust p value

        k1 = solve(n, edges, Q)
        k2 = solve2(n ,edges, Q)
        
        print("\033[1;37m" + f'Case {case}, verdict:')
        if k1 == k2:
            print( chr(27) + "[1;32m" + "Accepted")
        else:
            print(chr(27) + "[1;31m" +'Wrong Answer')
        print("\033[0;37m" )

if __name__ == '__main__':
    AMOUNT_OF_TEST_CASES = 10
    MAX_NUMBER_OF_NODES = 1000

    tester(
        amount_tests=AMOUNT_OF_TEST_CASES,
        max_nodes=MAX_NUMBER_OF_NODES
    )
