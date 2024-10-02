def encontrar_pareja_cero(lista):
    vistos = set()
    encontrado = False
    for numero in lista:
        opuesto = -numero
        if opuesto in vistos:
            print(f"Los números que suman cero son: {numero} y {opuesto}")
            encontrado = True
        vistos.add(numero)
    
    if not encontrado:
        print("No se encontraron dos números que sumen cero.")

# Función para obtener datos del usuario
def obtener_datos_usuario():
    entrada = input("Ingresa una lista de números separados por comas: ")
    # Convertir la entrada a una lista de enteros
    lista = [int(num.strip()) for num in entrada.split(',')]
    return lista

# Ejemplo de uso
while True:
    lista_datos = obtener_datos_usuario()
    print(f"Analizando la lista: {lista_datos}")
    encontrar_pareja_cero(lista_datos)
    
    continuar = input("¿Quieres analizar otra lista? (s/n): ")
    if continuar.lower() != 's':
        break
