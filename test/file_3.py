def quicksort(l):
    if not l:
        return []
    p = l[0]
    return quicksort([x for x in l[1:] if x<p]) + [p] + quicksort([x for x in l[1:] if x>=p])
