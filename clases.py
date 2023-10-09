import numpy as np
from random import randint
'''
class Barco:

    def __init__(self, size, x, y, orientacion):
        self.size = size
        self.x_ini = x
        self.y_ini = y
        self.orientacion = orientacion

    def dibujar_barco(self):
        if self.orientacion == 0:
            barco = np.full((3, self.size+2), '-')
            for i in range(self.size):
                barco[1][i+1] = 'O'
            return barco        
        elif self.orientacion == 1:
            barco = np.full((self.size+2, 3), '-')
            for i in range(self.size):
                barco[i+1][1] = 'O'
            return barco
        else:
            print('Error. Orientación incorrecta. Debe ser un valor 0(horizontal) o 1(vertical).')
        
'''

    

    

class Tablero:
    def __init__(self, id_jugador, size, n_ship4, n_ship3, n_ship2, n_ship1):
        self.size = size
        self.tablero_barcos = np.full((size,size), ' ')
        self.n_ship4 = n_ship4
        self.n_ship3 = n_ship3
        self.n_ship2 = n_ship2
        self.n_ship1 = n_ship1
        self.tablero_visible = np.full((size,size), ' ')

    def recibir_disparo(self, x, y):
        print(x)
        print(y)
        print(self.tablero_barcos[y][x])
        if self.tablero_barcos[y][x] == ' ':
            print('¡Agua!')
            self.tablero_barcos[y][x] = '-'
            self.tablero_visible[y][x] = '-'
        elif self.tablero_barcos[y][x] == 'O':
            print('¡Barco!')
            self.tablero_barcos[y][x] = 'X'
            self.tablero_visible[y][x] = 'X'
        else:
            print('¡Ya habías intentado esa casilla antes!')

    def colocar_barcos(self):
        for i in range(self.n_ship4):
            while True:
                x = randint(0, self.size - 4)
                y = randint(0, self.size - 4)
                dir = randint(0, 1)
                if dir == 0:
                    if self.tablero_barcos[y][x] == ' ' and self.tablero_barcos[y+1][x] == ' ' and self.tablero_barcos[y+2][x] == ' 'and self.tablero_barcos[y+3][x] == ' ':
                        self.tablero_barcos[y][x] = 'O' 
                        self.tablero_barcos[y+1][x] = 'O' 
                        self.tablero_barcos[y+2][x] = 'O'
                        self.tablero_barcos[y+3][x] = 'O'             
                        break
                elif dir == 1:
                    if self.tablero_barcos[y][x] == ' ' and self.tablero_barcos[y][x+1] == ' ' and self.tablero_barcos[y][x+2] == ' ' and self.tablero_barcos[y+3][x+3] == ' ':
                        self.tablero_barcos[y][x] = 'O' 
                        self.tablero_barcos[y][x+1] = 'O' 
                        self.tablero_barcos[y][x+2] = 'O'
                        self.tablero_barcos[y][x+3] = 'O'
                        break
        for i in range(self.n_ship3):
            while True:
                x = randint(0, self.size - 3)
                y = randint(0, self.size - 3)
                dir = randint(0, 1)
                if dir == 0:
                    if self.tablero_barcos[y][x] == ' ' and self.tablero_barcos[y+1][x] == ' ' and self.tablero_barcos[y+2][x] == ' ':
                        self.tablero_barcos[y][x] = 'O' 
                        self.tablero_barcos[y+1][x] = 'O' 
                        self.tablero_barcos[y+2][x] = 'O'            
                        break
                elif dir == 1:
                    if self.tablero_barcos[y][x] == ' ' and self.tablero_barcos[y][x+1] == ' ' and self.tablero_barcos[y][x+2] == ' ':
                        self.tablero_barcos[y][x] = 'O' 
                        self.tablero_barcos[y][x+1] = 'O' 
                        self.tablero_barcos[y][x+2] = 'O'
                        break
        for i in range(self.n_ship2):
            while True:
                x = randint(0, self.size - 2)
                y = randint(0, self.size - 2)
                dir = randint(0, 1)
                if dir == 0:
                    if self.tablero_barcos[y][x] == ' ' and self.tablero_barcos[y+1][x] == ' ':
                        self.tablero_barcos[y][x] = 'O' 
                        self.tablero_barcos[y+1][x] = 'O'            
                        break
                elif dir == 1:
                    if self.tablero_barcos[y][x] == ' ' and self.tablero_barcos[y][x+1] == ' ':
                        self.tablero_barcos[y][x] = 'O' 
                        self.tablero_barcos[y][x+1] = 'O' 
                        break
        for i in range(self.n_ship1):
            while True:
                x = randint(0, self.size - 1)
                y = randint(0, self.size - 1)
                dir = randint(0, 1)
                if dir == 0:
                    if self.tablero_barcos[y][x] == ' ':
                        self.tablero_barcos[y][x] = 'O'           
                        break
                elif dir == 1:
                    if self.tablero_barcos[y][x] == ' ':
                        self.tablero_barcos[y][x] = 'O' 
                        break







    