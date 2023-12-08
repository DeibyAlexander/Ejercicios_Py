# Definición de funciones para realizar operaciones
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: No se puede dividir por cero"

# Bucle principal para ejecutar la calculadora
while True:
    # Menú de operaciones
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    # Entrada del usuario para seleccionar la operación
    opcion = input("Ingrese la opción (1-5): ")

    # Salir del bucle si el usuario selecciona la opción 5
    if opcion == "5":
        print("¡Hasta luego!")
        break

    try:
        # Entrada del usuario para ingresar dos números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        # Capturar errores si el usuario no ingresa números válidos
        print("Error: Ingrese números válidos.")
        continue

    # Estructuras condicionales para realizar la operación seleccionada
    if opcion == "1":
        # Llamada a la función de suma y mostrar el resultado
        print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == "2":
        # Llamada a la función de resta y mostrar el resultado
        print(f"Resultado: {restar(num1, num2)}")
    elif opcion == "3":
        # Llamada a la función de multiplicación y mostrar el resultado
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcion == "4":
        # Llamada a la función de división y mostrar el resultado
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        # Mensaje si el usuario selecciona una opción no válida
        print("Opción no válida. Seleccione una opción del 1 al 5.")
