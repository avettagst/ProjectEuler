def solucion(N):

    soluciones = 0

    if(N == 2):
        soluciones = 2
    else:
        #for x1 in range(N-1, int(N/2), -1)
        soluciones += solucion(N-1)
    return soluciones

print(solucion(4))

N = 13
for x1 in range(N-1, int((N+1)/2)-1, -1):
    print(x1)