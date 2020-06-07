from Usuarios import Usuario
from Libros import Libro
from Fecha import *


def menu():
    print('\n0) Salir')
    print('1) Agregar usuario')
    print('2) Baja usuario')
    print('3) Alta libro')
    print('4) Baja libro')
    print('5) Rentar un libro')
    print('6) Devolver un libro')
    print('7) Lista de usuarios')
    print('8) Lista de libros\n')
    respuesta = int(input('Dime tu eleccion: '))
    if 0 <= respuesta <= 8:
        return respuesta
    else:
        while respuesta > 8 or respuesta < 0:
            print('Eleccion incorrecta')
            respuesta = int(input('Dime tu eleccion: '))


def agregar_usuario():
    nombre = str(input('Nombre: '))
    identificacion = int(input('ID: '))
    return Usuario(nombre, identificacion)


def agregar_libro():
    titulo = str(input('Titulo: '))
    autor = str(input('Autor: '))
    codigo = int(input('Codigo: '))
    ejemplares = int(input('Ejemplos: '))
    return Libro(titulo, autor, codigo, ejemplares)


def ingresar_fecha():
    dia = int(input('Dia: '))
    mes = int(input('Mes: '))
    ano = int(input('Año: '))

    while not fecha_valida(dia, mes, ano):
        print('Fecha invalida, teclea otra...')
        dia = int(input('Dia: '))
        mes = int(input('Mes: '))
        ano = int(input('Año: '))
    return Fecha(dia, mes, ano)
