
mesas = [["nombre","dni","tamaño mesa","turno","horario"]]


def admin():
    print("Bienvenido administrador. Desea ver las mesas?")
    print("1. Si")
    print("2. No")
    res = int(input("Ingrese el número de su respuesta"))
    while res != 1 and res != 2:
             res = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))
    if res == 1:
        print("Lista de mesas disponibles: ")
        print("Lista de mesas Reservadas: ")

    else: 
        print("Perfecto, será redireccionado al menú principal.")

    return

#Función para borrar reservas --> la llama el usuario o el admin dependiendo desde donde se llame la función.
'''def delM(): 
    print("Mesas disponibles: " m_reservadas[])
    cancel = int(input("'¿Que reserva desea cancelar?"))
        if (cancel in lista):
            delete m_reservadas[i]
            print(mesa: m_reservadas[i] cancelada) 
       else:
            print("esta mesa no esta reservada")
            cancel = int(input("¿Que reserva desea cancelar?"))
    return
'''

#Funcion ver reservas noche/mediodia --> admin

#Funcion imprimir --> se llama varias veces

# Función para reservar mesa
def reserva():
    # mesa = [tamaño,turno,horario]
    nom = input("Ingrese su nombre (sin apellido): ")
    id = int(input("Ingrese su DNI (sin comas ni puntos): "))
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
            print("1. No")





    return 



def main():
    terminar = False
    print("Bienvenido a A la mesa!" )
    #código admin: 1010
    while not terminar:
        print("Desea realizar una reserva? (si/no) (en caso de ser administrador, ingrese el código de acceso): ")
        print("1. Sí")
        print("2. No")
        print("Ingrese el código para acceder como administrador.")
        res = int(input("Ingrese el número correspondiente a su respuesta: "))
        if res == 1:
            print("Perfecto, vamos a realizar la reserva.")
            reserva()
        elif res == 1010:
            print("Bienvenido administrador, puede acceder a las funciones de administración.")
            admin()
        elif res == 2:
            print("Gracias por su visita, esperamos verlo pronto.")
            terminar = True


main()

