import Funciones as fun
from Libreria import Libreria


def main():
    libreria = Libreria()
    print('Bienvenido... Ingresa la fecha de hoy:')
    fecha = fun.ingresar_fecha()

    def info_usuario(identificacion):
        usuario = libreria.usuario(identificacion)
        print(usuario)

    def info_libro(codigo):
        libro = libreria.libro(codigo)
        print(libro)

    opcion = fun.menu()
    while opcion != 0:
        if opcion == 1:
            nuevo_usuario = fun.agregar_usuario()
            identificacion = nuevo_usuario.identificacion
            print('\nAgregando usuario...')
            libreria.alta_usuario(nuevo_usuario)
            info_usuario(identificacion)

        elif opcion == 2:
            identificacion = int(input('ID: '))
            hay_usuario = libreria.existe_usuario(identificacion)
            tiene_libro = libreria.tiene_libro(identificacion)
            if hay_usuario:
                if not tiene_libro:
                    print('\nBorrando usuario...')
                    info_usuario(identificacion)
                    libreria.baja_usuario(identificacion)
                else:
                    print('\nNo se puede dar de baja...')
            else:
                print('\nNo existe un usuario con ese ID')

        elif opcion == 3:
            nuevo_libro = fun.agregar_libro()
            codigo = nuevo_libro.codigo
            print('\nAgregando libro...')
            libreria.alta_libro(nuevo_libro)
            info_libro(codigo)

        elif opcion == 4:
            codigo = int(input('Codigo: '))
            hay_libro = libreria.existe_libro(codigo)
            hay_ejemplares = libreria.existe_ejemplar(codigo)
            if hay_libro:
                if hay_ejemplares:
                    print('\nBorrando libro...')
                    info_libro(codigo)
                    libreria.baja_libro(codigo)
                else:
                    print('\nNo hay ejemplares disponibles')
            else:
                print('\nNo existe un libro con ese codigo.')

        elif opcion == 5:
            print('\nDime que libro quieres rentar:')
            codigo = int(input('Codigo: '))
            identificacion = int(input('ID: '))

            hay_usuario = libreria.existe_usuario(identificacion)
            hay_libro = libreria.existe_libro(codigo)
            hay_ejemplares = libreria.existe_ejemplar(codigo)
            if hay_usuario:
                if hay_libro:
                    if hay_ejemplares:
                        print('\nRentando libro...')
                        libreria.rentar_libro(codigo, identificacion)
                        info_libro(codigo)
                    else:
                        print('\nNo hay ejemplares disponibles')
                else:
                    print('\nNo existe libro con ese codigo')
            else:
                print('\nNo existe usuario con ese ID')

        elif opcion == 6:
            print('\nDime que libro quieres devolver:')
            codigo = int(input('Codigo: '))
            print('\nDime tu identificacion')
            identificacion = int(input('ID: '))

            hay_usuario = libreria.existe_usuario(identificacion)
            hay_libro = libreria.existe_libro(codigo)
            tiene_libro = libreria.tiene_ejemplar(codigo, identificacion)
            if hay_usuario:
                if hay_libro:
                    if tiene_libro:
                        print('\nDevolviendo libro...')
                        libreria.devolver_libro(codigo, identificacion)
                        info_libro(codigo)
                    else:
                        print('\nNo tiene un libro prestado')
                else:
                    print('\nNo existe libro con ese codigo')
            else:
                print('\nNo existe usuario con ese ID')

        elif opcion == 7:
            usuarios = libreria.lista_usuarios()
            for usuario in usuarios:
                print(usuario)

        elif opcion == 8:
            libros = libreria.lista_libros()
            for libro in libros:
                print(libro)

        opcion = fun.menu()


main()
