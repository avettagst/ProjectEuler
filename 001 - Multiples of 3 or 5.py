'''
https://projecteuler.net/problem=1
'''

sum = 0
N = 1000

for n in range(1, N):
    if(n%3 == 0 or n%5 == 0):
        sum += n

print(sum)