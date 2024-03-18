'''
https://projecteuler.net/problem=2
'''


# Para iniciar la secuencia
first = 1
second = 2

# Acumulo la suma de los pares, ya sumando el término par que inicia la secuencia
sum = 2

N = 4e6 # Límite indicado

# Hasta superar el límite indicado
while((first+second) < N):
    new = first + second
    first = second
    second = new
    
    if(new%2 == 0):
        sum += new

print(sum)