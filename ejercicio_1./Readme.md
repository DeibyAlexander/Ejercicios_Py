Problema: Gestión de Tareas Diarias

Contexto:
Como parte de tu rutina diaria, a menudo te encuentras con varias tareas que necesitas realizar. Para mejorar tu organización, decides crear un programa simple que te permita gestionar tus tareas diarias. El programa debería ser capaz de agregar nuevas tareas, mostrar la lista actual de tareas, marcar tareas como completadas y eliminar tareas.


Requerimientos:

    Agregar Tarea: El usuario debería poder agregar nuevas tareas a la lista.
    Mostrar Tareas: El usuario debería poder ver la lista actual de tareas numeradas.
    Completar Tarea: El usuario debería poder marcar una tarea como completada.
    Eliminar Tarea: El usuario debería poder eliminar una tarea de la lista.
    Salir: El usuario debería poder salir del programa.

Estructura del Código:

    Función agregar_tarea(lista_tareas):
        Solicitar al usuario que ingrese una nueva tarea.
        Agregar la tarea a la lista de tareas.
        Mostrar un mensaje indicando que la tarea fue agregada exitosamente.

    Función mostrar_tareas(lista_tareas):
        Verificar si hay tareas en la lista.
        Si la lista está vacía, mostrar un mensaje indicando que no hay tareas.
        Si hay tareas, mostrar la lista numerada.

    Función completar_tarea(lista_tareas):
        Mostrar la lista de tareas numeradas.
        Solicitar al usuario que ingrese el número de la tarea a marcar como completada.
        Marcar la tarea como completada (eliminarla de la lista).
        Mostrar un mensaje indicando que la tarea fue marcada como completada.

    Función eliminar_tarea(lista_tareas):
        Mostrar la lista de tareas numeradas.
        Solicitar al usuario que ingrese el número de la tarea a eliminar.
        Eliminar la tarea de la lista.
        Mostrar un mensaje indicando que la tarea fue eliminada.

    Función main():
        Inicializar una lista vacía llamada tareas.
        Entrar en un bucle principal que muestra un menú de opciones.
        Permitir al usuario seleccionar una opción del menú.
        Llamar a la función correspondiente según la opción seleccionada.
        Repetir hasta que el usuario elija salir (5).