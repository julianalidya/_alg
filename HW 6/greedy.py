import random

def loss(x, y, b0, b1):
    s = 0
    for xi, yi in zip(x, y):
        s += ((b0 + b1 * xi) - yi) ** 2
    return s


def greedy(x, y, trials=20000):
    b0 = random.uniform(-5000, 5000)
    b1 = random.uniform(-500, 500)
    best = loss(x, y, b0, b1)

    for _ in range(trials):
        c0 = random.uniform(-5000, 5000)
        c1 = random.uniform(-500, 500)
        L = loss(x, y, c0, c1)
        if L < best:
            best = L
            b0, b1 = c0, c1

    return b0, b1, best
