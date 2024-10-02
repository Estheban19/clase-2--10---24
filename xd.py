def verificar_voto():
    edad = int(input("Ingresa tu edad: "))
    
    if edad < 0:
        print("No existe esa edad.")
    elif edad >= 18:
        print("Puedes votar.")
    else:
        print("No puedes votar.")

# Llamar a la función
verificar_voto() 