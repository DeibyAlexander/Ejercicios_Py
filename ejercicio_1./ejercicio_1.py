# Definición de la función para agregar una tarea a la lista
def agregar_tarea(lista_tareas):
    tarea_nueva = input("Ingrese una nueva tarea: ")
    lista_tareas.append(tarea_nueva)
    print(f"Tarea '{tarea_nueva}' agregada exitosamente.")

# Definición de la función para mostrar todas las tareas en la lista
def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas en la lista.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(lista_tareas, 1):
            print(f"{i}. {tarea}")

# Definición de la función para marcar una tarea como completada
def completar_tarea(lista_tareas):
    mostrar_tareas(lista_tareas)
    try:
        indice_tarea = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
        if 0 <= indice_tarea < len(lista_tareas):
            tarea_completada = lista_tareas.pop(indice_tarea)
            print(f"Tarea '{tarea_completada}' marcada como completada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Ingrese un número válido.")

# Definición de la función para eliminar una tarea de la lista
def eliminar_tarea(lista_tareas):
    mostrar_tareas(lista_tareas)
    try:
        indice_tarea = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if 0 <= indice_tarea < len(lista_tareas):
            tarea_eliminada = lista_tareas.pop(indice_tarea)
            print(f"Tarea '{tarea_eliminada}' eliminada exitosamente.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Ingrese un número válido.")

# Función principal que inicia el programa
def main():
    tareas = []

    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            mostrar_tareas(tareas)
        elif opcion == '3':
            completar_tarea(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
