def jank(string, depth=0):
    if depth <= 0:
        return string
    n = jank(string, depth-1)
    return string + "^{" + n + "}_{" + n + "}"

print( jank("jank", depth=9) )