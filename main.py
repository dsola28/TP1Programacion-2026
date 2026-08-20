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
# Función para reservar mesa
def reserva():
    mesa = int(input("Ingrese el tamaño de grupo que asistirá: "))
    if  mesa != 0:
        if mesa < 0:
            print()
            print("El tamaño de grupo ingresado es inválido. Intente nuevamente.")
        elif mesa >= 1 and mesa <= 4:
            print()
            print("El tipo de mesa requerida es: chica.")
        elif mesa >= 5 and mesa <= 7:
            print()
            print("El tipo de mesa requerida es: mediana.")
        elif mesa >= 8 and mesa <= 20:
            print()
            print("El tipo de mesa requerida es: grande.")
        else:
            print()
            print("El tamaño de grupo ingresado es demasiado grande para reservar.")

    print()
    print("Para continuar con su reserva, por favor seleccione el turno deseado: ")
    print("1. Mañana")
    print("2. Tarde")
    print("3. Noche")
    print()

    turno = int(input("Ingrese el número correspondiente a su respuesta: "))

    if turno == 1:
        print()
        print("Las opciones de horario a la mañana son:")
        print("1. 8:00")
        print("2. 9:30")
        print("3. 11:00")
        print()

        horario = int(input("Ingrese el número correspondiente a su respuesta: "))

        if horario == 1:
            print()
            print("Se reservó su pedido. Disfrute su comida.")
        elif horario == 2:
            print()
            print("Se reservó su pedido. Disfrute su comida.")
        else:
            print("Se reservó su pedido. Disfrute su comida.")

    elif turno == 2:
        print()
        print("Las opciones de horario a la tarde son: ")
        print("1. 13:00")
        print("2. 14:30")
        print("3. 16:00")
        print("4. 17:30")
        print()

        horario = int(input("Ingrese el número correspondiente a su respuesta: "))
        
        if horario == 1:
            print()
            print("Se reservó su pedido. Disfrute su comida.")
        elif horario == 2:
            print()
            print("Se reservó su pedido. Disfrute su comida.")
        elif horario == 3:
            print()
            print("Se reservó su pedido. Disfrute su comida.")
        else:
            print("Se reservó su pedido. Disfrute su comida.")
    else:
        print()
        print("Las opciones de horario a la noche son: ")
        print("1. 19:00") 
        print("2. 20:30")
        print("3. 22:00")
        print()

        horario = int(input("Ingrese el número correspondiente a su respuesta: "))
        if horario == 1:
            print()
            print("Se reservó su pedido. Disfrute su comida.")
        elif horario == 2:
            print()
            print("Se reservó su pedido. Disfrute su comida.")
        else:
            print()
            print("Se reservó su pedido. Disfrute su comida.")

    return mesa, horario, turno



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

