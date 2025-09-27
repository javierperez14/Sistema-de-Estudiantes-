# Sistema-de-Estudiantes-
lista_de_estudiantes = []
afirmacion = True
menu_principal = '''
________________________________________________________________
|                                                              |
|             ==== ===== MENU PRINCIPAL ===== ====             |
|                                                              |
|______________________________________________________________|
|                                                              |
|                  1. Registrar estudiante                     |
|                  2. Lista de estudiantes                     |
|                  3. Buscar estudiante                        |
|                  4. Calcular promedio de calificaciones      |    
|                  5. Salir                                    |
|______________________________________________________________|

'''
while afirmacion:
    print(menu_principal)
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        asignatura = input("Ingrese la asignatura: ")
        calificacion = float(input("Ingrese la calificación: "))
        estudiante = (nombre, asignatura, calificacion)
        lista_de_estudiantes.append(estudiante)
        print(" Estudiante registrado con éxito.")
   
   
    elif opcion =="2":
        if not lista_de_estudiantes:
            print(" No hay estudiantes registrados.")
        else:
            print("\n=== LISTA DE ESTUDIANTES ===")
            for estudiante in lista_de_estudiantes:
                print(f"Nombre: {estudiante[0]}, Asignatura: {estudiante[1]}, Calificación: {estudiante[2]}")
        
        
    elif opcion == "3":
        nombre_a_buscar = input("Ingrese el nombre del estudiante a buscar: ")
        estudiante_encontrado = False
        
        for estudiante in lista_de_estudiantes:
            if estudiante[0].lower() == nombre_a_buscar.lower():
                print(f" Estudiante encontrado: Nombre: {estudiante[0]}, Asignatura: {estudiante[1]}, Calificación: {estudiante[2]}")
                estudiante_encontrado = True
                break

        if not estudiante_encontrado:
            print(" Estudiante no registrado.")

    elif opcion == "4":
        if not lista_de_estudiantes:
            print(" No hay estudiantes para calcular el promedio.")
        else:
            suma_de_calificaciones = 0
            for estudiante in lista_de_estudiantes:
                suma_de_calificaciones += estudiante[2]
            
            promedio_de_calificaciones = suma_de_calificaciones / len(lista_de_estudiantes)
            print(f" El promedio de calificaciones es: {promedio_de_calificaciones:.2f}")

    elif opcion == "5":
        print(" Saliendo del sistema...")
        break

    else:
        print(" Opción inválida. Intente de nuevo.")
