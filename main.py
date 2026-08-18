def admin():
    return

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