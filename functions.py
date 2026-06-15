libros = [
    {"autor": "Gabriel García Márquez", "titulo": "Cien años de soledad", "disponibilidad": True},
    {"autor": "Isabel Allende", "titulo": "La casa de los espíritus", "disponibilidad": True},
    {"autor": "Jorge Luis Borges", "titulo": "Ficciones", "disponibilidad": True},
    {"autor": "Mario Vargas Llosa", "titulo": "La ciudad y los perros", "disponibilidad": True},
    {"autor": "Julio Cortázar", "titulo": "Rayuela", "disponibilidad": True},
    {"autor": "Freida McFadden", "titulo": "La asistenta", "disponibilidad": True},
    {"autor": "María Ignacia Urzúa", "titulo": "Una promesa de cien años", "disponibilidad": True},
    {"autor": "Francisca Solar", "titulo": "El buzón de las impuras", "disponibilidad": True},
    {"autor": "T.J Klune", "titulo": "La casa en el mar más azul", "disponibilidad": True},
    {"autor": "Alice Kellen", "titulo": "El mapa de los anhelos", "disponibilidad": True},
    {"autor": "Edgar Allan Poe ", "titulo": "Narraciones extraordinarias", "disponibilidad": True}
    
]

def agregar_libro(nombre_libro, autor):
    libro_nuevo = {"autor": autor, "titulo": nombre_libro, "disponibilidad": True}
    libros.append(libro_nuevo)


def mostrar_libros_registrados(libros):
    contador = 0
    for libro in libros:
        contador = contador + 1
        if libro["disponibilidad"] == True:
            estado = "Disponible"
        else:
            estado = "Prestado"

        print(f"{contador} - {libro['titulo']} - {libro['autor']} | {estado}")

def buscar_libro(nombre):
    contador = 0
    encontrado = False
    for libro in libros:
        contador += 1
        if nombre.lower() in libro["titulo"].lower():
            disponibilidad = "Disponible" if libro["disponibilidad"] else "Prestado"
            print(f"{contador} - {libro['titulo']} - {libro['autor']} - {disponibilidad}")
            encontrado = True
    
    if encontrado == False:
        print("No se encontró ningún libro con ese título")

    return encontrado


def prestar_libro(indice):
    libro = libros[indice - 1]
    
    if libro["disponibilidad"] == False:
        print("Este libro ya está prestado, intente con otro título disponible.")
    else:
        libro["disponibilidad"] = False
        print(f"El libro '{libro['titulo']}' ha sido prestado exitosamente.")


def devolver_libro(indice):
    libro = libros[indice - 1]
    
    if libro["disponibilidad"] == True:
        print("Este libro ya está prestado, intente con otro título disponible.")
    else:
        libro["disponibilidad"] = True
        print(f"El libro '{libro['titulo']}' ha sido devuelto con éxito.")


def eliminar_libro(indice):
    libro = libros[indice -1]
    libros.pop(indice-1)
    print(f"El libro '{libro['titulo']}' ha sido eliminado exitosamente.")


def modificar_libro(indice, nuevo_titulo, nuevo_autor):
    libros[indice]["titulo"] = nuevo_titulo
    libros[indice]["autor"] = nuevo_autor

def buscar_titulo_numero(nombre):
    contador = 0
    encontrado = False
    for libro in libros:
        contador += 1
        if nombre.lower() in libro["titulo"].lower():
            print(f"{contador} - {libro['titulo']} - {libro['autor']}")
            encontrado = True
    
    if encontrado == False:
        print("No se encontró ningún libro con ese título")

    return encontrado

def mostrar_estadisticas():
    total = len(libros)
    disponibles = 0
    prestados = 0
    for libro in libros:
        if libro["disponibilidad"] == True:
            disponibles +=1
        else:
            prestados +=1

    print(f"Total de libros: {total}")
    print(f"Libros disponibles: {disponibles}")
    print(f"Libros prestados: {prestados}")