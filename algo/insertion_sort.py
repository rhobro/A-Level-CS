import random as rand

def insertion(s):
    new = [s[0]]

    for tobe in s[1:]:
        idx = 0

        for n in new:            
            if tobe > n:
                idx += 1
            else:
                break
        new.insert(idx, tobe)
    
    return new

ss = [rand.randint(0, 1000000) for _ in range(1000)]
print(insertion(ss) == sorted(ss))