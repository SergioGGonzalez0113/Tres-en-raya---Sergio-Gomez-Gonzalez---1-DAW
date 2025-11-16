import numpy as np
import random

def crear_tablero():
    return np.zeros((3,3), dtype=int)

def posicion_valida(tablero, fila, columna):
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        return False
    if tablero[fila, columna] != 0:
        return False
    return True

def hacer_movimiento(tablero , fila, columna, jugador):
    tablero[fila, columna] = jugador
    return tablero

def determinar_movimientos_disponibles(tablero):
    huecos_libres = []
    for hueco in range(3):
        for jugada in range(3):
            if tablero[hueco, jugada] == 0:
                huecos_libres.append((hueco, jugada))
    return huecos_libres

def movimientos_maquina(tablero):
    huecos_libres = determinar_movimientos_disponibles(tablero)
    movimiento = len(huecos_libres)
    if movimiento > 0:
        posicion = random.randint(0, movimiento - 1)
        return huecos_libres[posicion]
    return None

def victoria(tablero, jugador):
    for i in range(3):
        #victoria fila
        if tablero[i, 0] == jugador and tablero[i, 1] == jugador and tablero[i, 2] == jugador:
            return True
        #victoria columna
    for j in range(3):
        if tablero[0, j] == jugador and tablero[1, j] == jugador and tablero[2, j] == jugador:
            return True
        #victoria diagonal 1
    if tablero[0, 0] == jugador and tablero[1, 1] == jugador and tablero[2, 2] == jugador:
        return True
        #victoria diagonal 2
    if tablero[0, 2] == jugador and tablero[1, 1] == jugador and tablero[2, 0] == jugador:
        return True
    return False

def hay_empate(tablero):
    libres = determinar_movimientos_disponibles(tablero)
    if len(libres) == 0:
        return True
    return False
