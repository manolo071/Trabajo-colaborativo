def validar_numero(input_str):
    """Función para validar que un número ingresado por el usuario sea válido."""
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def obtener_numero_validado(mensaje):
    """Función para obtener un número validado ingresado por el usuario."""
    while True:
        numero = input(mensaje)
        if validar_numero(numero):
            return float(numero)
        else:
            print("¡Error! Ingresa un número válido.")

def realizar_suma(a, b):
    """Función para realizar la operación de suma."""
    return a + b

def realizar_resta(a, b):
    """Función para realizar la operación de resta."""
    return a - b

def realizar_multiplicacion(a, b):
    """Función para realizar la operación de multiplicación."""
    return a * b
