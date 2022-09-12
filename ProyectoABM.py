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

class Productos():
    def __init__(self, prod, marca, cantidad, precio, codigo):
        self.prod = prod
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
        self.codigo = codigo
class ProductosDeLimpieza(Productos):
    def __init__(self, prod, marca, cantidad, precio, codigo):
        super().__init__(prod, marca, cantidad, precio, codigo)
productosdelimpieza = []

while True:
    print ("1. Ingresar productos al stock")
    print ("2. Lista de productos del stock")
    print ("3. Modificar producto")
    op = int(input('Ingrese numero de opcion: '))
    if op == 1:
        print("1. Ingresar productos de limpieza")
        print("2. Ingresar productos de Forrajeria")
        print("3. Ingresar productos de Utensilios Domesticos")
        op = int(input('Ingrese numero de opcion: '))
        if op == 1:
            productoslimpieza = input('Ingresar producto: ')
            marcalimpieza = input('Ingresa la marca: ')
            cantidadlimpieza = int(input('¿Cuantos quieres ingresar?: '))
            precio = int(input('Precio del producto : $'))
            codprodlimp = input('Codigo de producto: ')
            productolimp = ProductosDeLimpieza(productoslimpieza, marcalimpieza, cantidadlimpieza, precio, codprodlimp)
            productosdelimpieza.append(productolimp)
    if op == 2:
        print("1. Lista de productos limpieza")
        print("2. Lista de productos de Forrajeria")
        print("3. Lista de productos de Utensilios domesticos")
        op = int(input('Ingrese numero de opcion: '))
        if op == 1:
            for i in productosdelimpieza:
                print("Producto:", i.prod,", Marca: ",i.marca,", Cantidad: ",i.cantidad,", Precio:$",i.precio,", Codigo del producto: ",i.codigo)
    if op == 3:
        print ("1. Modificar productos de limpieza")
        print ("2. Modificar productos de Forrajeria")
        print ("3. Modificar productos de utensilio domesticos")
        op = int(input('Ingrese numero de opcion: '))
        if op == 1:
            productoslimpieza = input('¿Que producto quieres modificar: ')
            marcalimpieza = input('Ingresa la marca del producto a modificar: ')
            for i in productosdelimpieza:
                if i.prod == productoslimpieza and i.marca == marcalimpieza:
                    cantidadlimpieza = int(input('¿Cuantos productos quieres eliminar del stock?: '))
                    cantidad = i.cantidad - cantidadlimpieza
                    i.cantidad = cantidad
                    if cantidad == 0:
                        print ("No tienes mas stock de este producto")