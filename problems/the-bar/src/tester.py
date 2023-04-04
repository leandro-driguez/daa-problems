from logging import exception
from typing import List
from solution import solve
import random


# brute force
def solve2(a: List[int]) -> int:
    N = len(a)

    # precalculation of the array with the accumulated sum
    accum_sum = [0 for _ in range(N+1)]
    for i, item in enumerate(a):
        accum_sum[i+1] = item + accum_sum[i]

    for k in range(1, N+1):
        # checks if there is any subarray of size K, with non-positive sum
        l = 0; r = k
        while r <= N:
            if accum_sum[r] - accum_sum[l] <= 0:
                break
            l += 1; r += 1
        else:
            return k

    return -1


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


def tester(amount_tests: int, max_size: int):
    
    for case in range(amount_tests):
        
        size = random.randint(1, max_size)
        
        a = []
        for _ in range(size - size//2):
            a.append(random.randint(-1e9, 1e9))

        a += [random.randint(-1e9, 1e9)] * (size//2)

        k = solve(a)
        
        print("\033[1;37m" + f'Case {case}, verdict:')
        if k > 0 and check(a, k):
            print( chr(27) + "[1;32m" + "Accepted")
        elif solve2(a) == k == -1:
            print( chr(27) + "[1;32m" + "Accepted")
        else:
            print(chr(27) + "[1;31m" +'Wrong Answer')
            print(f'k={k} is not solution for the given list.\n')
        print("\033[0;37m" )

if __name__ == '__main__':
    AMOUNT_OF_TEST_CASES = 1000
    SIZE_OF_ARRAY = 1000

    tester(
        amount_tests=AMOUNT_OF_TEST_CASES,
        max_size=SIZE_OF_ARRAY
    )
