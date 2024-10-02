def encontrar_pareja_cero(lista):
    vistos = set()
    for numero in lista:
        opuesto = -numero
        if opuesto in vistos:
            print(f"Los números que suman cero son: {numero} y {opuesto}")
            return
        vistos.add(numero)
    print("No se encontraron dos números que sumen cero.")

# Ejemplo de uso
lista_datos = [10, 15, 7, -2, 5, -15]
encontrar_pareja_cero(lista_datos)



