# Copy and paste in Jupyter is easier than in IPython.
import numpy as np

## It's easier to edit the function definition on a Jupyter notebook because of the cell structure.
def square_plus(x, c):
    return np.power(x,2) + c

# Defining constants is similar in both, but because you can use IPython history, it's quicker on IPython to iterate.
x = 10
c = 100

# This part is easier to control on IPython, because the function definition must be redone in it, while the history in Jupyter can confuse the student.
result = square_plus(x, c)
print(result)
