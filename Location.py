class Location:
    def __init__(self, nombre):
        self.nombre = nombre
class Ruta(Location):
    def __init__(self, nombre, criatura):
        super().__init__(nombre)
        self.criatura = criatura
class Ciudad(Location):
    def __init__(self, nombre):
        super().__init__(nombre)
