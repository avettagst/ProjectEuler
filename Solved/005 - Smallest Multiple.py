'''
https://projecteuler.net/problem=5
'''


# # Busco el menor número divisible por 1, 2, ..., N
# N = 20

# # En el peor de los casos, este número es la productoria de 1*2*...*N
# max = 1
# for i in range(2, N+1):
#     max = max*i

# '''
# Particularmente para N = 20
# '''
# # Para N' = 10, sé que el resultado es 2520
# # Entonces, para N > 10, sé que este número debe ser mayor a 2520
# min = 2520

# divisores_a_chequear = range(11, 21) # Si es divisible por estos números, entonces también
#                                      # es divisible por [1, 10]


# for i in range(min, max):
#     divisible = True
#     for d in divisores_a_chequear:
#         if(i%d != 0):
#             divisible = False
#             break
#     if(divisible):
#         print(i)
#         break

'''
Esta solución lleva aprox 1'30'', cuando en teoría deberían llevar menos de 1 minuto
Pruebo una segunda
'''

import numpy as np

def primos(N: int):
    '''
    Devuelve la lista de números primos menores o igual a N
    '''

    # El código de abajo sirve para N > 4 (por la definición del segundo for)
    if(N < 2):
        return []
    if(N == 2):
        return [2]
    elif(N == 3 or N == 4):
        return [2, 3]
    else:
        primos = [2, 3]

    
    for i in range(5, N+1):

        # Recorro los posibles divisores de i (sin contar 1 y miro solo hasta sqrt(N))
        # (+1 porque redondeo para arriba el entero)
        primo = True
        for j in range(2, int(np.sqrt(i)) + 1):

            # Si encuentro un divisor, sé que no es primo y corto el loop
            if(i%j == 0):
                primo = False
                break
            
        # Si llegué al final del loop y no encontré divisor, es primo
        if(primo):
            primos.append(i)

    return primos

def divisible(k: int, divs: list):

    for d in divs:
        if(k%d != 0):
            return False
        
    return True


N = 20

primos = primos(N)

# Obtengo el producto de todos los números primos en [1, N]
mult_primos = 1
for p in primos:
    mult_primos = mult_primos*p


# Para cada múltiplo de este número, chequeo con los divisores que me falta chequear
# (los mismos que en el otro enfoque pero sin los primos)
divisores_a_chequear = [12, 14, 15, 16, 18, 20]

busco = True
i = 0
while(busco):
    i+=1
    if(divisible(mult_primos*i, divisores_a_chequear)):
        busco = False

print(mult_primos*i)

'''
Ésta solución funcionó infinitamente más rápido
'''