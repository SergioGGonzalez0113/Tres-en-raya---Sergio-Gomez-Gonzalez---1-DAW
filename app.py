import numpy as np
import random
from ttt_core import (crear_tablero, 
                    posicion_valida,
                    hacer_movimiento,
                    determinar_movimientos_disponibles,
                    movimientos_maquina, 
                    victoria,
                    hay_empate 
                    )


def imprimir_tablero(tablero):
    print("\n  0   1   2")
    i = 0
    while i < 3:
        fila = ""
        j = 0
        while j < 3:
            valor = tablero[i, j]

            if valor == 0:
                simbolo = " "
            elif valor == 1:
                simbolo = "X"
            else:
                simbolo = "O"

            if j < 2:
                fila = fila + simbolo + " | "
            else:
                fila = fila + simbolo

            j = j + 1

        print(f"{i} {fila}")

        if i < 2:
            print("  ---------")
        i += 1

def pedir_movimiento_jugador(jugador):
    fila = int(input(f"Jugador {jugador} - Fila (0-2): "))
    columna = int(input(f"Jugador {jugador} - Columna (0-2): "))
    return fila, columna

def jugar(modo_juego):
    tablero = crear_tablero()
    jugador = 1
    juego_terminado = False

    while not juego_terminado:
        imprimir_tablero(tablero)
        if modo_juego == 2 and jugador == 2:
            print("CPU pensando. . .")
            fila, columna = movimientos_maquina(tablero)
        else:
            fila, columna = pedir_movimiento_jugador(jugador)
        movimiento_valido = posicion_valida(tablero, fila, columna)
        while not movimiento_valido:
            print("El movimiento no es válido. Introduce la posción de nuevo: ")
            if modo_juego == 2 and jugador == 2:
                fila, columna = movimientos_maquina(tablero)
            else:
                fila, columna = pedir_movimiento_jugador(jugador)
            movimiento_valido = posicion_valida(tablero, fila, columna)

        tablero = hacer_movimiento(tablero, fila, columna, jugador)
        if victoria(tablero, jugador):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador} ha ganado!")
            juego_terminado = True
        else:
            if hay_empate(tablero):
                imprimir_tablero(tablero)
                print("Empate.")
                juego_terminado = True

        if not juego_terminado:
            if jugador == 1:
                jugador = 2
            else:
                jugador = 1

def menu():
    opcion = 0
    while opcion not in (1, 2):
        print("=== TRES EN RAYA ===")
        print("1. Jugador vs Jugador")
        print("2. Jugador vs CPU")
        opcion = int(input("Seleccione modo: "))
    jugar(opcion)

menu()
