import re

mesas = []

def imprimirMatriz(tabla): 
    print("Titular ====== DNI ====== Tamaño == Turno == Hora")
    for i in range (0, len(tabla)):
        print(tabla[i][0], "======", tabla[i][1],"===", tabla[i][2], "===", tabla[i][3], "===", tabla[i][4])
    return

def admin():
    print("Bienvenido administrador. Elija la acción a realizar: ")
    print("1. Ver las mesas reservadas")
    print("2. Volver al menú principal")
    res = int(input("Ingrese el número de su respuesta: "))
    
    while res != 1 and res != 2:
             res = int(input("Respuesta Inválida. Ingrese el número de su respuesta: "))
        
    if res == 1:
        print("Lista de mesas Reservadas: ")
        imprimirMatriz()
        print("Perfecto, será redireccionado al menú principal.")
        return
      
    else: 
        print("Perfecto, será redireccionado al menú principal.")
        return
    


#Funcion ver reservas noche/mediodia --> admin
#Funcion ver horarios disponibles en la matriz de mesas
#Funcion imprimir --> se llama varias veces

# Función para reservar mesa
def reserva():
    # mesa = [tamaño,turno,horario]
    mesaUsuario = []
    nom = input("Ingrese su nombre (sin apellido): ")
    id = input("Ingrese su DNI (sin comas ni puntos y si tiene menos de 8 digitos rellenar con 0): ")
    while not re.match(r"^\d{8}$", id):
        id = input("Dni invalido. Ingreselo de nuevo: ")
    tam = int(input("Ingrese el tamaño de grupo que asistirá: "))
    while tam < 0 or tam > 20:
        print("")
        print("El tamaño de grupo ingresado es inválido. Intente nuevamente.")
        tam = int(input("Ingrese el tamaño de grupo que asistirá: "))
    if tam >= 1 and tam <= 4:
        print("")
        print("El tipo de mesa requerida es: chica.")
        tam = "chica"
    elif tam >= 5 and tam <= 10:
        print("")
        print("El tipo de mesa requerida es: mediana.")
        tam = "mediana"
    else:
        print("")
        print("El tipo de mesa requerida es: grande.")
        tam = "grande"

    print("")
    print("Para continuar con su reserva, por favor seleccione el tiempo del día que asistirá: ")
    print("1. Mediodia")
    print("2. Noche")
    print("")

    turno = int(input("Ingrese el número correspondiente a su respuesta: "))

    while turno != 1 and turno != 2:
        turno = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))

    if turno == 1:
        print("Las opciones de horario al mediodía son:")
        print("1. 12:00")
        print("2. 13:00")
        print("3. 14:00")
        print("4. 15:00")

        hora = int(input("Ingrese el número correspondiente a su respuesta: "))

        while hora != 1 and hora != 2 and hora != 3 and hora != 4:
            hora = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))

        if hora == 1:
            hora = "12:00"
        elif hora == 2:
            hora = "13:00"  
        elif hora == 3:
            hora = "14:00"
        else:
            hora = "15:00"


        print("Usted eligió el horario: ",hora,"hs .")
        print("Desea confirmar reserva")
        print("1. Si")
        print("1. No")
                       

    else:
        print()
        print("Las opciones de horario a la noche son: ")
        print("1. 20:00")
        print("2. 21:00")
        print("3. 22:00")
        print("4. 23:00")


        hora = int(input("Ingrese el número correspondiente a su respuesta: "))

        while hora != 1 and hora != 2 and hora != 3 and hora != 4:
            hora = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))
    

        if hora == 1:
            hora = "20:00"
        elif hora == 2:
            hora = "21:00"  
        elif hora == 3:
            hora = "22:00"
        else:
            hora = "23:00"


    print("Usted eligió el horario: ",hora,"hs .")
    print("Desea confirmar reserva")
    print("1. Si")
    print("2. No")

    reserva = int(input("Ingrese el número correspondiente: "))
    while reserva != 1 and reserva != 2:
        reserva = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))
    if reserva == 1:
        mesaUsuario.append(nom)
        mesaUsuario.append(id)
        mesaUsuario.append(tam)
        mesaUsuario.append(turno)
        mesaUsuario.append(hora)
        mesas.append(mesaUsuario)
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
            print("Bienvenido usuario, que acción desea realizar: ")
            print("1. Hacer una reserva")
            print("2. Ver mi reserva")
            print("3. Eliminar mi reserva")
            ans = int(input("Ingrese el número correspondiente a su respuesta: "))

            #verificar ans dentro de rango}
            while ans != 1 and ans != 2 and ans != 3:
                print("Error número inválido.")
                ans = int(input("Ingrese el número correspondiente a su respuesta: "))
                
            #hacer reserva
            if ans == 1:
                print("Perfecto, vamos a realizar la reserva.")
                reserva()
                
            #ver reserva segun dni
            elif ans == 2:
                id = int(input("Ingrese su DNI con el que realizó su reserva: "))
                resv = list(filter(lambda x: id in x, mesas))
                imprimirMatriz(resv)  
                
            #borrar reserva con filter map
            else:
                
                print()

        #Administrador
        else: 
            clave = int(input("Ingrese la contraseña de administrador: "))
            ans = 0
            if clave != 6767:
                print("Contraseña incorrecta, desea reintentar o volver al menú principal?")
                print("1. Reintentar")
                print("2. Volver al menú principal")
                ans = int(input("Ingrese la opción que desea seleccionar: "))

            while ans == 1 and clave != 6767:
                clave = int(input("Ingrese la contraseña de administrador: "))
                if clave != 6767:
                    print("Error, vuelva a intentarlo: ")
                else:
                    ans = 0

            if clave == 1010:
                print("Bienvenido administrador, puede acceder a las funciones de administración.")
                admin()
            else:
                print("Perfecto, será redireccionado al menú inicial")
                


main()