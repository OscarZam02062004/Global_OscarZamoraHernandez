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

Colores=[
    "Azul",
    "Verde",
    "Rojo",
    "Morado",
    "Amarillo",
    "Dorado",
    "Plateado",
    "Rosa",
    "Tornasol",
    "Negro",]

ColorInteriores=[
    "Azul",
    "Rojo",
    "Negro",
    "Blanco",]

Transmicion=[
    "Manual",
    "Automatico",
    ]

Rines=[
"Acero",
"Magnesio",
"Aleacion"]

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

registro_carros=[
    ["BMW","Acero","Rojo","Negro","Manual"],
    ["General Motors","Magnesio","Verde","Azul","Automatico"],
    ["Honda","Aleacion","Morado","Amarillo","Manual"],
    ["Hyundai Motor Company","Acero","Dorado","Plateado","Manual"],
    ["Mazda","Magnesio","Rosa","Tornasol","Manual"],
    ["Nissan","Aleacion","Negro","Blanco","Manual"],
    ["Pagani","Acero","Azul","Rojo","Manual"],
    ["Ferrari","Magnesio","Negro","Blanco","Manual"],
    ["Lamborgini","Aleacion","Morado","Amarillo","Manual"],
    ["Audi","Acero","Dorado","Plateado","Manual"],
    ["Infiniti","Magnesio","Rosa","Tornasol","Manual"],
    ["Renault","Aleacion","Azul","Rojo","Manual"],
    ["Alfa Romeo","Acero","Dorado","Plateado","Manual"],
    ["Acura","Magnesio","Negro","Blanco","Manual"],
    ["Aston Martin","Aleacion","Morado","Amarillo","Manual"],
    ["Bentley","Acero","Verde","Azul","Manual"],
    ["Cadillac","Magnesio","Rojo","Negro","Manual"],
    ["Chevrolet","Aleacion","Verde","Azul","Manual"],
    ["Toyota","Acero","Morado","Amarillo","Manual"],
    ["Jeep","Magnesio","Dorado","Plateado","Manual"],
]
#------------Estructura de la pila
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
