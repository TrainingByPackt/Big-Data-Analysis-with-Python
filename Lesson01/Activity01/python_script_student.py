import numpy as np

def square_plus(x, c):
    return np.power(x,2) + c

x = 10
c = 100

result = square_plus(x, c)
print(result)
