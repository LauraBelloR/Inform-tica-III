"""
Aqui contenemos la parte visual del triqui. Este modulo contiene dos funciones:

* explicarJuego: retomar mensaje explicativo
* imprimirTablero: retomar string con el tablero

"""

def explicarJuego():
    explicacion = """
    =================================================
    Bienvenido, esto es triki.

    Para ganar debe completar una linea recta,
    compuesta por un mismo caracter ("x" o "o")

    Linea recta => horizontal o vertical o diagonal

    Debe ingresar la posicion 0-8, para ingresar 
    la opción durante su turno. Las posiciones son
    las siguientes:
    tablero ==>     0 | 1 | 2
                   -----------
                    3 | 4 | 5
                   -----------
                    6 | 7 | 8  
    =================================================
    """
    print(explicacion)

def imprimirTablero(tablerologico:list):
    tableroVisual = """
     {} | {} | {}
    -----------
     {} | {} | {}
    -----------
     {} | {} | {}  
    
    """.format(tablerologico[0],tablerologico[1],tablerologico[2],tablerologico[3],
    tablerologico[4],tablerologico[5],tablerologico[6], tablerologico[7],
    tablerologico[8])
    tableroVisual = tableroVisual.replace("None"," ")

    print(tableroVisual)

if __name__ == "__main__":
    explicarJuego()
    tableroLogico = ["x"]*9
    imprimirTablero(tableroLogico)


