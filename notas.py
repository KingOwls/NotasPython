import os
alumnos = []
isActive = True
menu = "1.Registrar alumno\n2.Registrar Notas\n3.Salir\n"
subMenuNotas = ["1. Parciales", "2.Quices", "3. Trabajos", "4. Regresar al menu principal"]
opMenu=0
while isActive:
    os.system("cls")
    try:
        opMenu= int(input(menu))
    except ValueError:
        print("Error al dato de ingreso")
        os.system("pause")
    else:
        if(opMenu== 1 ):
            rta = "S"
            while(rta in ["S", "s"]):
                codigo = input("ingrese el Codigo del Estudiante: ")
                nombre = input("ingrese el Nombre del Estudiante: ")
                edad = int(input("ingrese la edad del Estudiante: "))
                alumno = [codigo, nombre, edad, [], [], []]
                alumnos.append(alumno)
                print(alumnos)
                os.system("pause")
                rta = input("Desea registrar otro alumno S(si) o N (no)").upper()
        elif(opMenu== 2 ):
            if(len(alumnos)>=0):
                opNotas = 0
                isActiveGrades = True
                while isActiveGrades:
                    os.system("cls")
                    for i, item in enumerate(subMenuNotas):
                        print(f"{i+1}. {item}")
                    try:
                        opNotas = int(input(":)  "))                
                    except ValueError:
                        print("Error al dato de ingreso")
                        os.system("pause")
                    else:
                        if(opNotas==1):
                            rta = "S"
                            Buscador = input("Ingrese el codigo del estudiante:  ")
                            for item in alumno:
                                if Buscador in item:
                                    indice = alumno.index(item)
                            while bool(input("Desea iniciar con el registro S(si) o N (no)")):
                                while (rta in ["S", "s"]):
                                    nota=float ("ingrese la nota del parcial:  ")
                                    alumnos[Buscador][3].append(nota)
                                    print(alumnos)
                                    os.system("pause")
                                    rta = input("Desea registrar otra nota S(si) o N (no)").upper()
                                if bool(input ("Desea registrar otro estudiante S(si) o N(no)")):
                                    Buscador = input("Ingrese codigo del estudiante:   ")
                                    rta = "S"
                                    for item in alumno:
                                        if Buscador in item:
                                            indice = alumno.index(item)
                                isAddGrades = bool(input("Desea iniciar con el registro S(si) o N(no)"))
                        elif(opNotas==2):
                            rta = "S"
                            Buscador = input("Ingrese el codigo del estudiante:  ")
                            for item in alumno:
                                if Buscador in item:
                                    indice = alumno.index(item)
                            while bool(input("Desea iniciar con el registro S(si) o N (no)")):
                                while (rta in ["S", "s"]):
                                    nota=float ("ingrese la nota del parcial:  ")
                                    alumnos[Buscador][4].append(nota)
                                    print(alumnos)
                                    os.system("pause")
                                    rta = input("Desea registrar otra nota S(si) o N (no)").upper()
                                if bool(input ("Desea registrar otro estudiante S(si) o N(no)")):
                                    Buscador = input("Ingrese codigo del estudiante:   ")
                                    rta = "S"
                                    for item in alumno:
                                        if Buscador in item:
                                            indice = alumno.index(item)
                                isAddGrades = bool(input("Desea iniciar con el registro S(si) o N(no)"))
            elif(opNotas==3):
                        rta = "S"
                        Buscador = input("Ingrese el codigo del estudiante:  ")
                        for item in alumno:
                            if Buscador in item:
                                indice = alumno.index(item)
                        while bool(input("Desea iniciar con el registro S(si) o N (no)")):
                            while (rta in ["S", "s"]):
                                nota=float ("ingrese la nota del parcial:  ")
                                alumnos[Buscador][5].append(nota)
                                print(alumnos)
                                os.system("pause")
                                rta = input("Desea registrar otra nota S(si) o N (no)").upper()
                            if bool(input ("Desea registrar otro estudiante S(si) o N(no)")):
                                Buscador = input("Ingrese codigo del estudiante:   ")
                                rta = "S"
                                for item in alumno:
                                    if Buscador in item:
                                        indice = alumno.index(item)
                            isAddGrades = bool(input("Desea iniciar con el registro S(si) o N(no)"))
            elif(opNotas==4):
                        isActiveGrades = False
            else:
                print("opcion invadila")
        elif(opMenu==3):
            os.system("cls")
            print("gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("opcion invadila")
    os.system("pause")
    #Agregar el ordenamiento de los estudiantes
    #Conservacion de datos
    #colocar ordenamniento de estudiante y nota final