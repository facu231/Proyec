print("""#####################################
Programa que suma todos los números 
enteros impares desde el 0 hasta el 100: """)

total = 0
numerosInpares = []

for n in range(1,101):
    if n % 2 != 0:
        numerosInpares.append(n)
print(sum(numerosInpares))





        

    