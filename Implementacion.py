def validar_numero(input_str):
    """Función para validar que un número ingresado por el usuario sea válido."""
    try:
        float(input_str)
        return True
    except ValueError:
        return False
