def admin():
    return

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
