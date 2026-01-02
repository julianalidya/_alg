def loss(x, y, b0, b1):
    s = 0
    for xi, yi in zip(x, y):
        s += ((b0 + b1 * xi) - yi) ** 2
    return s


def hill_climbing(x, y, step=1.0, iters=10000):
    b0, b1 = 0.0, 0.0
    best = loss(x, y, b0, b1)

    for _ in range(iters):
        candidates = [
            (b0 + step, b1),
            (b0 - step, b1),
            (b0, b1 + step),
            (b0, b1 - step)
        ]
        improved = False
        for c0, c1 in candidates:
            L = loss(x, y, c0, c1)
            if L < best:
                best = L
                b0, b1 = c0, c1
                improved = True
        if not improved:
            break
    return b0, b1, best
