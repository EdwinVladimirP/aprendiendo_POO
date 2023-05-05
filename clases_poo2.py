"""Programación Orientada a Objetos:
-paradigma de programación:
    Imita los objetos de la vida real, consus proiedades y
    comportamientos, en los lenguajes de programación.
-¿Qué nos aporta?:
    1-Genera código mucho más modular
    2-Reutilización del código
    3-Encapsulamiento y simplificación"""

"""Que es un Objeto?:
Un objeto se forma principalmente por dos elementos: 
    Datos: desvriben el estado o las características del objeto. A los
    datos de un objeto los llamaremos PROPIEDADES o ATRIBUTOS.
    
ejemplo:
    Objeto: Camiseta.
    Atributos: Una camiset puede tener un precio, una marca, un color, y una talla.
    Métodos: Podemos rebajar el precio o teñirla para cambiar su color. """

"""Que son las Clases: 
    Una clase es el modelo para un grupo de objetos.
    La clase define los métodos y atributos comunes de todos los objetos que pertenecen a una 
    misma clase.
    A un objeto que pertenece a una clase se le llama INSTANCIA.
ejemplo: 
    Clase: Camisetas. Todos los objetos de la clase camisetas tendrán un 
    precio, una marca y u color. 
    Cada instancia de Camisetas tendrá un precio, color y talla distintos .
"""

"""Pilares de la POO
-->HERENCIA
-->POLIMORFISMO
-->ENCAPSULACIÓN
-->ABSTRACCIÓN
"""


# ******************************************************

class Camisetas:
    def __init__(self, marca, precio, talla, color):
        self.marca = marca
        self.precio = precio
        self.talla = talla
        self.color = color
        self.rebaja = False

    def aplicarDescuento(self, porcentaje):
        self.precio = self.precio - self.precio * porcentaje / 100
        if porcentaje < 100:
            self.rebaja = True

    def infoProducto(self):
        info = f"Descripción de la camiseta\nMarca: {self.marca}\nPrecio: ${self.precio:.2f}\nTalla: {self.talla}\nColor: {self.color}\n"
        if self.rebaja:
            info += "Este Producto Está Rebajado"
        return info


camiseta = Camisetas("Nike", 19.99, "S", "lila")
camisetaAdidas = Camisetas("Adidas", 30.50, "M", "Grey")
# --------------->Aplicando descuento<-------------------
# print(camisetaAdidas.precio)
# camisetaAdidas.aplicarDescuento(50)  # -------->Aplicando 50% de descuento
# print(camisetaAdidas.precio)

# print(camiseta.precio)
# camiseta.aplicarDescuento(50)  # -------------->Aplicando 50% de descuento
# print(camiseta.precio)

camiseta.aplicarDescuento(50)
print(camiseta.infoProducto())
print("*****************************")  # ---->he aplicado un descuento.
camisetaAdidas.aplicarDescuento(50)
print(camisetaAdidas.infoProducto())
