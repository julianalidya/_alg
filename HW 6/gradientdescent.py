def loss(x, y, b0, b1):
    s = 0
    for xi, yi in zip(x, y):
        s += ((b0 + b1 * xi) - yi) ** 2
    return s


def gradient_descent(x, y, lr=0.0001, iters=200000):
    b0, b1 = 0.0, 0.0
    n = len(x)

    for _ in range(iters):
        g0 = 0
        g1 = 0
        for xi, yi in zip(x, y):
            e = (b0 + b1 * xi) - yi
            g0 += e
            g1 += e * xi
        b0 -= lr * (2 * g0 / n)
        b1 -= lr * (2 * g1 / n)

    return b0, b1, loss(x, y, b0, b1)
