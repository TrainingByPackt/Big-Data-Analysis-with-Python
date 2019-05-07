import numpy as np

vec = np.random.randint(0, 100, size=10)

for j in np.arange(1, vec.size):
    v = vec[j]
    i = j
    while i > 0 and vec[i-1] > v:
        vec[i] = vec[i-1]
        i = i - 1
    vec[i] = v

print(vec)
