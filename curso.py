# Ejercicio: Mostrar la versión actual de Python instalada.

import sys

'''El módulo "sys" proporciona una serie de variables y funciones que
 permiten interactuar con el intérprete de Python.'''

print(sys.version)
print(sys.version_info)

# Ejercicio: Exponer el uso básico de la función print.

print(f"Este es un ejemplo básico", end='')

'''Además, el argumento "end=''" se utiliza para especificar que la 
función "print()" no agregará un carácter de nueva línea al final de 
la cadena impresa, lo que significa que la próxima línea impresa comenzará
 inmediatamente después del final de esta línea.'''

print("nombre = Juan", end='')
print("hola mundo")
print("buenos días...")
print("ejemplo", "gmail", sep='@')  # Ejemplo con: sep='-', ó usando sep='@'
print(1, 2, 3, 4, 5, sep='@')
print('{} es {}'.format("Python", "tremendo"))
'''La función "format()" se utiliza para crear una cadena de formato y 
reemplazar los marcadores de posición "{}" con los valores proporcionados
 como argumentos en la función. En este caso, la cadena de formato es "{} es {}", 
 lo que significa que hay dos marcadores de posición que se reemplazarán con
  los valores "Python" y "tremendo" respectivamente.'''

# usando .format("palabra", "palabra", "palabra")
historia = "una pequeña {} en lo profundo del {},\n donde " \
           "cuenta la {} que hace muchos {},\n hubo un {}" \
           "de aspecto muy {} "
print(historia.format("casa", "bosque", "leyenda", "años", "ser", "curioso"))

# Ejercicio: Obtener la fecha y hora actuales en el sistema.

import datetime

ahora = datetime.datetime.now()
print(type(ahora))
print(ahora.strftime('%d/%m/%y'))  # se reformatéa la manera de presentar la fecha.


