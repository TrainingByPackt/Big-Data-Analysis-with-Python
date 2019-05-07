import numpy as np

# this vector is modified to size=20
vec = np.random.randint(0, 100, size=20)

for j in np.arange(1, vec.size):
    v = vec[j]
    i = j
    while i > 0 and vec[i-1] > v:
        vec[i] = vec[i-1]
        i = i - 1
    vec[i] = v

print(vec)
