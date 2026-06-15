import os
from functions import mostrar_libros_registrados, libros, agregar_libro, modificar_libro, buscar_titulo_numero, buscar_libro, prestar_libro, devolver_libro, eliminar_libro, mostrar_estadisticas
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
    print("8. Mostrar estadísticas")
    print("9. Salir")
    

    try:

        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            print("1. Agregar libro")
    
            while True:
                nombre_libro = input("Ingrese el título del libro:\n").title()
                if nombre_libro.strip() == "":
                    print("El título no puede estar vacío, intente nuevamente.")
                else:
                    break
            
            while True:
                autor = input("Ingrese el nombre completo del autor:\n").title()
                if autor.strip() == "":
                    print("El autor no puede estar vacío, intente nuevamente.")
                else:
                    break
            
            agregar_libro(nombre_libro, autor)
            input("\nPresione Enter para continuar...")


        elif opcion == 2:
            print("2. Mostrar libros")
            mostrar_libros_registrados(libros)
            input("\nPresione Enter para continuar...")


        elif opcion == 3:
            print("3. Buscar libro")
            busqueda_libro = input("Ingrese el nombre del libro que busca:\n")
            validador = buscar_libro(busqueda_libro)
            input("\nPresione Enter para continuar...")


        elif opcion == 4:
            print("4. Prestar libro")
            busqueda_libro = input("Ingrese el título del libro que busca:\n")
            validador = buscar_libro(busqueda_libro)
            id_libro = int(input("Ingrese el ID del libro a prestar: "))
            prestar_libro(id_libro)
            input("\nPresione Enter para continuar...")


        elif opcion == 5:
            print("5. Devolver libro")
            busqueda_libro = input("Ingrese el título del libro que desea devolver:\n")
            validador = buscar_libro(busqueda_libro)
            id_libro = int(input("Ingrese el ID del libro a devolver: "))
            devolver_libro(id_libro)
            input("\nPresione Enter para continuar...")


        elif opcion == 6:
            print("6. Eliminar libro")
            busqueda_libro = input("Ingrese el título del libro que desea eliminar:\n")
            validador = buscar_libro(busqueda_libro)
            id_libro = int(input("Ingrese el ID del libro a eliminar: "))
            eliminar_libro(id_libro)
            input("\nPresione Enter para continuar...")


        elif opcion == 7:
            print("7. Modificar libro")

            while True:
                libro_buscado = input("¿Cuál es el título del libro que desea modificar?\n").title()
                if libro_buscado.strip() == "":
                    print("El título no puede estar vacío, intente nuevamente.")
                else:
                    break

            validador = buscar_titulo_numero(libro_buscado)

            if validador == True:
                indice_libro = int(input("De los libros que están en la lista, indíque el número del título que desea modificar:\n"))

                while True:
                    nombre_libro = input("Modifique el titulo del libro:\n").capitalize()
                    if nombre_libro.strip() == "":
                        print("El título no puede estar vacío, intente nuevamente.")
                    else:
                        break

                while True:
                    autor = input("Modifique el nombre del autor:\n").capitalize()
                    if autor.strip() == "":
                        print("El autor no puede estar vacío, intente nuevamente.")
                    else:
                        break

                modificar_libro(indice_libro - 1, nombre_libro, autor)
                input("\nPresione Enter para continuar...")
            else:
                print("Vuelva a intentarlo con un título existente por favor.")
                input("\nPresione Enter para continuar...")


        elif opcion == 8:
            print("Mostrar estadísticas")
            print("\n--- Estadísticas ---")
            mostrar_estadisticas()
            input("\nPresione Enter para continuar...")


        elif opcion == 9:
            print("9. Salir: ¡Hasta luego!")
            break


        else:
            print("Opción no válida, intente nuevamente")


    except ValueError:
        print("Error, ingrese un número válido.")
    
    

