#Datosestaticos
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

def listarCarrosGenerales():
    for i in range(len(listarCarros)):
        print(f"{i+1}. {listarCarros[i]}")
    """elegido=int(input("Que marca de vehiculo vas a escojer: "))
    print(f"Elegiste la marca: {listarCarros[elegido-1]}")
    print("Buena opcion")"""

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
    elegirColor=int(input("Que Color vas a querer para exteriores: "))
    print(f"Tu color exterior sera: {Colores[elegirColor-1]}")
    print("----Datos guardados----")

ColorInteriores=[
    "Azul",
    "Rojo",
    "Negro",
    "Blanco",]

def listarColoresInteriores():
    for i in range(len(ColorInteriores)):
        print(f"{i+1}.{ColorInteriores[i]}")
    elegirColorInt=int(input("Que Color vas a querer para interiores: "))
    print(f"Tu color interior sera :{ColorInteriores[elegirColorInt-1]}")
    print("----Datos guardados----")
Transmicion=[
    "Manual",
    "Automatico",
    ]
def tipoTransmicion():
    for i in range(len(Transmicion)):
        print(f"{i+1}.{Transmicion[i]}")
    elegirtransmicion=int(input("Tipo de transmicion que desea? "))
    print(f"Tu transmicion es:{Transmicion[elegirtransmicion-1]}")
    print("--Datos Guardados--")

Rines=[
"Acero",
"Magnesio",
"Aleacion",]

def tiposRines():
    for i in range(len(Rines)):
        print(f"{i+1}.{Rines[i]}")
    elegirRines=int(input("Tipos de rines que deseas? "))
    print(f"Tu rin sera:{Rines[elegirRines-1]}")
    print("--Datos Guardados--")

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
    
listaPrecios=["100,000",
    "90,000",
    "250,000",
    "300,000",
    "70,000",
    "150,000",
    "260,000",
    "800,000",
    "420,000",
    "950,000",
    "95,000",
    "450,000",
    "870,000",
    "600,000",
    "990,000",
    "840,000",
    "780,000",
    "650,000",
    "320,000",
    "60,000",
    "900,000",
    "1,000,000",
    "5,000,000",
    "150,000",
    "750,000",
    "390,000",
    "845,000",
    "900,000",
    "560,000",
    "410,000",
    "604,000",
    "910,000",
    "5,000,000",
    "100,000,000",
    "162,000",
    "951,000",
    "450,000",
    "741,000",
    "621,000",
    "145,000",
    "50,000",
    "60,000",
    "122,000",
    "850,000",
    "740,000",
    "360,000",
    "520,000",
    "450,000",
    "960,000",
    "520,000",
    "960,000",
    "710,000",
    "120,000",
    "250,000",
    "205,000",
    "958,000",
    "310,000,000",
    "630,000",
    "850,000",
    "710,000",
    "450,000",
    "900,200",
    "651,000",
    "750,000",
    "860,000",
    "450,000",
    "120,000",
    "450,000",
    "200,000",
    "980,000",
]

def Usuarios():
    print('{:<10} {:<20} {:<25} {:>15}'.format("|No|","|Usuario|","|Correo|","|Sueldo Mensual|"))
    for i in range(len(listaUsuarios)):
        print('{:<10} {:<20} {:<25} {:<15}'.format(i+1,listaUsuarios[i],listaCorreos[i],  listaPrecios[i]))
    elegirusuario=int(input("Que usuario vas a escoger: "))
    print(f"Elegiste el usuario {listaUsuarios[elegirusuario-1]}")

def Impresion_Usuarios_Existentes():
    print('{:<10} {:<20} {:<25} {:>15}'.format("|No|","|Usuario|","|Correo|","|Sueldo Mensual|"))
    for i in range(len(listaUsuarios)):
        print('{:<10} {:<20} {:<25} {:<15}'.format(i+1,listaUsuarios[i],listaCorreos[i],  listaPrecios[i]))
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

def Personalizacion_Usuario(): 
    listarCarrosGenerales()
    marca=input("Ingrese la marca del carro: ")
 

