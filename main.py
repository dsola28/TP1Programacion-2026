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

#Función para borrar reservas
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

#Funcion ver reservas noche/mediodia

# Función para reservar mesa
def reserva():
    # mesa = [tamaño,turno,horario]
    mesa = int(input("Ingrese el tamaño de grupo que asistirá: "))

    while mesa < 0 or mesa > 20:
        print("")
        print("El tamaño de grupo ingresado es inválido. Intente nuevamente.")
        mesa = int(input("Ingrese el tamaño de grupo que asistirá: "))
    if mesa < 0:
        print("")
        print("El tamaño de grupo ingresado es inválido. Intente nuevamente.")
    elif mesa >= 1 and mesa <= 4:
        print("")
        print("El tipo de mesa requerida es: chica.")
    elif mesa >= 5 and mesa <= 10:
        print("")
        print("El tipo de mesa requerida es: mediana.")
    elif mesa >= 11 and mesa <= 20:
        print("")
        print("El tipo de mesa requerida es: grande.")
    else:
        print("")
        print("El tamaño de grupo ingresado es demasiado grande para reservar.")

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

        print("Usted eligió el horario: ",hora,"hs .")
    
    else:
        print("Las opciones de horario a la noche son: ")
        print("1. 20:00")
        print("2. 21:00")
        print("3. 22:00")
        print("4. 23:00") 

        while hora != 1 and hora != 2 and hora != 3 and hora != 4:
            hora = int(input("Ingrese el número correspondiente a su respuesta: "))
    
            print("Se reservó su pedido. Disfrute su comida.")



    return mesa, hora, turno



def main():
    print()
    print("Bienvenido a A la mesa!, desea realizar una reserva? (si/no) (en caso de ser administrador, ingrese el código de acceso): ")
    #código admin: 1010
    print("1. Sí")
    print("2. No")
    print("Ingrese el código para acceder como administrador.")
    res = int(input("Ingrese el número correspondiente a su respuesta: "))
    if res == 1:
        print()
        print("Perfecto, vamos a realizar la reserva.")
        reserva()
    elif res == 1010:
        print()
        print("Bienvenido administrador, puede acceder a las funciones de administración.")
        admin()
    elif res == 2:
        print()
        print("Gracias por su visita, esperamos verlo pronto.")


main()

