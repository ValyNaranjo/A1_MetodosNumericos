import numpy as np

print("Programa para encontrar la inversa de una matriz")

#Código donde indica al usuario cuantas filas y columnas desea que sea su matriz
#en este caso vamos a considerar que sea una matriz 2x2
F = int(input("Ingrese el número de filas de su matriz: "))
C = int(input("Ingrese el número de columnas de su matriz: "))

#El usuario puede ingresar los valores de su matriz
matriz = []
print("Ingrese los valores de su matriz:")

entries = list(map(int, input().split()))

matriz = np.array(entries).reshape(F, C)
print(matriz)

#Código que muestra la matriz inversa
print("La inversa de su matriz es")
matriz = np.linalg.inv(matriz)
print(matriz)

