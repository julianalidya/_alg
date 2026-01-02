# Method 1
def power2n(n):
    return 2 ** n


# Method 2a
def power2n(n):
    if n == 0:
        return 1
    return power2n(n - 1) + power2n(n - 1)


# Method 2b
def power2n(n):
    if n == 0:
        return 1
    return 2 * power2n(n - 1)


# Method 3
lookup = [None] * 10000
lookup[0] = 1

def power2n(n):
    if lookup[n] is not None:
        return lookup[n]
    lookup[n] = power2n(n - 1) + power2n(n - 1)
    return lookup[n]
