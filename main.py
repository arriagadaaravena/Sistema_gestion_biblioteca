import os
from functions import mostrar_libros_registrados, libros, agregar_libro, modificar_libro, buscar_titulo_numero
os.system("clear")


menu = True

while menu:
    os.system("clear")
    print("====BIBLIOTECA====")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Eliminar libro")
    print("7. Modificar libro")
    print("8. Mostrar libro")
    print("9. Salir")
    

    try:

        opcion = int(input("Elija una opción:\n"))

        if opcion == 1:
            print("1. Agregar libro")
            nombre_libro = input("Ingrese el título del libro:\n").title()
            autor = input("Ingrese el nombre completo del autor:\n").title()
            agregar_libro(nombre_libro, autor)


        elif opcion == 2:
            print("2. Mostrar libros")
            mostrar_libros_registrados(libros)
            
        elif opcion == 3:
            print("3. Buscar libro")

        elif opcion == 4:
            print("4. Prestar libro")

        elif opcion == 5:
            print("5. Devolver libro")

        elif opcion == 6:
            print("6. Eliminar libro")

        elif opcion == 7:
            print("7. Modificar libro")
            libro_buscado = input("¿Cuál es el título del libro que desea modificar?\n").title()
            validador = buscar_titulo_numero(libro_buscado)

            if validador == True:

                indice_libro = int(input("De los libros que están en la lista, indíque el número del título que desea modificar:\n"))
                nombre_libro = input("Modifique el titulo del libro:\n").capitalize()
                autor = input("Modifique el nombre del autor:\n").capitalize()
                modificar_libro(indice_libro-1, nombre_libro, autor)
            else:
                print("Vuelva a intentarlo con un título existente por favor.")
        elif opcion == 8:
            print("Mostrar libro")

        elif opcion == 9:
            print("9. Salir")
            break
        else:
            print("Opción no válida")


    except Exception as e:
        print(f"Error real: {e}")
    
    

