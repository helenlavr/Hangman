import random


random.seed(3)
random_beta = random.betavariate(alpha=0.9, beta=0.1)
print(random_beta)
