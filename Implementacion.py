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

def realizar_division(a, b):
    """Función para realizar la operación de división."""
    if b != 0:
        return a / b
    else:
        print("¡Error! No se puede dividir por cero.")
        return None

# Solicitar al usuario ingresar dos números
numero1 = obtener_numero_validado("Ingresa el primer número: ")
numero2 = obtener_numero_validado("Ingresa el segundo número: ")

# Solicitar al usuario ingresar la operación deseada
operacion = input("Ingresa la operación deseada (+ para suma, - para resta, * para multiplicación, / para división): ")

# Realizar la operación seleccionada
if operacion == "+":
    resultado = realizar_suma(numero1, numero2)
elif operacion == "-":
    resultado = realizar_resta(numero1, numero2)
elif operacion == "*":
    resultado = realizar_multiplicacion(numero1, numero2)
elif operacion == "/":
    resultado = realizar_division(numero1, numero2)
else:
    print("¡Error! Operación inválida.")
    resultado = None

# Mostrar el resultado
if resultado is not None:
    print("El resultado de la operación es:", resultado)