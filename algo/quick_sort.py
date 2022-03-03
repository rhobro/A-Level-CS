import random as rand


def quick(s):
    if len(s) == 0:
        return s

    split_point = 0
    pivot = s[split_point]
    less = [n for n in s if n <= pivot]
    more = [n for n in s if n > pivot]

    less = quick(less)
    more = quick(less)
    
    # merge back
    return less + [pivot] + more


ss = [rand.randint(0, 10) for _ in range(10)]
print(quick(ss))