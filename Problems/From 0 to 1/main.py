import random


# work with this variable
n = int(input())
random.seed(n)
print(random.random())
# or random.uniform(0, 1), uniform: returns a pseudo-random float number in the range between 0 and 1
