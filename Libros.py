class Libro:

    def __init__(self, titulo, autor, codigo, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.ejemplares = ejemplares
        self.lista_de_prestamo = []

    def __str__(self):
        return '-------------------------\nTitulo: {0}\nCodigo: {1}\n\
Ejemplares disponibles: {2}\n-------------------------\
               '.format(self.titulo, self.codigo, self.disponibles())

    def ejemplares_prestados(self):
        return len(self.lista_de_prestamo)

    def disponibles(self):
        return self.ejemplares-self.ejemplares_prestados()
