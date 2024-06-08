from calcular_precio_billete import calcular_precio_billete

def test_calcular_precio_billete():
    # Pruebas para clase económica
    assert calcular_precio_billete(1, "economica") == 0, "Error: Bebé en clase económica"
    assert calcular_precio_billete(5, "economica") == 50, "Error: Niño en clase económica"
    assert calcular_precio_billete(30, "economica") == 100, "Error: Adulto en clase económica"
    
    # Pruebas para clase ejecutiva
    assert calcular_precio_billete(1, "ejecutiva") == 100, "Error: Bebé en clase ejecutiva"
    assert calcular_precio_billete(10, "ejecutiva") == 150, "Error: Niño en clase ejecutiva"
    assert calcular_precio_billete(30, "ejecutiva") == 300, "Error: Adulto en clase ejecutiva"
    
    # Prueba para clase no válida
    assert calcular_precio_billete(30, "primera clase") == "Clase no válida", "Error: Clase no válida"

    print("Todas las pruebas pasaron exitosamente.")

# Ejecutar las pruebas
test_calcular_precio_billete()
