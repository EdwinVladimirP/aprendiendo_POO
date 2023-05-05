"""POO (Programación Orientada a Objetos):
es un paradigma de programación que modula nuestro
códigi haciéndolo más entendible y reutilizable."""

"""La programación orientada a objetos se basa en crear 
tipos nuevos de datos a los que llamaremos:OBJETOS """

"""Para ello trataremos a nuestro código como un módulo
 con dos partes, porpiedades y funciones
 
 --------------
 |propiedades | ----->atributos
 |------------|
 |funciones   | ----->métodos
 --------------
 
 a los datos los llamaremos ATRIBUTOS y a las funciones
  les llamaremos MÉTODOS.
Los atributos son las propiedades que definen al objeto y 
Los métodos las acciones que puede realizar. 

 --------------
 |Clase ☕️    |                                |objeto☕️|
 |------------|                                |      |
 |PROPIEDADES |                                |------|
 |-volumen    |                                |-150  |
 |-líquido    |->atributos->construct(150,café)|-café |
 |-cantidad   |                                |-100  |
 |------------|                                --------
 |FUNCIONES   |
 |-llenar()   |                                |objeto☕️|
 |-beber()    |->métodos->constructor(250,té)  |      |
 |-vaciar()   |                                |-250  |
 --------------                                |-té   |
                                               |-200  |
                                               --------
 """

"""Abstracción: cuando seleccionamos una clase, debemos seleccionar
atributos y métodos que va a tener
"""

"""
class Personaje:
    nombre = 'León'
    fuerza = 0
    inteligencia = 3
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        # self, es un argumento que hace referenci así mismo, al objeto
        # y permite a traves del punto tener acceso a los atributos y métodos de la clase. 
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

# https://www.youtube.com/watch?v=JVNirg9qs4M
# 03:47
mi_personaje = Personaje("Big Boss", 98, 99, 100, 100)
# --->se ha creado el objeto mi_personaje
print(f"El nombre de mi personaje es: {mi_personaje.nombre}")
tu_personaje = Personaje("Rambo", 25, 30, 35, 40)
print(tu_personaje.nombre, tu_personaje.vida)
mi_personaje.vida = 99  # --->se ha alterado el valor de "vida"

print(f"Mi personaje tiene de vida: {mi_personaje.vida}")
"""

# EJEMPLO DEL VIDEO:
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self_.nombre = nombre
        self_.fuerza = fuerza
        self_.inteligencia = inteligencia
        self_.defensa = defensa
        self_.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza: ", self.fuerza)
        print("inteligencia: ", self.inteligencia)
        print("defensa: ", self.defensa)
        print("vida: ", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def morir(self):
        self.vida = 0
        print("😢...ha muerto...")

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

mi_personaje = Personaje("BigBoss", 8, 7, 9, 10)
enemigo_personaje = Personaje("Enemigo dark", 8, 5, 3, 6)
mi_personaje.atributos()
print("_-_-_-_-_-_-_-_-_-_-_-_")
mi_personaje.subir_nivel(2, 2, 2)
print(enemigo_personaje.atributos())

print("_-_-_-_-_-_-_-_-_-_-_-_")
print(mi_personaje.daño(enemigo_personaje))
mi_personaje.atacar(enemigo_personaje)
enemigo_personaje.atributos()


