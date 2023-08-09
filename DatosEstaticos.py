#Datosestaticos
import os
listarCarros=["BMW Group",
    "General Motors",
    "Honda",
    "Hyundai Motor Company",
    "Mazda",
    "Nissan",
    "Pagani",
    "Ferrari",
    "Lamborgini",
    "Audi",
    "Infiniti",
    "Renault",
    "Alfa Romeo",
    "Acura",
    "Aston Martin",
    "Bentley",
    "Cadillac",
    "Chevrolet",
    "Toyota",
    "Jeep",]
lista_precios_carros=[
    "450,500",
    "350,700",
    "78,450",
    "68,782",
    "70,485",
    "60,780",
    "3,500,100",
    "5,874,150",
    "8,000,000",
    "350,520",
    "120,000",
    "90,874",
    "110,541",
    "130,458",
    "850,450",
    "450,150",
    "235,145",
    "90,450",
    "87,154",
    "78,152"
]

def listarCarrosGenerales():
    print('{:<10} {:<25} {:<45}'.format("|No.|","|Modelo de Carros|","|Precios|"))
    for i in range(len(listarCarros)):
        print('{:<10} {:<25} {:<45}'.format(i+1,listarCarros[i],lista_precios_carros[i]))

Colores=[
    "Azul",
    "Verde",
    "Rojo",
    "Morado",
    "Amarillo",
    "Dorado",
    "Platado",
    "Rosa",
    "Tornasol",
    "Negro",]

def listarColores():
    for i in range(len(Colores)):
        print(f"{i+1}.{Colores[i]}")
    """elegirColor=int(input("Que Color vas a querer para exteriores: "))
    print(f"Tu color exterior sera: {Colores[elegirColor-1]}")"""


ColorInteriores=[
    "Azul",
    "Rojo",
    "Negro",
    "Blanco",]

def listarColoresInteriores():
    for i in range(len(ColorInteriores)):
        print(f"{i+1}.{ColorInteriores[i]}")
    """elegirColorInt=int(input("Que Color vas a querer para interiores: "))
    print(f"Tu color interior sera :{ColorInteriores[elegirColorInt-1]}")"""

Transmicion=[
    "Manual",
    "Automatico",
    ]
def tipoTransmicion():
    for i in range(len(Transmicion)):
        print(f"{i+1}.{Transmicion[i]}")
    """elegirtransmicion=int(input("Tipo de transmicion que desea? "))
    print(f"Tu transmicion es:{Transmicion[elegirtransmicion-1]}")"""


Rines=[
"Acero",
"Magnesio",
"Aleacion",]

def tiposRines():
    for i in range(len(Rines)):
        print(f"{i+1}.{Rines[i]}")
    """elegirRines=int(input("Tipos de rines que deseas? "))
    print(f"Tu rin sera:{Rines[elegirRines-1]}")"""


listaUsuarios=["Alicia",
    "Pedro",
    "Pablo",
    "Karla", 
    "Alfonso",
    "Axel",
    "Galicia",
    "Monserrat",
    "Armenta",
    "Oscar",
    "Omar",
    "Juan",
    "Ruben",
    "Sayde",
    "Leticia",
    "Tavo",
    "Danae",
    "Danna",
    "Coreya",
    "Rosita",
    "Panchito",
    "Margarita",
    "Maggy",
    "Aimee",
    "Anahi",
    "Edward",
    "Josue",
    "Erick",
    "Lemus",
    "Ivan",
    "Mauricio",
    "Neydy",
    "Alexandra",
    "Aleydy",
    "Berenice",
    "Joel",
    "Karime",
    "Rodolfo",
    "Hugo",
    "Anaid",
    "Rogelio",
    "Ariel",
    "Paty",
    "Selena",
    "Valentin",
    "Noe",
    "Paula",
    "Uriel",
    "Ismael",
    "Mundo",
    "Anita",
    "Julian",
    "Citlali",
    "Edgar",
    "Kain",
    "Sofia",
    "Joana",
    "Jazmin",
    "Yarazet",
    "Belen",
    "Julio",
    "Gaspar",
    "Maria",
    "Camila",
    "Brayan",
    "Cristian",
    "Alonso",
    "Alejandra",
    "Beyda",
    "Alejandro",
]

listaCorreos=["Alicia@gmailcom",
    "Pedro@gmailcom",
    "Pablo@gmailcom",
    "Karla@gmailcom", 
    "Alfonso@gmailcom",
    "Axel@gmailcom",
    "Galicia@gmailcom",
    "Monserrat@gmailcom",
    "Armenta@gmailcom",
    "Oscar@gmailcom",
    "Omar@gmailcom",
    "Juan@gmailcom",
    "Ruben@gmailcom",
    "Sayde@gmailcom",
    "Leticia@gmailcom",
    "Tavo@gmailcom",
    "Danae@gmailcom",
    "Danna@gmailcom",
    "Coreya@gmailcom",
    "Rosita@gmailcom",
    "Panchito@gmailcom",
    "Margarita@gmailcom",
    "Maggy@gmailcom",
    "Aimee@gmailcom",
    "Anahi@gmailcom",
    "Edward@gmailcom",
    "Josue@gmailcom",
    "Erick@gmailcom",
    "Lemus@gmailcom",
    "Ivan@gmailcom",
    "Mauricio@gmailcom",
    "Neydy@gmailcom",
    "Alexandra@gmailcom",
    "Aleydy@gmailcom",
    "Berenice@gmailcom",
    "Joel@gmailcom",
    "Karime@gmailcom",
    "Rodolfo@gmailcom",
    "Hugo@gmailcom",
    "Anaid@gmailcom",
    "Rogelio@gmailcom",
    "Ariel@gmailcom",
    "Paty@gmailcom",
    "Selena@gmailcom",
    "Valentin@gmailcom",
    "Noe@gmailcom",
    "Paula@gmailcom",
    "Uriel@gmailcom",
    "Ismael@gmailcom",
    "Mundo@gmailcom",
    "Anita@gmailcom",
    "Julian@gmailcom",
    "Citlali@gmailcom",
    "Edgar@gmailcom",
    "Kain@gmailcom",
    "Sofia@gmailcom",
    "Joana@gmailcom",
    "Jazmin@gmailcom",
    "Yarazet@gmailcom",
    "Belen@gmailcom",
    "Julio@gmailcom",
    "Gaspar@gmailcom",
    "Maria@gmailcom",
    "Camila@gmailcom",
    "Brayan@gmailcom",
    "Cristian@gmailcom",
    "Alonso@gmailcom",
    "Alejandra@gmailcom",
    "Beyda@gmailcom",
    "Alejandro@gmailcom",
]
    
listaSueldos=["5,000",
    "15,000",
    "25,000",
    "3,000",
    "7,500",
    "13,000",
    "26,000",
    "81,000",
    "42,000",
    "70,000",
    "15,000",
    "45,000",
    "87,000",
    "60,000",
    "65,000",
    "84,000",
    "78,000",
    "65,000",
    "32,000",
    "60,000",
    "90,000",
    "1,500",
    "5,500",
    "15,000",
    "75,000",
    "39,000",
    "84,000",
    "90,000",
    "56,000",
    "41,000",
    "60,000",
    "91,000",
    "5,000",
    "1,000",
    "16,000",
    "95,000",
    "45,000",
    "74,000",
    "62,000",
    "14,000",
    "50,000",
    "60,000",
    "12,000",
    "85,000",
    "74,000",
    "36,000",
    "52,000",
    "45,000",
    "96,000",
    "52,000",
    "96,000",
    "71,000",
    "12,000",
    "20,000",
    "25,000",
    "58,000",
    "31,000",
    "63,000",
    "85,000",
    "71,000",
    "45,000",
    "9,200",
    "61,000",
    "50,000",
    "60,000",
    "40,000",
    "20,000",
    "50,000",
    "00,000",
    "80,000",
]

def Usuarios():
    print('{:<10} {:<20} {:<25} {:>15}'.format("|No|","|Usuario|","|Correo|","|Sueldo Mensual|"))
    for i in range(len(listaUsuarios)):
        print('{:<10} {:<20} {:<25} {:<15}'.format(i+1,listaUsuarios[i],listaCorreos[i],  listaSueldos[i]))
    elegirusuario=int(input("Que usuario vas a escoger: "))
    print(f"Elegiste el usuario {listaUsuarios[elegirusuario-1]}")

def Impresion_Usuarios_Existentes():
    print('{:<10} {:<20} {:<25} {:>15}'.format("|No|","|Usuario|","|Correo|","|Sueldo Mensual|"))
    for i in range(len(listaUsuarios)):
        print('{:<10} {:<20} {:<25} {:<15}'.format(i+1,listaUsuarios[i],listaCorreos[i],  listaSueldos[i]))
    print("----------Impresion de Datos Exitoso---------")
listaVendedores=["Ximena",
    "Adriana",
    "Alfredo",
    "Choco",
    "Carlos",
    "Javier",
    "Yeiden",
    "Axel",
    "Yoshi",
    "Kevin",]

def Vendedores():
    for i in range(len(listaVendedores)):
        print(f"{i+1}.{listaVendedores[i]}")
    elegirvendedor=int(input("Que vendedor vas a escoger: "))
    print(f"Tu vendedor personal sera: {listaVendedores[elegirvendedor-1]}")

registro_carros=[
    ["BMW","Acero","Rojo","Negro","Manual"],
    "General Motors",
    "Honda",
    "Hyundai Motor Company",
    "Mazda",
    "Nissan",
    "Pagani",
    "Ferrari",
    "Lamborgini",
    "Audi",
    "Infiniti",
    "Renault",
    "Alfa Romeo",
    "Acura",
    "Aston Martin",
    "Bentley",
    "Cadillac",
    "Chevrolet",
    "Toyota",
    "Jeep",
    "Azul",
    "Verde",
    "Rojo",
    "Morado",
    "Amarillo",
    "Dorado",
    "Platado",
    "Rosa",
    "Tornasol",
    "Negro",
    "Manual",
    "Automatico",
    "Acero",
    "Magnesio",
    "Aleacion",
]
def Personalizacion_Usuario(): 
    listarCarrosGenerales()
    marca=int(input("Ingrese la marca del carro: "))
    input("Presiona Enter para continuar...")
    os.system('cls')

    tiposRines()
    Rines=input("Ingresa el tipo de rin que desees: ")
    input("Presiona Enter para continuar...")
    os.system('cls')

    print("Colores disponibles")
    for i in range(len(Colores)):
        print(f"{i+1}.{Colores[i]}")

    color_elegido=int(input("Ingrese el numero del color exterior del vehiculo: "))
    color_exterior=Colores[color_elegido-1]
    #input("Presiona Enter para continuar...")
    #os.system('cls')


    color_elegido=int(input("Ingresa el numero del color interior del vehiculo: "))
    color_interior=Colores[color_elegido-1]
    input("Presiona Enter para continuar...")
    os.system('cls')

    tipoTransmicion()
    Transmicion=input("Ingresa el tipo de transmicion que deseas: ")
  

    Personalizacion_Final=[listarCarros[marca-1],Rines,color_exterior,color_interior,Transmicion]

    registro_carros.append(Personalizacion_Final)
    print("La impresion de datos de la personalizacion del carro es: ")
    print("|Marca|     |Rin|   |Color exterior|   |Color interior|    |Transmicion|")
    for i in range(len(registro_carros)):
        print(f"Todo: {registro_carros}")
        print(f"Solo i {registro_carros[i]}")
       # print(f"{registro_carros[i][0]}--{registro_carros[i][1]}--{registro_carros[i][2]}--{registro_carros[i][3]}--{registro_carros[i][4]}--{registro_carros[i][5]}")




 

