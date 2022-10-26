### Juego triqui
# Se necesitan 3 modulos: interfas.py, lógica.py, controlJuego,py 
# interfaz. py    ---> imprimirTablero (tablerologico:list)
#                 ---> explicarJuego()
# logica.py       ---> obtenerTablerologico() ---> lista
#                 ---> insertarCaracter(tablerologico, posicion, caracter)
#                 ---> determinarGanador(tablerologico)   ---> 'x', 'o', None
# ControlJuego.py ---> Aqui consumimos interfaz y logica

"""
Este modulo contiene 3 funciones:

* generarTableroLogico => No recibe nada, 
                          devuelve una lista de Nones
* insertarCaracterEnTablero => recibe lista, posicion, caracter
                               retorna una lista actualizada
* determinarGanador => recibe una lista (tablero)
                       retorna ganador ("x", "o", None)
"""

def generarTableroLogico():
    tablerologico = [None, None, None, None, None, None, None, None, None]
    return tablerologico

def insertarCaracterEnTablero(tableroLogico:list, posicion:int, caracter:str):
    tableroLogico[posicion] = caracter
    return tableroLogico

def determinarGanador(tableroLogico:list):
    ganador = None
    posicionesAComparar = [(0,1,2),
                           (3,4,5),
                           (6,7,8),
                           (0,3,6),
                           (1,4,7),
                           (2,5,8),
                           (0,4,8),
                           (2,4,6)]
    for pos1,pos2,pos3 in posicionesAComparar:
        if (tableroLogico[pos1] == tableroLogico[pos2] == tableroLogico[pos3]) and (tableroLogico[pos1] != None):
            ganador = tableroLogico[pos1]
            break
    return ganador

if __name__ == "__main__":
    tablero = generarTableroLogico()
    ganador = determinarGanador(tablero)
    print(tablero)
    print(ganador)
    tableroNuevo = insertarCaracterEnTablero(tablero, 0, "x")
    tableroNuevo = insertarCaracterEnTablero(tablero, 4, "x")
    tableroNuevo = insertarCaracterEnTablero(tablero, 8, "x")
    print(tableroNuevo)
    ganador = determinarGanador(tableroNuevo)
    print(ganador)


