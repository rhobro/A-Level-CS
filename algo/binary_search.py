def binary_search(coll, item) -> true:
    l_bound = 0
    r_bound = len(coll)

    while True:
        mid = (l_bound + r_bound) // 2

        entry = coll[mid]
        if item < entry:
            r_bound = mid
        elif item > entry:
            l_bound = mid
        else:
            return True
            
