from FuncionPDF import *
from DatosEstaticos import *
import os
import time
import sys

#------------Menu
print("Bienvenidos a la concecionaria Dacia")
print("---------------")
def menu():
    opcion="1"
    while(opcion!="7"):
        print("1. Usuario existente")
        print("2. Nuevo usuario")
        print("3. Vendedor que te va entender")
        print("4. Imprimir Datos de usuarios existentes")
        print("5. Encuesta")
        print("6. Generar PDF")
        print("7. Salir")
        opcion = input("Elige una opcion ")
        os.system('cls')
        if(opcion=="1"):
            Usuarios()
        elif(opcion=="2"):
            pedirDatos()
        elif(opcion=="3"):
            Vendedores()
            input("Presiona Enter para continuar...")
            os.system('cls')
            Personalizacion_Usuario()
            input("Presiona Enter para continuar...")
            os.system('cls') 
        elif (opcion=="4"):
            Impresion_Usuarios_Existentes()
        elif (opcion=="5"):
            Encuesta_Pila()
        elif (opcion=="6"):
            generarPDF()
            #generarQR()
        elif(opcion=="7"):
            print("llegale")
        else:
            print("Opcion no valida")

        input("Presiona Enter para continuar...")
        os.system('cls')       
#------------Menu
#------------Usuario nuevo
def pedirDatos():
    listaUsuarios.append(input("Ingresa el nombre del usuario:"))
    listaCorreos.append(input("Ingresa un correo electronico:"))
    listaSueldos.append(str(input("Ingresa tu sueldo mensual: ")))
    print("-----------Guardado-------")
#------------Tipo de garantia 
def Garantia():
    print("----Tipo de seguro que solicitara----")
    print("1.Por defecto")
    print("2.Premium")
    valor=input("Ingrese la opcion que desee: ")
    if valor=="1":
        print("Cada 15,000 km  o 1 año lo que suceda primero")
    elif valor=="2":
        print("2 años extendida sin limite de kilometraje")
    else:
        print("Opcion no valida")
#------------Pago
def Pago(marca):
    print(f"Auto elegido: {listarCarros[marca-1]} Precio: {lista_precios_carros[marca-1]}")
    print("1.Pago en efectivo")
    print("2.Pago con tarjeta")
    pago=input("¿Como pagaras? ")
    elemento=lista_precios_carros[marca-1]
    if pago=="1":
        PagoEfectivo=str(input("Ingrese la cantidad de efectivo: "))
        if PagoEfectivo>=elemento:
            print("Cobro exitososo disfrute su vehiculo")
        else:
            print("No le alcanza jefe")
    elif pago=="2":
        mensaje = "Procesando el pago con tarjeta.........."
        duracion = 5
        intervalo = 0.3
        parpadeo(mensaje, duracion, intervalo)
        print("Pago con tarjeta exitoso")
    else:
        print("Opcion no valida"),
#------------Lista de precio de carro
def Precios_Carros():
    for i in range(len(lista_precios_carros)):
        print(f"{lista_precios_carros[i]}")
#------------Lista de la marca de carro
def listarCarrosGenerales():
    print('{:<10} {:<25} {:<45}'.format("|No.|","|Modelo de Carros|","|Precios|"))
    for i in range(len(listarCarros)):
        print('{:<10} {:<25} {:<45}'.format(i+1,listarCarros[i],lista_precios_carros[i]))
#------------Lista colores exteriores
def listarColores():
    for i in range(len(Colores)):
        print(f"{i+1}.{Colores[i]}")
#------------Lista colores interiores
def listarColoresInteriores():
    for i in range(len(ColorInteriores)):
        print(f"{i+1}.{ColorInteriores[i]}")
#------------Lista transmicion
def tipoTransmicion():
    for i in range(len(Transmicion)):
        print(f"{i+1}.{Transmicion[i]}")
#------------Lista transmicion
def tiposRines():
    for i in range(len(Rines)):
        print(f"{i+1}.{Rines[i]}")
#------------Lista usuarios
def Usuarios():
    print('{:<10} {:<20} {:<25} {:>15}'.format("|No|","|Usuario|","|Correo|","|Sueldo Mensual|"))
    for i in range(len(listaUsuarios)):
        print('{:<10} {:<20} {:<25} {:<15}'.format(i+1,listaUsuarios[i],listaCorreos[i],  listaSueldos[i]))
    elegirusuario=int(input("Que usuario vas a escoger: "))
    print(f"Elegiste el usuario {listaUsuarios[elegirusuario-1]}")
#-------------Lista de impresion de datos de usuarios 
def Impresion_Usuarios_Existentes():
    print('{:<10} {:<20} {:<25} {:>15}'.format("|No|","|Usuario|","|Correo|","|Sueldo Mensual|"))
    for i in range(len(listaUsuarios)):
        print('{:<10} {:<20} {:<25} {:<15}'.format(i+1,listaUsuarios[i],listaCorreos[i],  listaSueldos[i]))
    print("----------Impresion de Datos Exitoso---------")
#-------------Lista de vendedores
def Vendedores():
    for i in range(len(listaVendedores)):
        print(f"{i+1}.{listaVendedores[i]}")
    elegirvendedor=int(input("Que vendedor vas a escoger: "))
    print(f"Tu vendedor personal sera: {listaVendedores[elegirvendedor-1]}")
#-------------Personalizacion del usuario
def Personalizacion_Usuario():
    listarCarrosGenerales() 
    marca=int(input("Ingresa la marca del carro: "))
    print(f"Elegiste {listarCarros[marca-1]}")
    input("Presiona Enter para continuar...")
    os.system('cls')

    tiposRines()
    Rines_Escogido=int(input("Ingresa el nombre del rin que desees: "))
    input("Presiona Enter para continuar...")
    os.system('cls')

    print("Colores disponibles")
    for i in range(len(Colores)):
        print(f"{i+1}.{Colores[i]}")

    color_elegido=int(input("Ingrese el numero del color exterior del vehiculo: "))
    color_exterior=Colores[color_elegido-1]
    color_elegido=int(input("Ingresa el numero del color interior del vehiculo: "))
    color_interior=Colores[color_elegido-1]
    input("Presiona Enter para continuar...")
    os.system('cls')

    tipoTransmicion()
    Transmicion_Elegido=int(input("Ingresa el tipo de transmicion que deseas: "))
    Personalizacion_Final=[listarCarros[marca-1],Rines[Rines_Escogido-1],color_exterior,color_interior,Transmicion[Transmicion_Elegido-1]]
    registro_carros.append(Personalizacion_Final)
    print("La impresion de datos de la personalizacion del carro es: ")
    print('{:<10} {:<20} {:<20} {:<15} {:>20}'.format("|Marca|","|Tipo de rin|","|Color ext|","|Color interior|","|Transmición|"))
    print('{:<10} {:<20} {:<20} {:<15} {:>20}'.format(registro_carros[i+11][0],registro_carros[i+11][1],registro_carros[i+11][2],registro_carros[i+11][3],registro_carros[i+11][4]))
    Garantia()
    input("Presiona Enter para continuar...")
    os.system('cls')
    Pago(marca)
#-----------Encuesta-------------------
def Encuesta_Pila():
    stack=Stack()
    seleccionar="1"
    while(seleccionar!="6"):
        print("¿Que marca de vehiculo te gustaria que obtuvieramos en un futuro:")
        print("1. Agregar marca del vehiculo")
        print("2. Eliminar marca del ultimo vehiculo agregado")
        print("3. Ver ultimo elemento agregado")
        print("4. Mostrar todas las marcas agregadas")
        print("5. Numero de elementos agregados")
        print("6. Salir")

        seleccionar=input("Que opcion desea?: ")
        if seleccionar=="1":
            agregar=input("Ingresa la marca del vehiculo: ")
            stack.push(agregar)
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif seleccionar=="2":
            if not stack.is_empty():
                eliminar_agregado=stack.pop()
                print(f"Marca eliminado: {eliminar_agregado}")
                input("Presiona Enter para continuar...")
                os.system('cls')
            else:
                print("No se ha ingresado ninguna marca")
                input("Presiona Enter para continuar...")
                os.system('cls')
        elif seleccionar=="3":
            if not stack.is_empty():
                tope_agregar=stack.peek()
                print(f"La ultima marca agregada fue:{tope_agregar}")
                input("Presiona Enter para continuar...")
                os.system('cls')
            else:
                print("No se ha agregado ninguna marca")
                input("Presiona Enter para continuar...")
                os.system('cls')
        elif seleccionar=="4":
            if not stack.is_empty():
                mostrar_agregados=stack.display()
                print(f"Marcas registradas: {mostrar_agregados}")
                input("Presiona Enter para continuar...")
                os.system('cls')
            else:
                print("No se agregado ninguna marca")
                input("Presiona Enter para continuar...")
                os.system('cls')
        elif seleccionar=="5":
            print(f"El total de marcas registrados es:{stack.size()}")
            input("Presiona Enter para continuar...")
            os.system('cls')
        elif seleccionar=="6":
            print("Regreso al menu")
            input("Presiona Enter para continuar...")
            os.system('cls')
        else:
            print("Opcion invalida.")

#---------Datos extras---------------------
def parpadeo(mensaje, duracion, intervalo):
    iteraciones = int(duracion / intervalo)
    for _ in range(iteraciones):
        sys.stdout.write("\r" + mensaje)
        sys.stdout.flush()
        time.sleep(intervalo)
        
        sys.stdout.write("\r" + " " * len(mensaje))
        sys.stdout.flush()
        time.sleep(intervalo)
    sys.stdout.write("\r" + mensaje + "\n")
    sys.stdout.flush()
                       
