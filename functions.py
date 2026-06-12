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