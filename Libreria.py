from Usuarios import Usuario
from Libros import Libro


class Libreria:

    def __init__(self):
        self.libros = []
        self.usuarios = []

    '''---------- Usuarios -----------'''

    def existe_usuario(self, identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return True
            else:
                return False

    def usuario(self, identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario

    def tiene_libro(self, identificacion):
        for libro in self.libros:
            if identificacion in libro.lista_de_prestamo:
                return True
            else:
                return False

    def alta_usuario(self, usuario):
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)

    def baja_usuario(self, identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                self.usuarios.remove(usuario)

    def lista_usuarios(self):
        lista = []
        for usuario in self.usuarios:
            lista.append(usuario)
        return lista

    '''------------ Libros ------------'''

    def libro(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro

    def existe_libro(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return True
            else:
                return False

    def existe_ejemplar(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                if libro.disponibles() != 0:
                    return True
                else:
                    return False

    def alta_libro(self, libro):
        if libro not in self.libros:
            self.libros.append(libro)

    def baja_libro(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                self.libros.remove(libro)

    def rentar_libro(self, codigo, identificacion):
        for libro in self.libros:
            if libro.codigo == codigo:
                libro.lista_de_prestamo.append(identificacion)

    def devolver_libro(self, codigo, identificacion):
        for libro in self.libros:
            if libro.codigo == codigo:
                libro.lista_de_prestamo.remove(identificacion)

    def tiene_ejemplar(self, codigo, identificacion):
        for libro in self.libros:
            if libro.codigo == codigo:
                if identificacion in libro.lista_de_prestamo:
                    return True
                else:
                    return False

    def lista_libros(self):
        lista = []
        for libro in self.libros:
            lista.append(libro)
        return lista
