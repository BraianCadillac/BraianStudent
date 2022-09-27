import time
from os import system
class Productos():
    def __init__(self, contador, prod, marca, cantidad, precio, codigo, peso):
        self.contador = contador
        self.prod = prod
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
        self.codigo = codigo
        self.peso = peso
    def Lista(self, lista):
        print('------------------------------------------------------------------------------------------------------------------------------')
        for i in lista:
            print(i.contador,":  PRODUCTO:", i.prod,", MARCA: ", i.marca, ", PESO:", i.peso,", CANTIDAD: ", i.cantidad,", PRECIO:$",i.precio,", CODIGO DEL PRODUCTO: ", i.codigo)
        print('------------------------------------------------------------------------------------------------------------------------------')
    def ModificacionDeProducto(self, lista, opcion):
        for i in lista:
            if opcion == i.contador:
                print('-------------\n0. Volver\n-------------')
                time.sleep(2)
                cantidad = int(input('Ingresa la cantidad a ELIMINAR del stock: '))
                if cantidad == 0:
                    system("cls")
                    print('CARGANDO...')
                    time.sleep(1)
                    system("cls")
                    break
                elif cantidad > i.cantidad:
                    system("cls")
                    print ('HAS INGRESADO UNA CANTIDAD MAYOR A LA DEL STOCK')
                    time.sleep(2)
                    system("cls")
                else:
                    if cantidad < i.cantidad:
                        i.cantidad = i.cantidad - cantidad
                        i.cantidad = i.cantidad
                        system("cls")
                        print ('¡ELIMINACION EXITOSA!')
                        time.sleep(2)
                        system("cls")
                    else:
                        lista.remove(i)
                        system("cls")
                        print ('¡YA NO TIENES MAS STOCK DE ESTE PRODUCTO!')
                        time.sleep(3)
                        system("cls")