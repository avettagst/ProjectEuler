'''
https://projecteuler.net/problem=4
'''


# Acá almaceno los palíndromos que vaya encontrando
palindromos = []

# Todos los pares posibles de números de 3 dígitos, empezando de arriba para abajo
for i in range(999, 99, -1):
    for j in range(999, i-1, -1):

        # Producto 
        k = i*j

        # Lo transformo en string para analizar si es palíndromo
        string = str(k)
        N = len(string)

        # Es palíndromo hasta que se demuestre lo contrario
        pal = True


        for c in range(int(N/2)):
            # Si para un par de dígitos no se cumple la igualdad, no es palíndromo
            if(string[c] != string[N-1-c]):
                pal = False
        
        # Después de recorrer todos los dígitos, si siempre cumplió la igualdad, es palíndromo
        if(pal):
            palindromos.append(k)

print(palindromos)
print("Máximo: " + str(max(palindromos)))
