"""
Aqui se controla el juego triqui
"""
from interfazJuego import explicarJuego, imprimirTablero
from logicaJuego import generarTableroLogico, determinarGanador, insertarCaracterEnTablero

explicarJuego()
jugador1 = 10
jugador2 = 11
tablero = generarTableroLogico()
while True:
    print("Ingresar posición deseada")
    jugador1 = int(input("Jugador 1 (x): "))
    while jugador1 not in range(9):
        print("Error. Posición ingresada no valida. Ingrese nuevamente.")
        jugador1 = int(input("Jugador 1 (x): "))  
    # Jugador 1
    if tablero[jugador1] == None:
        tablero = insertarCaracterEnTablero(tablero, jugador1, "x")
    else:
        while tablero[jugador1] != None:
            print("Esta posición ya está ocupada, por favor ingrese nuevamente su posición deseada")
            jugador1 = int(input("Jugador 1 (x): "))
        tablero = insertarCaracterEnTablero(tablero, jugador1, "x")
    ganador = determinarGanador(tablero)
    if None not in tablero or ganador != None: 
        imprimirTablero(tablero)
        print("El ganador es:", ganador)
        break
    # Jugador 2
    if None in tablero:
        jugador2 = int(input("Jugador 2 (o): "))
        while jugador2 not in range(9):
            print("Error. Posición ingresada no valida. Ingrese nuevamente.")
            jugador2 = int(input("Jugador 2 (o): "))
        
        if tablero[jugador2] == None:
            tablero = insertarCaracterEnTablero(tablero, jugador2, "o")
        else:
            while tablero[jugador2] != None:
                print("Esta posición ya está ocupada, por favor ingrese nuevamente su posición deseada")
                jugador2 = int(input("Jugador 2 (o): "))
            tablero = insertarCaracterEnTablero(tablero, jugador2, "o")
    
    tableroVisual = imprimirTablero(tablero)
    ganador = determinarGanador(tablero)
    if None not in tablero or ganador != None: 
        print("El ganador es:", ganador)
        break




