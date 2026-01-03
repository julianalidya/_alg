import numpy as np
import math

def softmax(z):
    z = np.array(z, dtype=float)
    z -= np.max(z)
    e = np.exp(z)
    return e / np.sum(e)

def cross_entropy_base2(p, q):
    return -np.sum(p * np.log(q)) / math.log(2)

def optimize_q_to_match_p(p, steps=5000, lr=0.5, seed=0):
    rng = np.random.default_rng(seed)
    z = rng.normal(size=len(p))

    for _ in range(steps):
        q = softmax(z)
        grad = (q - p) / math.log(2)
        z -= lr * grad

    q = softmax(z)
    return q, cross_entropy_base2(p, q)

p = [0.5, 0.25, 0.25]

for i in range(3):
    q, loss = optimize_q_to_match_p(p, seed=i)
    print("q =", q, " cross_entropy =", loss)

print("cross_entropy(p,p) =", cross_entropy_base2(p, p))
