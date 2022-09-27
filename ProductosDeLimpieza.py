from Productos import *
class ProductosDeLimpieza(Productos):
    def __init__(self, contador, prod, marca, cantidad, precio, codigo, peso):
        super().__init__(contador, prod, marca, cantidad, precio, codigo, peso)