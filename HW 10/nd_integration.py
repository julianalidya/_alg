import math
import random

def riemann_nd(f, bounds, k):
    n = len(bounds)
    deltas = [(b - a) / k for a, b in bounds]
    total = 0.0

    def recurse(dim, x):
        nonlocal total
        if dim == n:
            total += f(x)
            return
        a, _ = bounds[dim]
        dx = deltas[dim]
        for i in range(k):
            xi = a + (i + 0.5) * dx
            recurse(dim + 1, x + [xi])

    recurse(0, [])
    return total * math.prod(deltas)

def monte_carlo_nd(f, bounds, samples):
    volume = math.prod(b - a for a, b in bounds)
    total = 0.0
    for _ in range(samples):
        x = [random.uniform(a, b) for a, b in bounds]
        total += f(x)
    return volume * total / samples

def main():
    f = lambda x: x[0] + x[1]
    bounds = [(0, 1), (0, 1)]

    riemann_result = riemann_nd(f, bounds, 50)
    monte_result = monte_carlo_nd(f, bounds, 100000)

    print(riemann_result)
    print(monte_result)

if __name__ == "__main__":
    main()
