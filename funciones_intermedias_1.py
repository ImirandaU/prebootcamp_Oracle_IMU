''' Crea el archivo un Python llamado funciones_intermedias_1.py
Actualiza los valores en diccionarios y listas
Crea la función iterarDiccionario(lista)
Crea la función iterarDiccionario2(llave, lista)
Crea la función imprimirInformacion(diccionario) '''

#1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

def actualizar(matriz, cantantes, ciudades, coordenadas):
    matriz[1][0] = 6
    cantantes[0]["nombre"] = "Enrique Martin Morales"
    ciudades["México"][2] = "Monterrey"
    coordenadas[0]["latitud"] = 9.9355431
    print(matriz)
    print(cantantes)
    print(ciudades)
    print(coordenadas)

actualizar(matriz, cantantes, ciudades, coordenadas)

#2. Iterar a través de una lista de diccionarios
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]


def iterarDiccionario(cantantes):
    for i in range(len(cantantes)):
        nombre = cantantes[i]["nombre"]
        pais = cantantes[i]["pais"]
        print (f"nombre - {nombre}, pais - {pais}")

iterarDiccionario(cantantes)

#3. Obtener valores de una lista de diccionarios
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])
        else:
            print(f"La clave '{llave}' no existe en el diccionario.")

iterarDiccionario2("pais", cantantes)

#4. Iterar a través de un diccionario con valores de lista
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)
        print()  # Línea en blanco para separar secciones

imprimirInformacion(costa_rica)




