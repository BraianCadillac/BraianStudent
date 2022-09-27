class Caja():
    def __init__(self, caja, nombre, apellido, nacimiento, dni):
        self.caja = caja
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.dni = dni
    def MostrarLista(self, lista):
        print('------------------------------------------------------------------------------------------------------------------------------')
        for i in lista:
            print(i.caja,":  NOMBRE:", i.nombre,", APELLIDO: ", i.apellido, ", FECHA DE NACIMIENTO:", i.nacimiento,", N° DE DNI: ", i.dni)
        print('------------------------------------------------------------------------------------------------------------------------------')