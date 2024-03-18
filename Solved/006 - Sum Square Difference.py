'''
https://projecteuler.net/problem=6
'''

import numpy as np

N = 100

sum_squares = sum(np.power(range(1, N+1), 2))
squared_sum = sum(range(1, N+1))**2

print(squared_sum - sum_squares)

'''
Hay una solución más elegante con expresiones analíticas para ambos valores
'''

