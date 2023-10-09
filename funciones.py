from clases import *
from time import sleep
from random import randint

def menu():
    print('HUNDIR LA FLOTA')
    print('Elige la opción:')
    print('a - Jugar.')
    print('h - Imprime este menú.')
    print('exit - Salir del juego')

def juego():
    tablero_jugador = Tablero('Rai',10,1,2,3,4)
    tablero_maquina = Tablero('Rai',10,1,2,3,4)
    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()
    
    while 'O' in tablero_jugador.tablero_barcos and 'O' in tablero_maquina.tablero_barcos:
        print('Tu turno:')
        print(tablero_maquina.tablero_visible)
        print('Dime tus disparos:')
        y = int(input('Fila: '))
        x = int(input('Columna: '))
        tablero_maquina.recibir_disparo(x, y)
        print(tablero_maquina.tablero_visible)
        sleep(3)
        print('Turno de la máquina:')
        print(tablero_jugador.tablero_barcos)
        print('Pensando disparos disparos.')
        sleep(2)
        a = randint(0,9)
        b = randint(0,9)
        tablero_jugador.recibir_disparo(a, b)
        print(tablero_jugador.tablero_barcos)
        print(f'Disparos de la máquina: [{a}][{b}]')
        sleep(4)
    print('GAME OVER')



def main():
    menu()
    opt = input('\nEscribe tu opción: ')
    while opt != 'exit':
        if opt == 'a':
            juego()
        elif opt == 'h':
            menu()
            opt = input('\nEscribe tu opción: ')
        else:
            print('Opción no válida. Pulsa h para obtener ayuda.')
            opt = input('\nEscribe tu opción: ')
