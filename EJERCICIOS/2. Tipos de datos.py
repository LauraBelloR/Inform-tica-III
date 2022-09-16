# Agosto 26/2022
# Declaramos los siguientes elementos y asignamos en variables de su elección:

# Enteros: 10, -100, 500, 200 ==> Luego restelos de manera sucesiva
from xmlrpc.client import boolean


a = 10
b = -100
c = 500
d = 200 

resultado = a-b-c-d
print(resultado)

# Flotantes; 100.0, 305.2, 400.3 ==> dividalos de manera sucesiva
A, B, C = 100.0, 305.2, 400.3
resultado2 = A / B / C
print("Resultado 2:",resultado2)

# Booleanos: True, False ==> Primero sumelos y luego restelos
a = True
b = False
sumaBooleanos = a + b
restaBooleanos = a - b

print(sumaBooleanos)
print(restaBooleanos)
# Strings: "Cristian", "Juanita" ==> Sumelos, restelos
#           "", '', """","''"   ==> ¿Qué sucede?
nombre1 = "Cristian"
nombre2 = "Juanita" 
cadena1 = ""
cadena2 = ''
# cadena3 = """" Esto no se puede hacer
cadena4 = "''"
cadena5 = '""'


print("nombre1 =>",nombre1)
print("nombre2 =>",nombre2)
print("cadena1 =>",cadena1)
print("cadena2 =>",cadena2)
print("cadena4 =>",cadena4)
print("cadena5 =>",cadena5)

suma = nombre1 + nombre2
print("suma = > ", suma)   # concatenación
# no se puede hacer resta nombre1 - nombre2

# Busque la manera de convertir: (casteo)
# Un entero a flotante
# Un flotante a un entero
# Un flotante y un entero a un string
# Un string a un entero y flotante
# Un Booleano a un entero y flotante
# Un entero y flotante a booleano

entero = 10
flotante = 11.95
string = "Manizales"
string2 = "123"
booleano = True

print("E a F ==>", entero, float(entero))
print("F a E ==>", flotante, int(flotante))  # Elimina el decimal sin redondear
print("E a S ==>", entero, str(entero))
print("F a S ==>", flotante, str(flotante))
#print("S a E ==>", string, int(string))    # No se puede porque no es un numero
#print("S a F ==>", string, float(string))  # No se puede porque no es un numero
print("S a E ==>", string2, int(string2))
print("S a F ==>", string2, float(string2))
print("B a E ==>", booleano, int(booleano))
print("B a F ==>", booleano, float(booleano))
print("E a B ==>", entero, bool(entero))
print("F a B ==>", flotante, bool(flotante))

lista = [1, 2, 3, 8, 9]
tupla = (1, 4, 8, 0, 5)
conjunto = set([1, 3, 1, 4])
diccionario = {'a': 1, 'b': 3, 'z': 8}
print(lista)
print(tupla)
print(conjunto)
print(diccionario)

