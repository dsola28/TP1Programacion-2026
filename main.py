import re
import json
import os

# generación y manejo del archivo json
id_usado = []

tipo_mesa = ((1, 4, "chica"),(5, 10, "mediana"),(11, 20, "grande"))


# formato "plantilla" del salon y sus mesas segun horarios

mesas_e = { 
    ("mediodia"): {
        "12:00" : {
            "chica":[1,2,3,4],
            "mediana":[5,6,7],
            "grande":[8,9] 
        },
        "13:00" : {
            "chica":[1,2,3,4],
            "mediana":[5,6,7],
            "grande":[8,9]
        },
        "14:00" : {
            "chica":[1,2,3,4],
            "mediana":[5,6,7],
            "grande":[8,9]
        },
        "15:00" : {
            "chica":[1,2,3,4],
            "mediana":[5,6,7],
            "grande":[8,9]
        }
    },
    ("noche"): {
        "20:00" : {
            "chica":[1,2,3,4],
            "mediana":[5,6,7],
            "grande":[8,9]
        },
        "21:00" : {
            "chica":[1,2,3,4],
            "mediana":[5,6,7],
            "grande":[8,9]
        },
        "22:00" : {
            "chica":[1,2,3,4],
            "mediana":[5,6,7],
            "grande":[8,9]
        },
        "23:00" : {
            "chica":[1,2,3,4],
            "mediana":[5,6,7],
            "grande":[8,9]
        }
    }

}

def generar_archivo(nombre_archivo,mesas_e):
    try:
        with open(nombre_archivo, "w", encoding="UTF-8") as archivo:
            json.dump(mesas_e, archivo, ensure_ascii=False, indent=4)
    except TypeError as error:
        print("ERROR, hay un dato que no se puede guardar en el JSON:", error)
    except OSError as error:
        print("ERROR al generar el archivo:", error)
    else:
        print("Archivo JSON generado correctamente.")


def traer_horarios(nombre_archivo,tipo,turno):
    h=[]
    try:
        with open(nombre_archivo,"r",encoding="UTF-8") as archivo:
            m = json.load(archivo)
            t = m[turno]
            for hora,tam in t.items():
                if tipo in tam and len(tam[tipo]) != 0:
                    h.append(hora)
    except FileNotFoundError as error:
        print("Error, el archivo no existe")
    except KeyError as error:
        print("Error, no se encontró en el archivo la clave:", error)
    except ValueError as error:
        print("Error, el archivo JSON tiene un formato inválido:", error)
    except OSError as error:
        print("Error al generar el archivo: ", error)
    return h


def borrar_mesa_reserva(nombre_archivo,tipo,turno,hora):
    num_mesa = None
    try:
        with open(nombre_archivo,"r",encoding="UTF-8") as archivo:
            mesas = json.load(archivo)
            num_mesa = mesas[turno][hora][tipo][0]
            mesas[turno][hora][tipo].pop(0)
        with open(nombre_archivo, "w") as archivo:
            json.dump(mesas, archivo, indent=4)
    except FileNotFoundError as error:
        print("Error, el archivo no existe")
    except KeyError as error:
        print("Error, no se encontró en el archivo la clave:", error)
    except IndexError as error:
        print("Error, no quedan mesas disponibles de ese tipo en ese horario")
    except ValueError as error:
        print("Error, el archivo JSON tiene un formato inválido:", error)
    return num_mesa

# generación y manejo del archivo txt


def generar_reservas(reservas_arch):
    try:
        with open(reservas_arch, "w", encoding="UTF-8") as archivo:
            archivo.write("Mesas reservadas: \n\n")
        archivo.close()
    except OSError as error:
        print("ERROR al trabajar con el archivo:", error)


#funciona 
def agregar_r(reservas_arch,m):
    try:
        with open(reservas_arch,"a",encoding="UTF-8") as archivo:
            archivo.write(f"{m}\n\n")
    except FileNotFoundError as error:
        print("Error, el archivo no existe")    
    except OSError as error:
        print("Error al trabajar con el archivo: ",error)
    return



#Busca una reserva en el archiov txt segun el dni ingresado, y si la encunetra la guarda en un diccionario y marca True para la funcion main
def buscar_reserva(reservas_arch,dni):
    encontrada = False
    reserva = {}
    try:
        with open(reservas_arch,"r",encoding="UTF-8") as archivo:
            for linea in archivo:
                if len(linea) > 3 and "'" in linea:
                    partes = linea.strip().split("'")
                    if int(partes[7]) == dni:
                        reserva = {
                            "nombre" : partes[3],
                            "dni" : partes[7],
                            "tipo" : partes[11],
                            "numero" : partes[15],
                            "turno" : partes[19],
                            "horario" : partes[23]
                        }
                        encontrada = True
                        archivo.close()
                        return reserva, encontrada
            archivo.close()
    except FileNotFoundError as error:
        print("Error, el archivo no existe")
    except IndexError as error:
        print("Error, hay una reserva con formato incorrecto en el archivo")
    except ValueError as error:
        print("Error, hay un DNI con formato inválido en el archivo")
    except OSError as error:
        print("Error al trabajar con el archivo: ",error)
    return reserva, encontrada
        
#Listo funciona 
#Borra reserva del txt segun dni, y luego vuelve a ingresar al json el numero de la mesa para que vuelva a estar disponible
def borrar_reserva(reservas_arch,dni):
    num_mesa = 0
    turno = ""
    hora = ""
    tipo = ""
    try:
        with open(reservas_arch, "r", encoding="UTF-8") as archivo, open("temporal.txt", "w", encoding="UTF-8") as temporal:
            for linea in archivo:
                if len(linea) > 3 and "'" in linea:
                    datos = linea.strip().split("'")
                    if int(datos[7]) == dni:
                        # Es la reserva a borrar: no se copia
                        # y se salta la línea en blanco que le sigue
                        tipo = datos[11]
                        num_mesa = int(datos[15])
                        turno = datos[19]
                        hora = datos[23]
                        archivo.readline()
                    else:
                        temporal.write(linea)
                else:
                    # Encabezado "Mesas reservadas:" y líneas en blanco
                    temporal.write(linea)
        archivo.close()
        temporal.close()
        os.replace("temporal.txt", reservas_arch)
        print("Reserva eliminada correctamente.")
      
        with open(nombre_archivo,"r",encoding="UTF-8") as archivo:
            mesas = json.load(archivo)
            mesas[turno][hora][tipo].append(num_mesa)
            archivo.close()
        with open(nombre_archivo, "w") as archivo:
            json.dump(mesas, archivo, indent=4)
            
    except FileNotFoundError:
        print("Error, el archivo no existe")
    except IndexError:
        print("Error, hay una reserva con formato incorrecto en el archivo")
    except KeyError as error:
        print("Error, no se encontró en el archivo la clave:", error)
    except ValueError:
        print("Error, hay un dato con formato inválido en el archivo")
    return


#funcion para admin para imprimir todas las reservas hechas
def imprimir_reservas(reservas_arch):
 # Abrimos el archivo en modo lectura
    try:
        archivo = open(reservas_arch, "r", encoding="UTF-8")

        print("Reservas: \n")
        print("-"*30)
        # Recorremos directamente el archivo
        for linea in archivo:
            # Verificamos que la línea tenga texto y además contenga comillas
            if len(linea) > 3 and "'" in linea:
                partes = linea.strip().split("'")
                # Ahora es seguro acceder a los índices
                nombre =  partes[3]
                dni =  partes[7]
                tipo =  partes[11]
                num_mesa = partes[15]
                turno = partes[19]
                horario = partes[23]
                
                print(F'Nombre:             {nombre}')
                print(F'DNI:                {dni}')
                print(F'Tipo de mesa:       {tipo}')
                print(F'Turno:              {turno}')
                print(F'Horario             {horario}')
                print(F'Número de mesa:     {num_mesa}')
                print("-"*30)
        archivo.close()
    except FileNotFoundError:
        print("Error, el archivo no existe")
    except IndexError:
        print("Error, hay una reserva con formato incorrecto en el archivo")
#modificar

def mesas_disponibles(nombre_archivo, plantilla):
    try:
        with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
            actual = json.load(archivo)
    except FileNotFoundError:
        print("Error, el archivo no existe")
        return
    except ValueError:
        print("Error, el archivo JSON tiene un formato inválido")
        return

    try:
        print("Mesas disponibles:")
        for turno, horarios in actual.items():
            print("-" * 30)
            print(f"Turno: {turno}")
            print("-" * 30)
            libres_por_hora = []  
            for hora, tipos in horarios.items():
                print("\n")
                print("-" * 30)
                print(f"\n  Hora: {hora}")
                libres_hora = set()
                for tipo, numeros in tipos.items():
                    libres = set(numeros)
                    todas = set(plantilla[turno][hora][tipo])
                    #diferencia
                    reservadas = todas - libres         
                    #union
                    libres_hora |= libres
                    print(f"    {tipo}: libres {sorted(libres)} - reservadas {sorted(reservadas)}")

                libres_por_hora.append(libres_hora)

            # Intersección: mesas libres en TODOS los horarios del turno
            if libres_por_hora:
                siempre_libres = set.intersection(*libres_por_hora)
                print("\n")
                print("-" * 30)
                print(f"\n  Libres en todos los horarios de {turno}: {sorted(siempre_libres)}")
    except KeyError as error:
        print("Error, no se encontró en la plantilla la clave:", error)
    except TypeError:
        print("Error, el archivo JSON tiene datos con un tipo incorrecto")
#Funciones de administrador

def admin():
    try:
        print("-"*30)
        print("\nBienvenido administrador, ahora podrá acceder a las funciones de administración.\n")
        print("Elija la acción a realizar:\n1. Ver las mesas reservadas\n2. Ver las mesas Disponibles\n3. Volver al menú principal\n")
        res = int(input("Ingrese el número de su respuesta: "))
        print("\n")

        #verificar res dentro de rango
        while res != 1 and res != 2 and res!= 3:
            res = int(input("Respuesta Inválida. Ingrese el número de su respuesta: "))
        print("\n")

        if res == 1:
            imprimir_reservas(reservas_arch)
            print("\nPerfecto, será redireccionado al menú principal.\n")
            print("-"*30)
            return
        elif res == 2:
            mesas_disponibles(nombre_archivo,mesas_e)
        else: 
            print("Perfecto, será redireccionado al menú principal.")
            print("\n")
            print("-"*30)
            return
    except ValueError:
        print("\nError, debe ingresar un número entero. Será redireccionado al menú principal.\n")



#funciona

#Función para obtener que tipo de mesa segun cantidad de invitados
def verificar_tipo(t):
    tipo = ""
    for fila in tipo_mesa:
        if t >= fila[0] and t <= fila[1]:
            tipo = fila[2]

    return tipo


# Función para reservar mesa
def reserva():
    # mesa = [nombre,id,tamaño,turno,horario]
    try:
        mesaUsuario = []
        nom = input("Ingrese su nombre (sin apellido): ")
        print("\n\n")
        id_user = input("Ingrese su DNI (sin comas ni puntos y si tiene menos de 8 digitos rellenar con 0): ")
        print("\n\n")
        while not re.match(r"^\d{8}$", id_user):
            id_user = input("Dni invalido. Ingreselo de nuevo: ")
        while id_user in id_usado:
            id_user = input("Dni invalido, ya fue utilizado. Ingrese uno nuevo: ")
        tam = int(input("Ingrese el tamaño de grupo que asistirá: "))
        while tam < 0 or tam > 20:
            print("\n\n")
            print("El tamaño de grupo ingresado es inválido. Intente nuevamente.")
            tam = int(input("Ingrese el tamaño de grupo que asistirá: "))
        tipo = verificar_tipo(tam)
        print(f"Usted ha elegido una mesa del tipo: {tipo} para un grupo de {tam} personas.\n\n")
        print("Para continuar con su reserva, por favor seleccione el tiempo del día que asistirá:\n1. Mediodia\n2. Noche\n")
        turno = int(input("Ingrese el número correspondiente a su respuesta: "))

        #Verifica respuesta dentro de rango
        while turno != 1 and turno != 2:
            turno = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))

        if turno == 1:
            turno = "mediodia"
        else:
            turno = "noche"

        #Funcion que trae horarios disponibles en el turno elegido para el tipo de mesa necesaria
        horarios = traer_horarios(nombre_archivo,tipo,turno)

        #Si no encuentra horarios disponibles, le ofrece al usuario la posibilidad de ver los horarios del otro turno, o cancelar la reserva
        while horarios == []:
            print("No hay horarios disponibles para el tipo de mesa y turno seleccionado. Por favor intente nuevamente.")
            print("Desea ver los horarios del otro turno?")
            resp = int(input("1. Si\n2. No, no deseo continuar con la reserva\nIngrese el número correspondiente a su respuesta: "))
            while resp != 1 and resp != 2:
                turno = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))
            if resp == 1:
                if turno == "mediodia":
                    turno = "noche"
                else:
                    turno = "mediodia"
                horarios = traer_horarios(nombre_archivo,tipo,turno)
            else:
                print("Usted ha cancelado su reserva. Lo esperamos en otra ocasión.")
                return

        print(f"Las opciones de horario en el turno: {turno}, son:")
        for i in range(0,len(horarios)):
            print(f"{i+1}. {horarios[i]}")
        hora = int(input("Ingrese el número correspondiente a su respuesta: "))

        #Verifica respuesta dentro de rango
        while hora != 1 and hora != 2 and hora != 3 and hora != 4:
            hora = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))
                
        i = 0
        while i < len(horarios):
            if hora == i+1:
                hora = horarios[i]
            else:
                i+=1

        print(f"Usted eligió el horario: {hora}hs .")

        print("-"*30)
        print("Resumen de su reserva:")
        print("Nombre:", nom)
        print("DNI:", id_user)
        print("Tamaño de mesa:", tam)
        print("Horario:", hora, " hs.\n\n")

        print("Desea confirmar la reserva?\n\n1. Si\n2. No\n")
        reserva = int(input("Ingrese el número correspondiente: "))

        #Verifica respuesta dentro de rango
        while reserva != 1 and reserva != 2:
            reserva = int(input("Respuesta Inválida. Ingrese el número de su respuesta"))

        #Si el usuario decide confirmar su reserva, el sistema lo agrega todo a un diccionario que luego se envia al archivo txt
        if reserva == 1:
            id_usado.append(id_user) # ahora solo guarda el dni cuando confirma la reserva
            num = borrar_mesa_reserva(nombre_archivo,tipo,turno,hora)
            mesa = {
                "nombre" : nom,
                "dni" : id_user,
                "tipo_mesa" : tipo,
                "num_mesa" : str(num),
                "turno"  : turno,
                "hora" : hora
            }
            
            agregar_r(reservas_arch,mesa)
          
            print("Su reserva ha sido confirmada. Lo esperamos en A la mesa!")
            print("-"*30)
        else:
            print("Usted ha cancelado su reserva. Lo esperamos en otra ocasión.")
        return 
    except ValueError:
        print("\nError, debe ingresar un número entero. La reserva fue cancelada.\n")
        return

def main():
    terminar = False
    print("Bienvenido a A la mesa!\n" )

    #código admin: 6767

    while not terminar:
        try:
            print("¿Cómo desea ingresar?\n1. Ingresar como comensal\n2. Ingresar como administrador.\n")
            res = int(input("Ingrese el número correspondiente a su respuesta: "))

            #verificar res dentro de rango
            while res != 1 and res != 2:
                print("Error número inválido.")
                res = int(input("Ingrese el número correspondiente a su respuesta: "))
                
            #Comensal
            if res == 1:
                print("-"*30)
                print("Bienvenido usuario, que acción desea realizar:\n1. Hacer una reserva\n2. Ver mi reserva\n3. Eliminar mi reserva")
                ans = int(input("Ingrese el número correspondiente a su respuesta: "))

                #verificar ans dentro de rango
                while ans != 1 and ans != 2 and ans != 3:
                    print("Error número inválido.")
                    ans = int(input("Ingrese el número correspondiente a su respuesta: "))
                    
                #hacer reserva
                if ans == 1:
                    print("Perfecto, vamos a realizar la reserva.\n")
                    reserva()


                #ver reserva segun dni
                elif ans == 2:
                    idUser = int(input("Ingrese su DNI con el que realizó su reserva: "))
                    resv, e = buscar_reserva(reservas_arch,idUser)
                    if e :
                        imprimir_reserva = lambda d: [print(f"{k}: {v}") for k, v in d.items()]
                        imprimir_reserva(resv)
                    else:
                        print("No se encontró ninguna reserva con ese DNI.\n ")
                        print("-"*30)
                    
                #borrar reserva con filter map
                else:
                    idUser = int(input("Ingrese un DNI con el que realizó su reserva:  "))
                    resv, e = buscar_reserva(reservas_arch,idUser)
                    if e:
                        confirmar = int(input("Desea eliminar esta reserva? \n1. Si\n2. No\n\nIngrese el número correspondiente a su respuesta: "))
                        while confirmar != 1 and confirmar != 2:
                            confirmar = int(input("Respuesta inválida. Ingrese el número correspondiente a su respuesta: "))
                        if confirmar == 1:
                            borrar_reserva(reservas_arch,idUser)
                        else:
                            print("\nPerfecto, no se borrará la reserva, será redireccionado al menú inicial.")

                    else:
                        print("\nNo se encontró ninguna reserva con ese DNI.\n ")
                        print("-"*30)
                    

            #Administrador
            else: 

                clave = int(input("Ingrese la contraseña de administrador: "))
                ans = 0

                #Verifica la contraseña 

                if clave != 6767:
                    print("Contraseña incorrecta, desea reintentar o volver al menú principal?\n1. Reintentar\n2. Volver al menú principal\n")
                    ans = int(input("Ingrese la opción que desea seleccionar: "))

                #Si la contraseña ingresada es incorrecta, se solicita ingresarla nuevamente o volver al menú principal
               
                while ans == 1 and clave != 6767:
                    clave = int(input("\nIngrese la contraseña de administrador: "))
                    if clave != 6767:
                        print("\nError, vuelva a intentarlo: ")
                    else:
                        ans = 0

                if clave == 6767:
                    print("-"*30)
                    print("\nBienvenido administrador, puede acceder a las funciones de administración.")
                    admin()
                else:
                    print("Perfecto, será redireccionado al menú inicial\n")
                    print("-"*30)
        except ValueError:
            print("\nError, debe ingresar un número entero. Será redireccionado al menú inicial.\n")
            print("-"*30)


reservas_arch = "mesas_reservadas.txt"               
nombre_archivo = "mesas_existentes.json"
generar_reservas(reservas_arch)
generar_archivo(nombre_archivo,mesas_e)



main()