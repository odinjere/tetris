import numpy as np




#Tablero - Matrix 18x10

tablero = np.zeros((18, 10))

print(tablero)

#Fichas - hay 7 fichas diferentes que se pueden representar con matrices desde 2x2 hasta 4x4

#Ficha o (yellow)
o = np.array([1,1],
             [1,1])

#Ficha J (Blue)
j = np.array([0,1,0],
             [0,1,0],
             [1,1,0])

#Ficha L (orange)
l = np.array([0,1,0],
             [0,1,0],
             [0,1,1])

#Ficha s (green)
s = np.array([0,1,1],
             [1,1,0],
             [0,0,0])

#Ficha z (red)
z = np.array([1,1,0],
             [0,1,1],
             [0,0,0])

#Ficha T (violet)
t = np.array([1,1,1],
             [0,1,0],
             [0,0,0])

#Ficha I (cyan)
i = np.array([1,0,0,0],
             [1,0,0,0],
             [1,0,0,0],
             [1,0,0,0])


#Movimientos #al ser una matriz cuadrada girar las fichas es una simple opreracion matematica 

#Bolda de Fichas #la bolsa debe contener 1 de cada tipo de fichas y sacar una al azar, la bolsa se rellena al vaciarse.
