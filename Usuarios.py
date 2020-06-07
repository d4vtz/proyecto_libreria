class Usuario:

    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return '-------------------------\n\
Nombre: {0}\nID: {1}\n-------------------------\
               '.format(self.nombre, self.identificacion)

    def dias_prestado(self):
        pass
