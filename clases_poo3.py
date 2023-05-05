"""
-Programación orientada a objetos
-Clase
    -Método
    Atributo
-Objeto
-Constructor

    __init__
    Un constructor es un método(función) de nombre __init__ que se
    ejecuta cada vez que se crea un objeto de la clase.
    Todos los métodos de la clase, reciben como primer parámetro self
    self('yo mismo') es una referencia al objeto actual, al objeto mismo que
    ejecuta el método.

        def __init__(self, num = 0, den = 1):
            self.num=num
            self.den=den
"""


class Cerveza:

    def __init__(self, nombre="🤖🍺Cerveza sin nombre :("):
        self.nombre = nombre

    def añejar(self, tiempo=5):  # ------> opcional colocar el valor por defecto.
        self.tiempo = tiempo
        print(f"Tu cerveza {self.nombre} se ha añejado {self.tiempo} años")


miCerveza = Cerveza("🍺 Chapulteca!")
<<<<<<< HEAD


# print(miCerveza.nombre)
# miCerveza.añejar()


# **************************************************************************************************************

class Naves:
    peso = 2500
    largo = 50
    ancho = 20
    color1 = "Negro"
    color2 = "Plateado"
    motores = 4
    activada = False
    compuerta_principal = True
    sistema_defensa = True
    autodestruccion = False

    def encender(self):
        self.activada = True

    def apagar(self):
        self.activada = False

    def abrir_compuerta(self):
        self.compuerta_principal = True

    def cerrar_compuerta(self):
        self.compuerta_principal = False

    def desactivar_defensa(self):
        self.sistema_defensa = False

# https://www.youtube.com/watch?v=eSYuUb6y59M
=======
print(miCerveza.nombre)
miCerveza.añejar()
>>>>>>> origin/master
