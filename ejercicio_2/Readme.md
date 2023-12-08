Descripción del Problema:

La CONFECH requiere un sistema de registro de votación para agilizar el recuento de votos en las universidades participantes. El sistema debe permitir a los usuarios ingresar el número de universidades participantes, registrar el nombre de cada universidad y los votos de sus alumnos. Al finalizar el proceso, el sistema deberá mostrar los totales de votos para cada universidad y proporcionar un resumen de los resultados generales, indicando cuántas universidades aceptan, cuántas rechazan y cuántas tienen empate entre aceptar y rechazar.

Requerimientos Funcionales:

    Registro de Universidades:
        El sistema debe solicitar al usuario que ingrese el número de universidades participantes.
        Para cada universidad, el sistema debe permitir al usuario ingresar el nombre de la universidad.

    Registro de Votos:
        El sistema debe proporcionar un mecanismo para que el usuario registre los votos de los alumnos de cada universidad.
        Los votos pueden ser de cuatro tipos: aceptar (A), rechazar (R), nulo (N) o blanco (B).
        El registro de votos debe continuar hasta que el usuario decida terminar.

    Cálculo de Resultados:
        El sistema debe calcular y mostrar los totales de votos para cada universidad.
        Debe determinar cuántas universidades aceptan, cuántas rechazan y cuántas tienen empate.
        Los resultados deben presentarse de manera clara y comprensible para el usuario.

    Manejo de Datos:
        El sistema debe almacenar la información de cada universidad y sus votos de manera estructurada, como en una lista de diccionarios.

Estructura del Programa:

    Función registro_votacion():
        Inicializar una lista llamada universidades para almacenar la información de cada universidad.
        Solicitar al usuario que ingrese el número de universidades participantes.
        Para cada universidad:
            Solicitar el nombre de la universidad.
            Inicializar contadores para los tipos de votos.
            Entrar en un bucle para registrar los votos de los alumnos hasta que el usuario decida terminar.
            Calcular el total de votos y agregar la información de la universidad a la lista universidades.
        Calcular y mostrar los resultados generales de la votación.

    Variables y Estructuras de Datos Utilizadas:
        universidades: Lista que almacena diccionarios con la información de cada universidad y sus votos.
        numero_universidades: Número de universidades participantes ingresado por el usuario.
        Contadores para los tipos de votos (Aceptan, Rechazan, Blancos, Nulos).
        Variables para contar cuántas universidades aceptan, cuántas rechazan y cuántas tienen empate.

    Bucles y Estructuras Condicionales:
        Se utilizan bucles for para iterar sobre las universidades y procesar su información.
        Un bucle while se utiliza para registrar los votos de los alumnos hasta que el usuario decida terminar.
        Se utilizan estructuras condicionales if, elif, else para clasificar los tipos de votos.

    Presentación de Resultados:
        El programa presenta los resultados de manera clara y detallada para que el usuario pueda entender fácilmente los totales de votos y los resultados generales.