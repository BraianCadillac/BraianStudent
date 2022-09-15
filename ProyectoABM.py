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
class ProductosDeUtensiliosD(Productos):
    def __init__(self, prod, marca, cantidad, precio, codigo, peso):
        super().__init__(prod, marca, cantidad, precio, codigo, peso)
utensiliosdomesticos = []

while True:
        print ("1. Ingresar productos al stock")
        print ("2. Lista de productos del stock")
        print ("3. Modificar producto")
        try:
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
                    system("cls")
                    print('PRODUCTO INGRESADO CON EXITO')
                    time.sleep(3)
                    system("cls")
                elif op == 2:
                    productosforrajeria = input('Ingresar producto: ')
                    marcaforrajeria = input('Ingresa la marca: ')
                    cantidadforrajeria = int(input('¿Cuantos quieres ingresar?: '))
                    preciof = int(input('Precio del producto unitario: $'))
                    codigoforr = input('Codigo de producto: ')
                    pesoforr = input('Ingresar peso del producto de forrajeria: ')
                    productoforr = ProductosDeForrajeria(productosforrajeria, marcaforrajeria, cantidadforrajeria, preciof, codigoforr, pesoforr)
                    productosdeforrajeria.append(productoforr)
                    system("cls")
                    print('PRODUCTO INGRESADO CON EXITO')
                    time.sleep(3)
                    system("cls")
                elif op == 3:
                    productosudomesticos = input('Ingresar producto: ')
                    marcaud = input('Ingresa la marca: ')
                    cantidadud = int(input('¿Cuantos quieres ingresar?: '))
                    precioud = int(input('Precio del producto: $'))
                    codigoud = input('Codigo de producto: ')
                    productoud = ProductosDeUtensiliosD(productosudomesticos, marcaud, cantidadud, precioud, codigoud, None)
                    utensiliosdomesticos.append(productoud)
                    system("cls")
                    print('PRODUCTO INGRESADO CON EXITO')
                    time.sleep(3)
                    system("cls")
                else:
                    print('¡HAS INGRESADO UNA OPCION INCORRECTA!')
                    time.sleep(3)
                    system("cls")
            elif op == 2:
                print("1. Lista de productos limpieza")
                print("2. Lista de productos de Forrajeria")
                print("3. Lista de productos de Utensilios domesticos")
                op = int(input('Ingrese numero de opcion: '))
                system("cls")
                if op == 1:
                    if len(productosdelimpieza) == 0:
                        print ('AUN NO TIENES PRODUCTOS DE LIMPIEZA EN EL STOCK')
                        time.sleep(3)
                        system("cls")
                    else:    
                        for i in productosdelimpieza:
                            print("PRODUCTO:", i.prod,", MARCA:", i.marca,", PESO:", i.peso,", CANTIDAD: ", i.cantidad,", PRECIO:$",i.precio,", CODIGO DEL PRODUCTO: ", i.codigo)
                elif op == 2:
                    if len(productosdeforrajeria) == 0:
                        print ('AUN NO TIENES PRODUCTOS DE FORRAJERIA EN EL STOCK')
                        time.sleep(3)
                        system("cls")
                    else:
                        for j in productosdeforrajeria:
                            print("PRODUCTO:", j.prod,", MARCA: ", j.marca, ", PESO:", j.peso,", CANTIDAD: ", j.cantidad,", PRECIO:$",j.precio,", CODIGO DEL PRODUCTO: ", j.codigo)
                elif op == 3:
                    if len(utensiliosdomesticos) == 0:
                        print ('AUN NO TIENES PRODUCTOS DE UTENSILIOS DOMESTICOS')
                        time.sleep(3)
                        system("cls")
                    else:
                        for k in utensiliosdomesticos:
                            print("PRODUCTO:", k.prod,", MARCA: ", k.marca, ", PESO:", k.peso,", CANTIDAD: ", k.cantidad,", PRECIO:$",k.precio,", CODIGO DEL PRODUCTO: ", k.codigo)
                else:
                    print('¡HAS INGRESADO UNA OPCION INCORRECTA!')
            elif op == 3:
                print ("1. Modificar productos de limpieza")
                print ("2. Modificar productos de Forrajeria")
                print ("3. Modificar productos de utensilio domesticos")
                op = int(input('Ingrese numero de opcion: '))
                system("cls")
                if op == 1:
                    for i in productosdelimpieza:
                        print("PRODUCTO:", i.prod,", MARCA:", i.marca,", PESO:", i.peso,", CANTIDAD: ", i.cantidad,", PRECIO:$",i.precio,", CODIGO DEL PRODUCTO: ", i.codigo)
                        productoslimpieza = input('¿Que producto quieres modificar: ')
                        if productoslimpieza != i.prod:
                            print('PRODUCTO INGRESADO INEXISTENTE EN EL STOCK')
                            time.sleep(3)
                            system("cls")
                        elif productoslimpieza == i.prod:
                            marcalimpieza = input('Ingresa la marca del producto a modificar: ')
                            if marcalimpieza != i.marca:
                                print('LA MARCA DEL PRODUCTO INGRESADO ES INEXISTENTE EN EL STOCK')
                                time.sleep(4)
                                system("cls")
                            else:
                                cantidadlimpieza = int(input('¿Cuantos productos quieres eliminar/reponer del stock?: '))
                                if cantidadlimpieza > i.cantidad:
                                    print ('¡HAS INGRESADO UN NUMERO MAYOR DEL STOCK QUE TIENES!')
                                    time.sleep(4)
                                    system("cls")
                                elif cantidadlimpieza < i.cantidad:
                                    i.cantidad = i.cantidad - cantidadlimpieza
                                    i.cantidad = i.cantidad
                                else:
                                    productosdelimpieza.remove(i)
                                    print ('¡YA NO TIENES MAS STOCK DE ESTE PRODUCTO!')
                                    time.sleep(3)
                                    system("cls")
                elif op == 2:
                    for j in productosdeforrajeria:
                        print("PRODUCTO:", j.prod,", MARCA: ", j.marca, ", PESO:", j.peso,", CANTIDAD: ", j.cantidad,", PRECIO:$",j.precio,", CODIGO DEL PRODUCTO: ", j.codigo)
                        productosforrajeria = input('¿Que producto quieres modificar: ')
                        if productosforrajeria != j.prod:
                            print('PRODUCTO INGRESADO INEXISTENTE EN EL STOCK')
                            time.sleep(3)
                            system("cls")
                        elif productosforrajeria == j.prod:
                            marcaforrajeria = input('Ingresa la marca del producto a modificar: ')
                            if marcaforrajeria != j.marca:
                                print('LA MARCA DEL PRODUCTO INGRESADO ES INEXISTENTE EN EL STOCK')
                                time.sleep(4)
                                system("cls")
                            else:
                                cantidadforrajeria = int(input('¿Cuantos productos quieres eliminar/reponer del stock?: '))
                                if cantidadforrajeria > j.cantidad:
                                    print ('¡HAS INGRESADO UN NUMERO MAYOR DEL STOCK QUE TIENES!')
                                    time.sleep(4)
                                    system("cls")
                                elif cantidadforrajeria < j.cantidad:
                                    j.cantidad = j.cantidad - cantidadforrajeria
                                    j.cantidad = j.cantidad
                                else:
                                    productosdeforrajeria.remove(j)
                                    print ('¡YA NO TIENES MAS STOCK DE ESTE PRODUCTO!')
                                    time.sleep(3)
                                    system("cls")
                elif op == 3:
                    for k in utensiliosdomesticos:
                        print("PRODUCTO:", k.prod,", MARCA: ", k.marca, ", PESO:", k.peso,", CANTIDAD: ", k.cantidad,", PRECIO:$",k.precio,", CODIGO DEL PRODUCTO: ", k.codigo)
                        productosudomesticos = input('¿Que producto quieres modificar: ')
                        if productosudomesticos != k.prod:
                            print('PRODUCTO INGRESADO INEXISTENTE EN EL STOCK')
                            time.sleep(3)
                            system("cls")
                        elif productosudomesticos == k.prod:
                            marcaud = input('Ingresa la marca del producto a modificar: ')
                            if marcaud != k.marca:
                                print('LA MARCA DEL PRODUCTO INGRESADO ES INEXISTENTE EN EL STOCK')
                                time.sleep(4)
                                system("cls")
                            else:
                                cantidadud = int(input('¿Cuantos productos quieres eliminar/reponer del stock?: '))
                                if cantidadud > k.cantidad:
                                    print ('¡HAS INGRESADO UN NUMERO MAYOR DEL STOCK QUE TIENES!')
                                    time.sleep(4)
                                    system("cls")
                                elif cantidadud < k.cantidad:
                                    k.cantidad = k.cantidad - cantidadud
                                    k.cantidad = k.cantidad
                                else:
                                    utensiliosdomesticos.remove(k)
                                    print ('¡YA NO TIENES MAS STOCK DE ESTE PRODUCTO!')
                                    time.sleep(3)
                                    system("cls")
                else:
                    print('HAS INGRESADO UNA OPCION INCORRECTA')
            else:
                print('HAS INGRESADO UNA OPCION INCORRECTA')
                time.sleep(3)
                system("cls")
        except:
            system("cls")
            print('HAS INGRESADO UNA OPCION INCORRECTA')
            time.sleep(3)
            system("cls")