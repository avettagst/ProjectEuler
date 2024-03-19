'''
https://projecteuler.net/problem=9
'''

sum = 1000

# a < b < c. Como mínimo, c = sum/3
# Además, a > 0 (porque no puede ser b = c) y b > a, así que, como máximo, c = sum - 3
min = int(sum/3)
max = sum - 3

def es_triplete(a: int, b: int, c: int):
    if(a**2 + b**2 == c**2):
        return True
    else:
        return False

encontrado = False
for c in range(min, max):
    for b in range(1, c):
        for a in range(1, b):
            if(es_triplete(a, b, c) and (a+b+c) == 1000):
                print(a*b*c)
                encontrado = True
                break
    
    # Si encontré el triplete, corto
    if(encontrado):
        break