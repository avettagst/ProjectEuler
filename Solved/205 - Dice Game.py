'''
https://projecteuler.net/problem=205

Variables aleatorias correspondientes a cada dado:
p ~ U(1,4)
c ~ U(1,6)

Variables aleatorias correspondientes a las sumas de los dados de cada uno:
P = 9p / 9 <= P <= 36
C = 6c / 6 <= C <= 36

---> Cambios de variable no inyectivos
                         
Puedo pensar a este cambio de variables como una convolución y con algo de recursión:
https://stats.libretexts.org/Bookshelves/Probability_Theory/Book%3A_Introductory_Probability_(Grinstead_and_Snell)/07%3A_Sums_of_Random_Variables/7.01%3A_Sums_of_Discrete_Random_Variables

--> Defino a las distribuciones de probabilidad como diccionarios
'''

def dist_N(dist_1: dict, dist_Nmenos1: dict, k: int, N: int):
    '''
    A partir de la distribución de la variable aleatoria unidimensional (dist_1) que toma valores
    enteros entre 1 y k y de la distribución de la suma de N-1 variables aleatorias (dist_Nmenos1), obtengo la distribución para la suma de N variables aleatorias.
    '''

    dist_nueva = {} # Distribución a retornar

    for suma in range(N, k*N + 1):
        prob = 0
        #print(suma)
        for i in range(max(1, suma-(N-1)*k), min(suma, k)+1):
            if((suma - i) < (N-1)):
                break
            #print(str(i) + "    /    " + str(suma-i))
            prob += dist_1[i]*dist_Nmenos1[suma-i]

        dist_nueva[suma] = prob

    return dist_nueva



np = 4 # cantidad de caras para Peter
nc = 6 # cantidad de caras para Colin

p_S1 = {}
for p in range(1, np+1):
    p_S1[p] = 1/np

c_S1 = {}
for p in range(1, nc+1):
    c_S1[p] = 1/nc

# Con recursión y a partir de la distribución para una sola variable aleatoria
# puedo obtener la distribución para la suma de 6 y 9 variables aleatorias, según corresponda
p_S2 = dist_N(p_S1, p_S1, np, 2)
p_S3 = dist_N(p_S1, p_S2, np, 3)
p_S4 = dist_N(p_S1, p_S3, np, 4)
p_S5 = dist_N(p_S1, p_S4, np, 5)
p_S6 = dist_N(p_S1, p_S5, np, 6)
p_S7 = dist_N(p_S1, p_S6, np, 7)
p_S8 = dist_N(p_S1, p_S7, np, 8)
p_S9 = dist_N(p_S1, p_S8, np, 9)
print("Distribución para Pyramidal Peter")
print(p_S9)

c_S2 = dist_N(c_S1, c_S1, nc, 2)
c_S3 = dist_N(c_S1, c_S2, nc, 3)
c_S4 = dist_N(c_S1, c_S3, nc, 4)
c_S5 = dist_N(c_S1, c_S4, nc, 5)
c_S6 = dist_N(c_S1, c_S5, nc, 6)
print("Distribución para Cubic Colin")
print(c_S6)


'''
Plot de distribuciones
'''
# import matplotlib.pyplot as plt

# S9 = list(p_S9.keys()) 
# probs_S9 = list(p_S9.values())

# S6 = list(c_S6.keys()) 
# probs_S6 = list(c_S6.values())

# plt.plot(S9, probs_S9, label = "Peter")
# plt.plot(S6, probs_S6, label = "Colin")
# plt.legend()
# plt.show()

gana_peter = 0

for peter in range(9, 37):
    marginal = p_S9[peter]
    condicionada = 0
    #print(peter)
    #print(marginal)
    for colin in range(6, peter):
        #print("\t" + str(colin) + "\t" + str(c_S6[colin]))
        condicionada += c_S6[colin]

    gana_peter += condicionada*marginal

print("\n\nProbabilidad de que gane Peter")
print(round(gana_peter, 7))

