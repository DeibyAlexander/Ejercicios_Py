def registro_votacion():
    # Función principal para gestionar el registro de votación
    universidades = []  # Lista para almacenar información de cada universidad
    numero_universidades = int(input('Ingrese el número de universidades participantes: '))

    # Bucle para recorrer cada universidad
    for i in range(1, numero_universidades + 1):
        nombre_universidad = input(f'Ingrese el nombre de su universidad {i}: ')
        voto_a = 0
        voto_r = 0
        voto_n = 0
        voto_b = 0

        # Bucle para recoger votos de estudiantes de la universidad actual
        while True:
            voto = input(f'Ingrese el voto de un alumno de la universidad {nombre_universidad}, aceptar (A), rechazar (R), nulo (N) o blanco (B). Terminar ingreso de votos (X): ')
            
            # Terminar el ingreso de votos si se ingresa 'X'
            if voto == "X":
                break
            
            # Contabilizar votos según la opción ingresada
            if voto == "A":
                voto_a += 1
            elif voto == "R":
                voto_r += 1
            elif voto == "N":
                voto_n += 1
            elif voto == "B":
                voto_b += 1
            else:
                print('Voto no válido. Ingrese A, R, N, B o X.')

        # Calcular el total de votos y almacenar la información de la universidad
        total_votos = voto_a + voto_r + voto_n + voto_b
        universidades.append({
            'nombre': nombre_universidad,
            'VotoA': voto_a,
            'VotoR': voto_r,
            'VotoN': voto_n,
            'VotoB': voto_b,
            'totalVotos': total_votos
        })
        print(universidades)  # Mostrar la información de la universidad actual

    # Inicializar contadores para resultados finales
    aceptan = rechazan = empate = 0

    # Analizar los resultados de cada universidad
    for universidad in universidades:
        voto_a, voto_r = universidad['VotoA'], universidad['VotoR']
        if voto_a > voto_r:
            aceptan += 1
        elif voto_r > voto_a:
            rechazan += 1
        else:
            empate += 1

    # Mostrar los resultados finales para cada universidad
    for univers in universidades:
        nombre, voto_a, voto_r, voto_n, voto_b = univers['nombre'], univers['VotoA'], univers['VotoR'], univers['VotoN'], univers['VotoB']
        print(f'Numero de universidades: {numero_universidades}\n' +
              f'Universidad: {nombre}\n' +
              f'Voto A: {voto_a}\n' +
              f'Voto R: {voto_r}\n' +
              f'Voto N: {voto_n}\n' +
              f'Voto B: {voto_b}\n' +
              f'{nombre}: {voto_a} Aceptan, {voto_r} Rechazan, {voto_b} Blancos, {voto_n} Nulos\n')


if __name__ == "__main__":
    registro_votacion()
