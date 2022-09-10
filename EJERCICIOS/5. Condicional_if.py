## Determine si un número es mayor a 18, utilizando el condicional IF

numero = 19
if numero > 18:
    print("Número es mayor a 18")

## Determine si un número es mayor o no a 18, utilizando el condicional IF -- ELSE


numero = 18
if numero > 18:
    print("Número es mayor a 18")
else:
    print("Número no es mayor a 18")

## Pedir al usuario que ingrese 3 numeros, luego, retornar el numero mayor y el menor

# Forma Laura
print('Ingrese 3 numeros')
Numero1 = int(input('Ingrese el Numero 1: '))
Numero2 = int(input('Ingrese el Numero 2: '))
Numero3 = int(input('Ingrese el Numero 3: '))

if Numero1 > Numero2:
    if Numero2 > Numero3:
        Mayor = Numero1
        Menor = Numero3
    else:
        if Numero3 > Numero1: 
            Mayor = Numero3
            Menor = Numero2
        else:
            Mayor = Numero1
            Menor = Numero2
else:
    if Numero1 > Numero3:
        Mayor = Numero2
        Menor = Numero3
    else:
        if Numero3 > Numero2:
            Mayor = Numero3
            Menor = Numero1

print('Mayor:', Mayor, 'Menor:', Menor)
        
# Forma profe

if (Numero1 >= Numero2) and (Numero1 >= Numero3):
    Mayor = Numero1
elif (Numero2 >= Numero1) and (Numero2 >= Numero3):
    Mayor = Numero2
else:
    Mayor = Numero3

print('Mayor:', Mayor, 'Menor:', Menor)