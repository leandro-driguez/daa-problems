from typing import List
from solution import solve
import random


# brute force
def solve2(a: List[int]) -> int:
    N = len(a)

    accum_sum = [0 for _ in range(N+1)]

    for i, item in enumerate(a):
        accum_sum[i+1] = item + accum_sum[i]

    for k in range(1, N+1):
        l = 0; r = k
        while r <= N:
            if accum_sum[r] - accum_sum[l] <= 0:
                break
            l += 1; r += 1
        else:
            return k

    return -1


def check(a: List[int], k) -> int:
    N = len(a)

    accum_sum = [0 for _ in range(N+1)]

    for i, item in enumerate(a):
        accum_sum[i+1] = item + accum_sum[i]

    l = 0; r = k
    while r <= N:
        if accum_sum[r] - accum_sum[l] <= 0:
            break
        l += 1; r += 1
    else:
        return k

    return -1


def tester(amount_tests: int, max_size: int):
    
    for _ in range(amount_tests):
        
        size = random.randint(1, max_size)
        
        a = []
        for _ in range(size - size//2):
            a.append(random.randint(-2**32, 2**32))

        a += [random.randint(-2**32, 2**32)] * (size//2)

        k = solve(a)

        try:
            if k > 0:
                assert check(a, k)
            else:
                assert solve2(a) == k == -1
        except:
            print(f'k={k} is not solution of:\n{a}\n')


if __name__ == '__main__':
<<<<<<< HEAD
    AMOUNT_OF_TEST_CASES = 1_000
    SIZE_OF_ARRAY = 1_000_000

=======
    AMOUNT_OF_TEST_CASES = 1_000_0
    SIZE_OF_ARRAY = 1000
    
>>>>>>> 9f179a0b3b5099f958986ddb648bd92df42cc01f
    tester(
        amount_tests=AMOUNT_OF_TEST_CASES,
        max_size=SIZE_OF_ARRAY
    )
