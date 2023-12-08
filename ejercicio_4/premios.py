def crear():
    
    linombre1=[] 
    limesdeingreso1=[] 
    ligrupo1=[]
    liedad1=[]
    cantidad1=int(input("Digite la cantidad de campersdel grupo basico: "))
    for i in range(cantidad1):
        linombre1.append(input("DIgite el nombre del camper: "))
        limesdeingreso1.append(input("Digite el mes en el que ingreso: "))
        ligrupo1.append(input("Digite el nombre del grupo al cual ingreso: "))
        liedad1.append(int(input("Digite su edad: ")))
    return linombre1, limesdeingreso1, ligrupo1, liedad1

def registrar():
    listatrained1=[]
    trainer1=int(input("Digite la cantidad de trainers del grupo basico: "))
    for o in range(trainer1):
        listatrained1.append(input("Digite el nombre del trained: "))
    return listatrained1

def busqueda(linombre1):
    buscar1=(input("Digite el nombre del camper que desea encontrar: ")) 
    for e in range(buscar1):
        if buscar1 in linombre1: 
            print("el camper esta duplicado")

        else:
            print("El camper no esta duplicado")
   

def eliminar(linombre1):
    eli1=int(input("Digite la cantidad de campers que desea eliminar: "))
    for u in range(eli1):
        o1=(input("DIgite el nombre del camper que desea eliminar: "))
        linombre1.remove(o1)
    return linombre1

def imprimir(linombre1):
    for y in range(len(linombre1)):
        print(f'Nombre de camper: {linombre1[y]}\n'+
              f'Mes de ingreso: {limesdeingreso1[y]}\n'+
              f'Grupo de camper: {ligrupo1[y]}\n'+
              f'Edad del camper: {liedad1[y]}\n')

def agrcamper(linombre1, limesdeingreso1, ligrupo1, liedad1):
    cant1=int(input("Digite la cantidad de campers que desea agregar: "))
    for u in range(cant1):
       linombre1.append(input("DIgite el nombre del camper: "))
       limesdeingreso1.append(input("Digite el mes en el que ingreso: "))
       ligrupo1.append(input("Digite el nombre del grupo al cual ingreso: "))
       liedad1.append(int(input("Digite su edad: ")))
    return linombre1, limesdeingreso1, ligrupo1, liedad1


def mayoramenor(liedad1):
    
    # Combinar los dos arrays en una lista de tuplas (nombre, edad)
        datos_combinados = list(zip(linombre1, liedad1))

    # Ordenar la lista de tuplas por edades (segundo elemento de la tupla)
        datos_ordenados = sorted(datos_combinados, key=lambda x: x[1],  reverse=True)
        
    # Mostrar los resultados
        for nombre, edad in datos_ordenados:
            print(f"Nombre Camper: {nombre}, Edad camper: {edad}")


    


        







option=-1
while option !=0:
    print("------MANTENIMIENTO Y PREMIOS CAMPERS CAMPUS-----")
    print("0. Terminar proceso ")
    print("1. CREAR GRUPO BASICO CON CAMPERS Y SUS DATOS PERSONALES ")
    print("1.1 REGISTRAR EXPERT TRAINER DEL GRUPO BASICO ")
    print("1.2 BUSQUEDA DE CAMPERS DUPLICADOS")
    print("1.3 ELIMINACION DE CAMPERS POR INASISTENCIA ")
    print("1.4 LISTAR CAMPERS ")
    print("1.5 TRANSLADO DE CAMPER ENTRE GRUPOS POR NIVELACION ")
    print("1.6 AGREGAR CAMPERS AL GRUPO (Despues del registro inicial) ")
    print("1.7 REPORTAR CAMPERS DE MAYOR A MENOR EDAD ")


    option=float(input("Digite la opcion que desee: "))

    if option==1:
         linombre1, limesdeingreso1, ligrupo1, liedad1 =crear()

    elif option==1.1:
        listatrained1=registrar()

    elif option==1.2:
        busqueda(linombre1)

    elif option==1.3:
        eliminar(linombre1)

    elif option==1.4:
        imprimir(linombre1)
    
    elif option==1.6:
        agrcamper(linombre1, limesdeingreso1, ligrupo1, liedad1)

    elif option ==1.7:
        mayoramenor(liedad1)
    
  

  



    
    

    
    


