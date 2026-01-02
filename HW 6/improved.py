import random

def loss(x, y, b0, b1):
    s = 0
    for xi, yi in zip(x, y):
        s += ((b0 + b1 * xi) - yi) ** 2
    return s


def hill_step(x, y, b0, b1, step, iters):
    best = loss(x, y, b0, b1)
    for _ in range(iters):
        for dx, dy in [(step,0),(-step,0),(0,step),(0,-step)]:
            c0, c1 = b0 + dx, b1 + dy
            L = loss(x, y, c0, c1)
            if L < best:
                best = L
                b0, b1 = c0, c1
    return b0, b1, best


def improved(x, y, restarts=10):
    best_L = float("inf")
    best_b0, best_b1 = 0, 0

    for _ in range(restarts):
        b0 = random.uniform(-5000, 5000)
        b1 = random.uniform(-500, 500)
        step = 50

        for _ in range(6):
            b0, b1, L = hill_step(x, y, b0, b1, step, 2000)
            step *= 0.5

        if L < best_L:
            best_L = L
            best_b0, best_b1 = b0, b1

    return best_b0, best_b1, best_L
