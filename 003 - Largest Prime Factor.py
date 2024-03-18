'''
https://projecteuler.net/problem=3
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
        
def es_primo(k: int):
    '''
    Devuelve True si k es primo, False si no
    '''

    # Único caso mal respondido con el algoritmo del for
    if(k == 1):
        return False




    # Recorro los posibles divisores de k (sin contar 1 y miro solo hasta sqrt(N))
    # (+1 porque redondeo para arriba el entero)
    primo = True
    for j in range(2, int(np.sqrt(k)) + 1):
        

        # Si encuentro un divisor, sé que no es primo y corto la función
        if(k%j == 0):
            return False
        
    # Si llegué al final del loop y no encontré divisor, es primo
    return True

N = 600851475143

if(es_primo(N)):
    print(str(N) + " es primo y es factor de sí mismo")
else:
    # Si no es primo, empiezo a analizar de su raíz cuadrada para abajo
    # Cuando encuentro un número primo, me fijo si es divisor. Al primero que encuentre, terminé
    for i in range(int(np.sqrt(N)) + 1, 2, -1):
        if(es_primo(i) and N%i == 0):
            print(i)
            break