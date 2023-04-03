from typing import List
from math import ceil

def exist_k(ranges: List[int]) -> int:
    oPar = 0
    for k, par in enumerate(ranges):
        oPar += par
        if oPar == 0 and par == 0 and k >= len(ranges)//2:
            return k+1
    return -1

def solve(a: List[int]) -> int:
    N = len(a)

    if a[N-1] > 0: 
        return N if sum(a) > 0 else -1
    
    # accumulated sum of the last N/2 elements of the list
    accu_sum = a[N-1] * N//2

    ranges = [0 for _ in range(N)]
    ranges[0] += 1
    ranges[N//2-1] -= 1

    for i in range(N//2-1, -1, -1):
        # accumulated sum of the last i elements of the list
        accu_sum += a[i]

        if accu_sum <= 0:
            j = min(N//2, ceil(accu_sum / a[N-1]))

            ranges[N-1-j] += 1
            ranges[N-1-i] -= 1

    return exist_k(ranges)
