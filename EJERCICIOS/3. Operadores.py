# Agosto 31/2022

#####################  Operadores aritméticos ##################### 

print("Suma            ==>", 1+2+3)
print("mult y Sum      ==>", 1*2+3)
print("Suma y mult     ==>", 1+2*3)
print("División entera ==>", 5//3)
print("División entera ==>", 0//3)
print("Residuo         ==>",5%2)
print("Residuo         ==>",13%9)
print("Potenciación    ==>",9**2)
print("Potenciación    ==>",9**0.5)

# Orden de operaciones: **, */, +-

print("Concatenación ==>", "hola" + " mundo")
print("Replicación   ==>", "a"*10)
print("Concatenación ==>", [1]+ [1,2,3])       #Usando listas
print("Replicación   ==>", [0]*10)             #Usando listas


##################### Operadores lógicos ##################### 
print("and ==>",True and False) # Solo es verdadero si ambos son verdadero
print("and ==>",False and True)
print("or  ==>",True or False)  # Solo es verdadero si uno de los dos es verdadero
print("or  ==>",False or False)
# Se puedo utilizar solo con booleanos?
print(1 and 1)
print(1 and 0)
print(19 and 20)
print(0 and 100)

print(100 or 1)
print(-2 or 20)
print("Cristian" and "Elias")   #  string es falso si esta vacio
print("Unal" and "")

## Para pensar:
  # Desarrolle un algoritmo, que me imprima si un número es mayor de 18
  # sin utilizar el condicional if, utilice operadores lógicos para ello.

##################### Operadores de comparación ##################### 

print("mayor que     ==>",1 > 2)
print("menor que     ==>",19 < 0)
print("menor o igual ==>",-1001 >= -1001)
print("igual que     ==>",3 == -5)
print("mayor o igual ==>",19 >= 20)
print("diferente de  ==>",30 != 31)

print("Cristian" > "Elias")   #  Por orden alfabético
print(True > False)
print(True < False)           # Los toma como 1 y 0
print([20,2] > [20,1])        #Evalua posicion por posicion

##################### Operadores de pertenencia ##################### 
# Sirve para evaluar si un elemento está contenido en otro
print('"a" in "hola mundo"          ==>', "a" in "hola mundo")
print('"A" in "hola mundo"          ==>', "A" in "hola mundo")
print('"hola" in "hola mundo"       ==>', "hola" in "hola mundo")
print('" " in "hola mundo"          ==>', " " in "hola mundo")
print('1 in [1,2,3]                 ==>', 1 in [1,2,3])
print('1 in ["1", "2", "3"]         ==>', 1 in ["1", "2", "3"])
print('"3" not in "124567890"       ==>', "3" not in "124567890")
print('"01" in "0 1 2 3 4 5 6 7"    ==>', "01" in "0 1 2 3 4 5 6 7")