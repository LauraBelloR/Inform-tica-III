""" Crear un ciclo infinito"""

# while True:
#   print('ciclo ejecutado')

""" Crear un ciclo infinito, pero protegerlo en caso de que se ejecute más veces"""

contador = 0
while True:
    print('ciclo ejecutado {}'.format(contador))
    contador = contador + 1

    if contador > 100:
        print('Contador superado')
        print('Vamos a romper la ejecución')
        break

""" Imprima los numeros del 20 al 50"""
n = 20
while n <= 50:
    print(n)
    n = n + 1

""" Mostrar en pantalla los primeros 10 numero de fibonacci"""
n = 3
fibant = 1
fibact = 1
print(fibant)
print(fibact)
while n <= 10:
    fibsig = fibant + fibact
    print(fibsig)
    fibant = fibact
    fibact = fibsig
    n += 1
