from math import sqrt


string = "1_2_3_4_5_6_7_8_9_0"
char_list = list(string) # lo uso así para cambiarle fácil los caracteres

'''
entendí mal el enunciado, no son todos los _ el mismo dígito
'''

for digit in range(10):
    for i in range(len(string)):
        if (i%2 != 0):
            char_list[i] = str(digit)
    numero_str = "".join(char_list)
    numero = int(numero_str)
        
    print(numero)
    print(sqrt(numero))
        
    if(isinstance(sqrt(numero), int)):
        print(digit)
        print(sqrt(numero))
        break
