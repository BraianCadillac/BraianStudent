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
from ProductosDeForrajeria import *
from ProductosDeLimpieza import *
from ProductosUDomesticos import *
from Productos import *
from Cajas import *

def Iniciar(lista):
    producto1 = ProductosDeLimpieza(1, "Destergente", "Magistral", 15, 900, "asdfasfa", "1lt")
    producto2 = ProductosDeLimpieza(2, "Destergente", "Cif", 25, 1900, "32f23f32", "2lt")
    producto3 = ProductosDeLimpieza(3, "Jabon en polvo", "Ala", 9, 1500, "f32f32", "1lt")
    lista.append(producto1)
    lista.append(producto2)
    lista.append(producto3)
    return lista

def lista(lista):
    print('------------------------------------------------------------------------------------------------------------------------------')
    for i in lista:
        print(i.contador,":  PRODUCTO:", i.prod,", MARCA: ", i.marca, ", PESO:", i.peso,", CANTIDAD: ", i.cantidad,", PRECIO:$",i.precio,", CODIGO DEL PRODUCTO: ", i.codigo)
    print('------------------------------------------------------------------------------------------------------------------------------')

productosdelimpieza = []
productosdeforrajeria = []
utensiliosdomesticos = []
Cajeros = []
productosdelimpieza = Iniciar(productosdelimpieza)
while True:
        print('------------------------------------------------------------------------------------------------------------------------------')
        print('\t\t\t\t\t\tLA FAMILIA SOSA')
        print('------------------------------------------------------------------------------------------------------------------------------')
        time.sleep(3)
        system("cls")
        print('------------------------------------------------------------------------------------------------------------------------------')
        print ("1. Ingresar productos al stock")
        print ("2. Lista de productos del stock")
        print ("3. Modificar producto")
        print ("4. Cajas")
        print('------------------------------------------------------------------------------------------------------------------------------')
        print ("0. Salir")
        print('\b')
        try:
            op = int(input('Ingrese numero de opcion: '))
            system("cls")
            if op == 1:
                while op != 0:
                    print('------------------------------------------------------------------------------------------------------------------------------')
                    print("1. Ingresar productos de limpieza")
                    print("2. Ingresar productos de Forrajeria")
                    print("3. Ingresar productos de Utensilios Domesticos")
                    print('------------------------------------------------------------------------------------------------------------------------------')
                    print("0. Volver al Menu principal")
                    print('\b')
                    op = int(input('Ingrese numero de opcion: '))
                    system("cls")
                    if op == 1:
                        while op != 0:
                            print('------------------------------------------------------------------------------------------------------------------------------\n\t\t\t\t\t\tPRODUCTOS DE LIMPIEZA\n------------------------------------------------------------------------------------------------------------------------------')
                            time.sleep(2)
                            system("cls")
                            print('0. Volver\n------------------------------------------------------------------------------------------------------------------------------')
                            contadorl = 1
                            for i in productosdelimpieza:
                                if contadorl == i.contador:
                                    contadorl+=1
                            productoslimpieza = input('Ingresar producto: ')
                            if productoslimpieza == '0':
                                system("cls")
                                print('CARGANDO...')
                                time.sleep(1)
                                system("cls")
                                break
                            system("cls")
                            marcalimpieza = input('Ingresa la marca: ')
                            cantidadlimpieza = int(input('¿Cuantos quieres ingresar?: '))
                            preciol = int(input('Precio del producto unitario: $'))
                            codigolimp = input('Codigo de producto: ')
                            pesolimp = input('Ingresar peso del producto de limpieza: ')
                            productolimp = ProductosDeLimpieza(contadorl, productoslimpieza, marcalimpieza, cantidadlimpieza, preciol, codigolimp, pesolimp)
                            productosdelimpieza.append(productolimp)
                            system("cls")
                            print('PRODUCTO INGRESADO CON EXITO')
                            time.sleep(2)
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
                        time.sleep(2)
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
                        time.sleep(2)
                        system("cls")
                    elif op == 0:
                        print ("CARGANDO...")
                        time.sleep(1)
                        system("cls")
                        break
                    else:
                        print('¡HAS INGRESADO UNA OPCION INCORRECTA!')
                        time.sleep(2)
                        system("cls")
            elif op == 2:
                while op != 0:
                    print('------------------------------------------------------------------------------------------------------------------------------')
                    print("1. Lista de productos Limpieza")
                    print("2. Lista de productos de Forrajeria")
                    print("3. Lista de productos de Utensilios domesticos")
                    print("4. Ordenar lista de productos de limpieza")
                    print("5. Ordenar lista de productos de Forrajeria")
                    print("6. Ordenar lista de Utensilios Domesticos")
                    print('------------------------------------------------------------------------------------------------------------------------------')
                    print("0. Volver al Menu principal")
                    print('\b')
                    op = int(input('Ingrese numero de opcion: '))
                    system("cls")
                    if op == 1:
                        if len(productosdelimpieza) == 0:
                            print('AUN NO TIENES PRODUCTOS DE LIMPIEZA EN EL STOCK')
                            time.sleep(2)
                            system("cls")
                        else:
                            lista(productosdelimpieza)
                            
                    elif op == 2:
                        if len(productosdeforrajeria) == 0:
                            print ('AUN NO TIENES PRODUCTOS DE FORRAJERIA EN EL STOCK')
                            time.sleep(2)
                            system("cls")
                        else:
                            productoforr.Lista(productosdeforrajeria)
                    elif op == 3:
                        if len(utensiliosdomesticos) == 0:
                            print ('AUN NO TIENES PRODUCTOS DE UTENSILIOS DOMESTICOS')
                            time.sleep(2)
                            system("cls")
                        else:
                            productoud.Lista(utensiliosdomesticos)
                    elif op == 0:
                        print ("CARGANDO...")
                        time.sleep(1)
                        system("cls")
                        break
                    else:
                        print('¡HAS INGRESADO UNA OPCION INCORRECTA!')
            elif op == 3:
                while op != 0:
                    print('------------------------------------------------------------------------------------------------------------------------------')
                    print ("1. Modificar productos de limpieza")
                    print ("2. Modificar productos de Forrajeria")
                    print ("3. Modificar productos de utensilio domesticos")
                    print('------------------------------------------------------------------------------------------------------------------------------')
                    print ("0. Volver al Menu principal")
                    print('\b')
                    op = int(input('Ingrese numero de opcion: '))
                    system("cls")
                    if op == 1:
                        if len(productosdelimpieza) == 0:
                            system("cls")
                            print ('AUN NO TIENES PRODUCTOS DE LIMPIEZA EN EL STOCK')
                            time.sleep(2)
                            system("cls") 
                        elif len(productosdelimpieza) > 0:
                            lista(productosdelimpieza)
                            print('\b')
                            opcion = int(input("Ingrese numero de producto para modificar: "))
                            if opcion <= 0:
                                system("cls")
                                print('¡HAS INGRESADO UN NUMERO DE PRODUCTO QUE NO EXISTE!')
                                time.sleep(2)
                                system("cls")
                            elif opcion > len(productosdelimpieza):
                                system("cls")
                                print('¡HAS INGRESADO UN NUMERO DE PRODUCTO QUE NO EXISTE!')
                                time.sleep(2)
                                system("cls")
                            else:
                                Productos(3, "Jabon en polvo", "Ala", 25, 1500, "f32f32", "1lt").ModificacionDeProducto(productosdelimpieza, opcion)
                        else:
                            pass
                    elif op == 2:
                        if len(productosdeforrajeria) == 0:
                            system("cls")
                            print ('AUN NO TIENES PRODUCTOS DE FORRAJERIA EN EL STOCK')
                            time.sleep(2)
                            system("cls")
                        else:
                            productoforr.Lista(productosdeforrajeria)
                            productosforrajeria = input('¿Que producto quieres modificar: ')
                            productoforr.ModificacionDeProductoLyF(productosdeforrajeria, productosforrajeria)
                    elif op == 3:
                        if len(utensiliosdomesticos) == 0:
                            system("cls")
                            print ('AUN NO TIENES PRODUCTOS DE UTENSILIOS DOMESTICOS')
                            time.sleep(2)
                            system("cls")
                        else:
                            productoud.Lista(utensiliosdomesticos)
                            udomesticos = input('¿Que producto quieres modificar: ')
                            productoud.ModificacionDeProducto(utensiliosdomesticos, udomesticos)
                    elif op == 0:
                        print ("CARGANDO...")
                        time.sleep(2)
                        system("cls")
                        break
                    else:
                        print('HAS INGRESADO UNA OPCION INCORRECTA')
                        time.sleep(2)
                        system("cls")
            elif op == 4:
                while op != 0:
                    print('------------------------------------------------------------------------------------------------------------------------------')
                    print ("1. Ingresar datos del personal de Caja")
                    print ("2. Lista de Cajeros")
                    print('------------------------------------------------------------------------------------------------------------------------------')
                    print("0. Volver")
                    print ("\b")
                    op = int(input('Ingrese numero de opcion: '))
                    system("cls")
                    if op == 1: 
                        while op != 0:
                            print('0. Volver')
                            print('------------------------------------------------------------------------------------------------------------------------------')
                            print('\b')
                            time.sleep(1)
                            contadorcaj = 1
                            for c in Cajeros:
                                if contadorcaj == c.caja:
                                    contadorcaj+=1
                            nom = input('Ingresar nombre: ')
                            if nom == '0':
                                system("cls")
                                print('CARGANDO...')
                                time.sleep(1)
                                system("cls")
                                break
                            system("cls")
                            ape = input('Apellido: ')
                            nac = input('Fecha de nacimiento: ')
                            dni = input('N° de DNI: ')
                            cajero = Caja(contadorcaj, nom, ape, nac, dni)
                            Cajeros.append(cajero)
                            system("cls")
                            print ('¡DATOS INGRESADOS CON EXITO!')
                            time.sleep(2)
                            system("cls")
                    elif op == 2:
                        if len(Cajeros) == 0:
                            system("cls")
                            print('¡AUN NO SE ENCUENTRAN DATOS DE LOS CAJEROS!')
                            time.sleep(2)
                            system("cls")
                        else:
                            cajero.MostrarLista(Cajeros)
                            time.sleep(1)
                    elif op == 0:
                        print ("CARGANDO...")
                        time.sleep(2)
                        system("cls")
                        break
                    else:
                        print('HAS INGRESADO UNA OPCION INCORRECTA')
                        time.sleep(2)
                        system("cls")
                
            elif op == 0:
                print ("¡HASTA PRONTO!")
                time.sleep(3)
                system("cls")
                break
                
            else:
                print('HAS INGRESADO UNA OPCION INCORRECTA')
                time.sleep(2)
                system("cls")
        except Exception as e:
            system("cls")
            print(e)
            time.sleep(15)
            system("cls")