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
            print("Ha ocurrido un error. Intente nuevamente.")
        elif mesa >= 1 and mesa <= 4:
            print("El tipo de mesa requerida es: chica.")
        elif mesa >= 5 and mesa <= 7:
            print("El tipo de mesa requerida es: mediana.")
        elif mesa >= 8 and mesa <= 20:
            print("El tipo de mesa requerida es: grande.")
        else:
            print("El tamaño de grupo ingresado es demasiado grande para reservar.")
    return mesa



def main():
    print("Bienvenido a A la mesa!, desea realizar una reserva? (si/no) (en caso de ser administrador, ingrese el código de acceso): ")
    #código admin: 1010
    print("1. Sí")
    print("2. No")
    print("Ingrese el código para acceder como administrador")
    res = int(input("Ingrese el número correspondiente a su respuesta: "))
    if res == 1:
        print("Perfecto, vamos a realizar la reserva.")
        reserva()
    elif res == 1010:
        print("Bienvenido administrador, puede acceder a las funciones de administración.")
        admin()
    elif res == 2:
        print("Gracias por su visita, esperamos verlo pronto.")


main()

