from Productos import *
class ProductosDeForrajeria(Productos):
    def __init__(self, prod, marca, cantidad, precio, codigo, peso):
        super().__init__(prod, marca, cantidad, precio, codigo, peso)