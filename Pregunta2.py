import numpy as np
from matplotlib import pyplot

print("Programa para graficar funciones")

a=float(input("Valor de (a):\n"))
b=float(input("Valor de (b):\n"))
c=float(input("Valor de (c):\n"))

# Función cuadrática (f(x) = x^2−x+1)
def f(x):
   return a*(x**2)+b*x+c

# Función lineal
def g(x):
   return 2*((x - 1)**-1)

# Valores del eje X que toma el gráfico
x = np.linspace(-100,100,1000)

# Graficar ambas funciones.
pyplot.plot(x, [f(i) for i in x])
pyplot.plot(x, [g(i) for i in x])

# Establecer el color de los ejes
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Limitar los valores de los ejes
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)

# Guardar gráfico como imagen PNG
pyplot.savefig("output.png")
pyplot.show()



