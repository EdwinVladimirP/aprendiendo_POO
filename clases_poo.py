class Book:

    def __init__(self, title, author, price, stock, oid):
        self._title = title
        self._author = author
        self._price = price
        self._stock = stock
        self._oid = oid
        # Getters / Setters
        # get -> obtener(lectura)
        # set -> setear/establecer (escritura)

    def get_info(self):
        return f"""\n Titulo: {self._title} \n Autor: {self._author} \n Precio: {self._price} \n Stock: {self._stock} \n Identificación: {self._oid}"""

    def set_price(self, new_price):
        if new_price > 50:
            self._price = new_price
            print("Aplicado el nuevo valor!")
        else:
            print("No aplica el valor inferior a 51")


# *****************************ÁREA DE CÓMIC************************

class Comic(Book):

    def __init__(self, title, author, price, stock, oid, ilustrator, vol):  # --->se agregaron 2 propiedades, hay que definirlas normal (ya que no pertenecen a la clase super
        super().__init__(title, author, price, stock, oid)
        self._ilustrators = ilustrator  # ----------------------------------------->definidas
        self._vol = vol  # -------------------------------------------------------->definidas

    def get_info(self):
        #  return super().get_info()
        info = super().get_info()
        str_ilustrators = ','.join(self._ilustrators)
        return info + f"""\n Ilustradores: {str_ilustrators}\n Vol. {self._vol}"""


comic1 = Comic("Batman - the killing joke", 'no recuerdo', 30, 70, 1, ['ilus1', 'ilus2'], 1)
comic2 = Comic("Ninja", "Azuke", 31, 69, 2, "Akira", 1.0)

book1 = Book("Así habló zaratustra", "Nietzche", 250.0, 100, 1)
print(book1._title)
print(book1._price)
print("===Otro Libro===")
book2 = Book("1984", 'G. Orwell', 150.0, 50, 2)
print(book2._title)
print(book2._price)
print("===Otro Libro===")
book3 = Book("El Jardín del Eden", "Carl Sagan", 300.0, 75, 3)
print(book3._title)
#  book3.set_price(50)  # ---------->se cambió el precio usando la función def set_price(self, new_price)
print(book3._price)
print("-*-*-*INFORMACIÓN*-*-*")
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
# book3._price = 0.0  # ----------->ejemplo de alteración de datos(vamos a evitar esto con el encapsulamiento!)
print(f"\n =====INICIO DE EL ÁREA CÓMIC, se utilizará herencia en POO. =====")
print(comic1.get_info())


"""Abstracción:
Abstraer, es eliminar los detalles innecesarios para solo
enfocarnos en los aspectos que son relevantes para el contexto(sistema que estamos desarrollando)"""

"""Encapsulamiento: 
Es ocultar los detalles que no son relevantes para el exterior.
agrupar propiedades y métodos de manera que 👉el acceso está restringido desde afura del paquete👈. """

"""Herencia:
La POO nos permite crear clases hijas que ehredan propiedades y métodos 
de una clase padre con la intención de tener objetos especializados. """

"""Polimorfismo:
Se refiere a la capacidad de realizar una misma acción en diferentes formas. """

# https://www.youtube.com/watch?v=InPVEFDvWT0.
