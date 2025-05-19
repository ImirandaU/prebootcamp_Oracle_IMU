''' TAREA 2 '''
#EJERCICIO 1: Básico: imprime todos los números enteros del 0 al 100.
def basico():
    suma = 0
    for i in range(101):
        if i>= 1:
            suma += i
    return suma
basico()

#EJERCICIO 2: Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
def multiplos_2():
    for i in range(501):
        if i>=2:
            if i%2 ==0:
                print(i)
multiplos_2()

#EJERCICIO 3: Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
def vainilla_ice():
    for i in range(101):
        if i%5==0:
            print("ice ice")
        if i%10==0:
            print("baby")
        else:
            print (i)
vainilla_ice()

# EJERCICIO 4: Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
def num_gigante():
    suma = 0
    for i in range(500001):
        if i%2==0:
            suma += i
    return suma
num_gigante()

#EJERCICIO 5: Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
def tres_en_tres():
    i = 2024
    while i >=0:
        print(i)
        i-=3
tres_en_tres()

#EJERCICIO 6: Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo
numInicial = 3
numFinal = 10
multiplo = 2

def contador_dinamico(numInicial, numFinal, multiplo):
    #final = numFinal + 1
    for i in range(numFinal):
        paso = i*multiplo
        if (paso >=numInicial and paso<=numFinal):
            print (paso)
            
contador_dinamico(numInicial, numFinal, multiplo)









