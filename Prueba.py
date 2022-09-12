'''Este software debe permitirme realizar el alta, baja, modificación y listado de productos 
por cada categoría, donde necesito cargar por cada producto su marca 
- modelo/producto - grupo/categoria - precio - peso/volumen (liquido) - cantidad a ingresar/stock 
- código de artículo (único por cada articulo que debe ser generado por el mismo software).
Requiero dar de alta -baja - modificación - listado de cajeros y cajas habilitadas.'''


class ProductosLimpieza():
    def __init__(self, prodlimp, marca, cantidad):
        self.prodlimp = prodlimp
        self.marca = marca
        self.cantidad = cantidad
productoslimpieza =  []

class ProductosForrajeria():
    def __init__(self, prodforr, marca):
        self.prodforr = prodforr
        self.marca = marca
        self.cantidad = 0
productosforrajeria = []

class UtensiliosDomesticos():
    def __init__(self, proddom, marca):
        self.proddom = proddom
        self.marca = marca
        self.cantidad = 0
productosdomesticos = []

while True:
    print("1) Insertar productos de limpieza al stock.")
    print("2) Insertar productos de Forrajeria al stock: ")
    print("3) Insertar productos de Utensilios Domesticos: ")
    print("4) Listado de los productos de limpieza.")
    print("5) Listado de los productos de forrajeria.")
    print("6) Listado de los productos de Utensilios Domesticos.")
    print("7) Dar de baja los productos ingresados")
    op = int(input('Ingrese numero de opcion: '))

    if op == 1:
        prodelimpieza = input('Insertar producto de Limpieza al stock: ')
        marcalimp = input('Marca del producto: ')
        cant = int(input('Cantidad a agregar en el stock: '))
        prodelimpieza = ProductosLimpieza(prodelimpieza, marcalimp, cant)
        productoslimpieza.append(prodelimpieza)
    elif op == 2:
        prodeforrajeria = input('Insertar productos de Forrajeria al stock: ')
        marcaforr = input('Marca del producto: ')
        prodeforrajeria = ProductosForrajeria(prodeforrajeria, marcaforr)
        productosforrajeria.append(prodeforrajeria)
    elif op == 3:
        prodeutensilios = input("Insertar productos de utensilios Domesticos: ")
        marcadom = input('Marca del producto: ')
        prodeutensilios = UtensiliosDomesticos(prodeutensilios, marcadom)
        productosdomesticos.append(prodeutensilios)
    elif op == 4:
        if len(productoslimpieza) == 0:
            print('Aun no se encuentran productos de Limpieza en el stock.')
        else:
            for x in productoslimpieza:
                print("Producto:",x.prodlimp,", Marca:",x.marca, ", Cantidad:",x.cantidad)
    elif op == 5:
        if len(productosforrajeria) == 0:
            print('Aun no se encuentran productos de Forrajeria en el stock')
        else:
            for j in productosforrajeria:
               print("Producto:",j.prodforr,", Marca:",j.marca)
    elif op == 6:
        if len(productosdomesticos) == 0:
            print('Aun no se encuentran productos Domesticos en el stock')
        else:
            for i in productosdomesticos:
                print("Producto:",i.proddom,", Marca:",i.marca)
    elif op == 7:
        print('1) Eliminar productos de Limpieza')
        print('2) Eliminar productos de Forrajeria')
        print('3) Eliminar productos Domesticos')
        op1 = int(input('Ingrese numero de opcion: '))
        if op1 == 1:
            try:
                proddelete=input('¿Que producto desea eliminar?: ')
                marcdelete=input('¿Marca del producto?: ')
                cantprod=int(input('¿Cuántos productos desea eliminar?: '))
                for q in productoslimpieza:
                    if q.prodlimp == proddelete:
                        delattr (prodelimpieza, 'prodlimp')
                    if q.marca == marcdelete:
                        delattr (prodelimpieza, 'marca')
                    totalcantidad = q.cantidad - cantprod
                    prodelimpieza = ProductosLimpieza(proddelete, marcdelete, totalcantidad)
                    productoslimpieza.append(prodelimpieza)
                    break
            except:
                print('Haz ingresado una cantidad mayor al stock o un producto erroneo')
        else:
            print('Opcion de numero erronea')