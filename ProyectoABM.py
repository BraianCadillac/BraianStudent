'''Mediante la presente le envio las definiciones del software a implementar para mi negocio.
Le comento que el negocio es una pyme dedicada a la venta de productos alimenticios, 
productos de limpieza, productos de forrajeria (objetos y alimentos para animales) 
y utensilios domesticos.
Este software debe permitirme realizar el alta, baja, modificación y listado 
de productos por cada categoría, donde necesito cargar por cada producto su 
marca - modelo/producto - grupo/categoria - precio - peso/volumen (liquido) 
- cantidad a ingresar/stock - código de artículo 
(único por cada articulo que debe ser generado por el mismo software).
Requiero dar de alta -baja - modificación - listado de cajeros y cajas habilitadas.
Mi negocio posee solo 8 cajas para operar.
De los cajeros requiero ingresar los datos como nombre - apellido - fecha de nacimiento - dni - 
preferencia de puesto - caja asignada/caja que atiende.
Necesito un area de administración donde pueda obtener el balance total del dia, 
el balance total del mes, el balance total de cada cajero, el balance total por caja, 
cantidad de productos vendidos por categoria, cantidad de productos vendidos en total.
Tambien necesito un area de compra, donde pueda simular una compra real de los productos ingresados.
Esta área debe permitirme elegir los productos que existen en el negocio, 
la cantidad que quiero comprar y luego el cierre de la compra donde me dirá 
cuanto debo pagar y debe darme a elegir los metodos de pagos (tarjeta de credito - debito o efectivo)
Ante cualquier consulta, quedo a disposición.
Saludos!'''
from os import system
import time
class Productos():
    def __init__(self, prod, marca, cantidad, precio, codigo, peso):
        self.prod = prod
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
        self.codigo = codigo
        self.peso = peso
class ProductosDeLimpieza(Productos):
    def __init__(self, prod, marca, cantidad, precio, codigo, peso):
        super().__init__(prod, marca, cantidad, precio, codigo, peso)
productosdelimpieza = []
class ProductosDeForrajeria(Productos):
    def __init__(self, prod, marca, cantidad, precio, codigo, peso):
        super().__init__(prod, marca, cantidad, precio, codigo, peso)
productosdeforrajeria = []
class ProductosDeUtensiliosD():
    def __init__(self, prod, marca, cantidad, precio, codigo):
        self.prod = prod
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
        self.codigo = codigo
utensiliosdomesticos = []

while True:
    try:
        print ("1. Ingresar productos al stock")
        print ("2. Lista de productos del stock")
        print ("3. Modificar producto")
        op = int(input('Ingrese numero de opcion: '))
        system("cls")
        if op == 1:
            print("1. Ingresar productos de limpieza")
            print("2. Ingresar productos de Forrajeria")
            print("3. Ingresar productos de Utensilios Domesticos")
            op = int(input('Ingrese numero de opcion: '))
            system("cls")
            if op == 1:
                productoslimpieza = input('Ingresar producto: ')
                marcalimpieza = input('Ingresa la marca: ')
                cantidadlimpieza = int(input('¿Cuantos quieres ingresar?: '))
                preciol = int(input('Precio del producto unitario: $'))
                codigolimp = input('Codigo de producto: ')
                pesolimp = input('Ingresar peso del producto de limpieza: ')
                productolimp = ProductosDeLimpieza(productoslimpieza, marcalimpieza, cantidadlimpieza, preciol, codigolimp, pesolimp)
                productosdelimpieza.append(productolimp)
            elif op == 2:
                productosforrajeria = input('Ingresar producto: ')
                marcaforrajeria = input('Ingresa la marca: ')
                cantidadforrajeria = int(input('¿Cuantos quieres ingresar?: '))
                preciof = int(input('Precio del producto unitario: $'))
                codigoforr = input('Codigo de producto: ')
                pesoforr = input('Ingresar peso del producto de forrajeria: ')
                productoforr = ProductosDeForrajeria(productosforrajeria, marcaforrajeria, cantidadforrajeria, preciof, codigoforr, pesoforr)
                productosdeforrajeria.append(productoforr)
        elif op == 2:
            try:
                print("1. Lista de productos limpieza")
                print("2. Lista de productos de Forrajeria")
                print("3. Lista de productos de Utensilios domesticos")
                op = int(input('Ingrese numero de opcion: '))
                if op == 1:
                    if len(productosdelimpieza) == 0:
                        print ('AUN NO TIENES PRODUCTOS DE LIMPIEZA EN EL STOCK')
                        time.sleep(2)
                    else:    
                        for i in productosdelimpieza:
                            print("PRODUCTO:", i.prod,", MARCA:", i.marca,", PESO:", i.peso,", CANTIDAD: ", i.cantidad,", PRECIO:$",i.precio,", CODIGO DEL PRODUCTO: ",i.codigo)
                if op == 2:
                    if len(productosdeforrajeria) == 0:
                        print ('AUN NO TIENES PRODUCTOS DE FORRAJERIA EN EL STOCK')
                        time.sleep(2)
                    else:
                        for j in productosdeforrajeria:
                            print("PRODUCTO:", j.prod,", MARCA: ",j.marca, ", PESO:", j.peso,", CANTIDAD: ",j.cantidad,", PRECIO:$",j.precio,", CODIGO DEL PRODUCTO: ",j.codigo)
            except:
                print('¡HAS INGRESADO UNA OPCION INCORRECTA!')
                time.sleep(2)
                system("cls")
        elif op == 3:
            try:
                print ("1. Modificar productos de limpieza")
                print ("2. Modificar productos de Forrajeria")
                print ("3. Modificar productos de utensilio domesticos")
                op = int(input('Ingrese numero de opcion: '))
                system("cls")
                if op == 1:
                    for i in productosdelimpieza:
                        print("PRODUCTO:", i.prod,", MARCA:", i.marca,", PESO:", i.peso,", CANTIDAD: ", i.cantidad,", PRECIO:$",i.precio,", CODIGO DEL PRODUCTO: ",i.codigo)
                    productoslimpieza = input('¿Que producto quieres modificar: ')
                    marcalimpieza = input('Ingresa la marca del producto a modificar: ')
                    for i in productosdelimpieza:
                        if i.prod == productoslimpieza and i.marca == marcalimpieza:
                            cantidadlimpieza = int(input('¿Cuantos productos quieres eliminar/reponer del stock?: '))
                            if cantidadlimpieza > i.cantidad:
                                print ('Has ingresado un numero mayor al stock del que tienes')
                            else:
                                i.cantidad = i.cantidad - cantidadlimpieza
                                i.cantidad = i.cantidad
                        if i.cantidad == 0:
                            productosdelimpieza.remove(i)
                            print ('Ya no tienes mas stock de este producto')
                elif op == 2:
                    for j in productosdeforrajeria:
                        print("PRODUCTO:", j.prod,", MARCA: ",j.marca, ", PESO:", j.peso,", CANTIDAD: ",j.cantidad,", PRECIO:$",j.precio,", CODIGO DEL PRODUCTO: ",j.codigo)
                    productosforrajeria = input('¿Que producto quieres modificar: ')
                    marcaforrajeria = input('Ingresa la marca del producto a modificar: ')
                    for j in productosdeforrajeria:
                        if j.prod == productosforrajeria and j.marca == marcaforrajeria:
                            cantidadforrajeria = int(input('¿Cuantos productos quieres eliminar del stock?: '))
                            if cantidadforrajeria > j.cantidad:
                                print ('Has ingresado un numero mayor al stock del que tienes')
                            else:
                                j.cantidad = j.cantidad - cantidadforrajeria
                                j.cantidad = j.cantidad
                        if j.cantidad == 0:
                            productosdeforrajeria.remove(j)
                            print('Ya no tienes mas stock de este producto')

            except:
                print('HAS INGRESADO UNA OPCION INCORRECTA')
                time.sleep(2)
                system("cls")




    except:
        print('¡HAS INGRESADO UNA OPCION INCORRECTA!')
        time.sleep(2)
        system("cls")