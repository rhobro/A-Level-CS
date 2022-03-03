import random as rand

def bubble(s):
    clean = False
    while not clean:
        clean = True

        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
                clean = False
    
    return s

ss = [rand.randint(0, 1000000) for _ in range(1000)]
print(bubble(ss) == sorted(ss))