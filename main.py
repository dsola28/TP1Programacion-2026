import re

#Declaraciones de matrices

mesas = []

horarios_dia = ["12:00","13:00","14:00","15:00"]

horarios_noche = ["20:00","21:00","22:00","23:00"]

id_usado = []



#Función para imprimir reservas
def imprimirMatriz(tabla): 
    print("Titular ====== DNI ====== Tamaño == Turno == Hora")
    for i in range (0, len(tabla)):
        print(tabla[i][0], "======", tabla[i][1],"===", tabla[i][2], "===", tabla[i][3], "===", tabla[i][4])
    return

#Funciones de administrador

def admin():
    print("---------[ ADMIN ]---------")
    print("Elija la acción a realizar: ")
    print("1. Ver las mesas reservadas")
    print("2. Volver al menú principal")
    res = int(input("Ingrese el número de su respuesta: "))
    print("")

    #verificar res dentro de rango
    while res != 1 and res != 2:
             res = int(input("Respuesta Inválida. Ingrese el número de su respuesta: "))
    print("")
    if res == 1:
        print("Lista de mesas Reservadas: ")
        imprimirMatriz(mesas)
        print("")
        print("Perfecto, será redireccionado al menú principal.")
        print("")
        print("---------------------------------------------------")
        return
      
    else: 
        print("Perfecto, será redireccionado al menú principal.")
        print("")
        print("---------------------------------------------------")
        return
    
#Funcion ver reservas noche/mediodia --> admin
#Funcion ver horarios disponibles en la matriz de mesas
#Funcion imprimir --> se llama varias veces

# Función para reservar mesa
def reserva():
    # mesa = [nombre,id,tamaño,turno,horario]
    mesaUsuario = []
    nom = input("Ingrese su nombre (sin apellido): ")
    print("")
    id_user = input("Ingrese su DNI (sin comas ni puntos y si tiene menos de 8 digitos rellenar con 0): ")
    print("")
    while not re.match(r"^\d{8}$", id_user):
        id_user = input("Dni invalido. Ingreselo de nuevo: ")
    while id_user in id_usado:
        id_user = input("Dni invalido, ya fue utilizado. Ingrese uno nuevo: ")
    id_usado.append(id_user)
    tam = int(input("Ingrese el tamaño de grupo que asistirá: "))
    while tam < 0 or tam > 20:
        print("")
        print("El tamaño de grupo ingresado es inválido. Intente nuevamente.")
        tam = int(input("Ingrese el tamaño de grupo que asistirá: "))
    if tam >= 1 and tam <= 4:
        print("")
        print("El tipo de mesa requerida es: Chica.")
        tam = "Chica"
    elif tam >= 5 and tam <= 10:
        print("")
        print("El tipo de mesa requerida es: Mediana.")
        tam = "Mediana"
    else:
        print("")
        print("El tipo de mesa requerida es: Grande.")
        tam = "Grande"

    print("")
    print("Para continuar con su reserva, por favor seleccione el tiempo del día que asistirá: ")
    print("1. Mediodia")
    print("2. Noche")

    turno = int(input("Ingrese el número correspondiente a su respuesta: "))

    while turno != 1 and turno != 2:
        turno = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))

    if turno == 1:
        print("")
        print("Las opciones de horario al mediodía son:")
        for i in range(0,len(horarios_dia)):
            print(f"{i+1}. {horarios_dia[i]}")
        print("")
        hora = int(input("Ingrese el número correspondiente a su respuesta: "))

        while hora != 1 and hora != 2 and hora != 3 and hora != 4:
            hora = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))
            
        i = 0
        while i < len(horarios_dia):
            if hora == i+1:
                hora = horarios_dia[i]
            else:
                i+=1

    else:
        print("")
        print("Las opciones de horario a la noche son: ")
        for i in range(0,len(horarios_noche)):
            print(f"{i+1}. {horarios_noche[i]}")
        print("")

        hora = int(input("Ingrese el número correspondiente a su respuesta: "))

        while hora != 1 and hora != 2 and hora != 3 and hora != 4:
            hora = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))

        i = 0
        while i < len(horarios_noche):
            if hora == i+1:
                hora = horarios_noche[i]
            else:
                i+=1
      
        

    print("Usted eligió el horario: ",hora,"hs .")

    print("-------------------------")
    print("Resumen de su reserva:")
    print("Nombre:", nom)
    print("DNI:", id_user)
    print("Tamaño de mesa:", tam)
    print("Horario:", hora, " hs.")

    print("")

    print("Desea confirmar la reserva?")
    print("1. Si")
    print("2. No")

    reserva = int(input("Ingrese el número correspondiente: "))
    while reserva != 1 and reserva != 2:
        reserva = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))

    #Si el usuario elige confirmar la reserva, el sistema agrega todos sus datos a la matris de mesas reservadas.
    if reserva == 1:
        if hora in horarios_dia:
            horarios_dia.remove(hora)
        else: 
            horarios_noche.remove(hora)
        mesaUsuario.append(nom)
        mesaUsuario.append(id_user)
        mesaUsuario.append(tam)
        mesaUsuario.append(turno)
        mesaUsuario.append(hora)
        mesas.append(mesaUsuario)
        print("Su reserva ha sido confirmada. Lo esperamos en A la mesa!")
        print("")
        print("---------------------------------------------------")
    else:
        print("Usted ha cancelado su reserva. Lo esperamos en otra ocasión.")
    return 

def main():
    terminar = False

    print("Bienvenido a A la mesa!" )

    #código admin: 6767

    while not terminar:
        print("¿Cómo desea ingresar? ")
        print("1. Ingresar como comensal")
        print("2. Ingresar como administrador.")
        res = int(input("Ingrese el número correspondiente a su respuesta: "))

        #verificar res dentro de rango
        while res != 1 and res != 2:
            print("Error número inválido.")
            res = int(input("Ingrese el número correspondiente a su respuesta: "))

        #Comensal
        if res == 1:
            print("---------------------------------------------------")
            print("Bienvenido usuario, que acción desea realizar: ")
            print("1. Hacer una reserva")
            print("2. Ver mi reserva")
            print("3. Eliminar mi reserva")
            ans = int(input("Ingrese el número correspondiente a su respuesta: "))

            #verificar ans dentro de rango
            while ans != 1 and ans != 2 and ans != 3:
                print("Error número inválido.")
                ans = int(input("Ingrese el número correspondiente a su respuesta: "))
                
            #hacer reserva
            if ans == 1:
                print("Perfecto, vamos a realizar la reserva.")
                print("")
                reserva()
            #ver reserva segun dni
            elif ans == 2:
                idUser = input("Ingrese su DNI con el que realizó su reserva: ")
                resv = list(filter(lambda x: x[1] == idUser, mesas))

                if len(resv) != 0:
                    print("")
                    print("Se encontró la siguiente reserva: ")
                    imprimirMatriz(resv)
                    print("")
                    print("---------------------------------------------------")
                else:
                    print("No se encontró ninguna reserva con ese DNI. ")
                    print("")
                    print("---------------------------------------------------")
                
                
            #borrar reserva con filter map
            else:
                idUser = input("Ingrese un DNI con el que realizó su reserva:  ")

                resv = list(filter(lambda x: x[1] == idUser, mesas))
        
                if len(resv) != 0:
                    print("Se encontró la siguiente reserva: ")
                    imprimirMatriz(resv)
                    print("")
                    print("Desea eliminar esta reserva? ")
                    print("1. Si")
                    print("2. No")

                    confirmar = int(input("Ingrese el número correspondiente a su respuesta: "))

                    #verificar res dentro de rango

                    while confirmar != 1 and confirmar != 2:
                        confirmar = int(input("Respuesta inválida. Ingrese el número correspondiente a su respuesta: "))

                    if confirmar == 1:
                        mesas.remove(resv[0])
                        print("Su mesa ha sido eliminada.")
                        print("")
                        print("---------------------------------------------------")
                    else:
                        print("La reserva no fue eliminada.")
                        print("")
                        print("---------------------------------------------------")
                else:
                    print("No se encontró ninguna reserva con ese DNI. ")
                    print("")
                    print("---------------------------------------------------")

        #Administrador
        else: 

            clave = int(input("Ingrese la contraseña de administrador: "))
            ans = 0

            #Verifica la contraseña 

            if clave != 6767:
                print("Contraseña incorrecta, desea reintentar o volver al menú principal?")
                print("1. Reintentar")
                print("2. Volver al menú principal")
                ans = int(input("Ingrese la opción que desea seleccionar: "))

            #Si la contraseña ingresada es incorrecta, se solicita ingresarla nuevamente o volver al menú principal
           
            while ans == 1 and clave != 6767:
                clave = int(input("Ingrese la contraseña de administrador: "))
                if clave != 6767:
                    print("Error, vuelva a intentarlo: ")
                else:
                    ans = 0

            if clave == 6767:
                print("Bienvenido administrador, puede acceder a las funciones de administración.")
                admin()
            else:
                print("Perfecto, será redireccionado al menú inicial")
                


main()