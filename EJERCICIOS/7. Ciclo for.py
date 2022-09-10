alturas = [10, 20, 50, 80, 1, 50]
pesos = (70, 60, 55, 62, 45, 90)
mensaje = "Hola Mungo Cruel"
secuencia = range(1, 11, 1)

print('altura')
for altura in alturas:
    print(altura)

print('msg')
for msg in mensaje:
    print(msg, end = " ")

print('peso')
for peso in pesos:
    print(peso)

print('secuencia')
for s in secuencia:
    print(s)

# Utilizando el ciclo for generar las siguientes secuencias:
#    * 10, 11, 12, 13, 14, 15, 16, .. 29
for i in range(10, 21, 1):
    print(i, end = " ")
print()
#    * 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
for i in range(3, 31, 3):
    print(i, end = " ")
print()
#    * 3, 6, 9, 12, 15, 18, 21, 24, 27, 33, 36, 39, 42, 45
for i in range(3, 46, 3):
    if i != 30 :
        print(i, end = " ")
print()
#    * número pares del 200 al 400
for i in range(200, 401, 2):
    print(i, end = " ")
print()
#    * las primeras 20 potencias de 2
for i in range(1,21):
     print(2**i, end = " ")
print()
#    * Multiplos de 5 del 10 al 50

