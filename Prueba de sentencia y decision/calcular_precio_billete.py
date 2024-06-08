def calcular_precio_billete(edad, clase):
    if clase == "economica":
        if edad < 2:
            return 0  # Bebés viajan gratis
        elif edad <= 12:
            return 50  # Descuento para niños
        else:
            return 100  # Adulto
    elif clase == "ejecutiva":
        if edad < 2:
            return 100  # Bebés en clase ejecutiva
        elif edad <= 12:
            return 150  # Descuento para niños
        else:
            return 300  # Adulto
    else:
        return "Clase no válida"

def main():
    # Capturar la edad del usuario
    edad = int(input("Ingrese la edad del pasajero: "))

    # Capturar el tipo de clase del usuario
    clase = input("Ingrese la clase del pasajero (economica/ejecutiva): ").lower()

    # Calcular el precio del billete
    precio = calcular_precio_billete(edad, clase)

    # Mostrar el resultado
    if isinstance(precio, int):
        print(f"El precio del billete que tiene que pagar es: {precio} dólares.")
    else:
        print(precio)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
