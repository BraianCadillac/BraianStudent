'''Este software debe permitirme realizar el alta, baja, modificación y listado de productos 
por cada categoría, donde necesito cargar por cada producto su marca 
- modelo/producto - grupo/categoria - precio - peso/volumen (liquido) - cantidad a ingresar/stock 
- código de artículo (único por cada articulo que debe ser generado por el mismo software).
Requiero dar de alta -baja - modificación - listado de cajeros y cajas habilitadas.'''
#chanchito feliz

class ProductosLimpieza():
    def __init__(self, prodlimp, marca):
        self.prodlimp = prodlimp
        self.marca = marca
productoslimpieza =  []

class ProductosForrajeria():
    def __init__(self, prodforr, marca):
        self.prodforr = prodforr
        self.marca = marca
productosforrajeria = []

class UtensiliosDomesticos():
    def __init__(self, proddom, marca):
        self.proddom = proddom
        self.marca = marca
productosdomesticos = []

while True:
    print("1) Insertar productos de limpieza al stock.")
    print("2) Insertar productos de Forrajeria al stock: ")
    print("3) Insertar productos de Utensilios Domesticos: ")
    print("4) Listado de los productos de limpieza.")
    print("5) Listado de los productos de forrajeria.")
    print("6) Listado de los productos de Utensilios Domesticos.")
    op = int(input('Ingrese numero de opcion: '))

    if op == 1:
        prodelimpieza = input('Insertar productos de Limpieza al stock: ')
        marcalimp = input('Marca del producto: ')
        prodelimpieza = ProductosLimpieza(prodelimpieza, marcalimp)
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
                print("Producto:",x.prodlimp,", Marca:",x.marca)
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