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
    return



def main():
    res = input("Bienvenedido a A la mesa!, desea realizar una reserva? (si/no)(en caso de ser administrador, ingrese el código de acceso): "))
    #código admin: 1010
    if res == "si":
        print("Perfecto, vamos a realizar la reserva.")
        # función reserva
    elif res == "1010":
        print("Bienvenido administrador, puede acceder a las funciones de administración.")
        # función admin
    elif res == "no":
        print("Gracias por su visita, esperamos verlo pronto.")

main()

